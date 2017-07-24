#!/usr/bin/python

from struct import pack, unpack
import sys
import re

class MemoryDumpError(Exception):
    """ Custom Error Messages """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)

class MemoryDumpModule(object):
    """ Module Parent Object """

    MODULE_NAME = "dummy"
    HEADER_PATTERN = ""

    def __init__(self, dump):
        self.dump = dump
        self.offsets = [ match.start() for match in re.finditer(self.HEADER_PATTERN, dump) ]
        self.items = {}

    def __len__(self):
        return len(self.offsets)

    def analyse(self):
        """ overwrite me """

        pass

    def save(self):
        """ extract module specific data from memory dump and save it to disk """

        for offset, length in self.items.iteritems():
            open("%s-%s.extract" % (self.MODULE_NAME, offset), 'wb').write(self.dump[offset:offset + length])

class MemoryDump(object):
    """ Analyse memory dumps and extract content from it """

    _extractionModules = ( 'SQLite3Database', 'PEMPrivateKey', 'PEMCertificate')
    _loadedModules = []

    def __init__(self, dumpfile):
        self.dumpfile = dumpfile
        self.items = {}

        try:
            self.dump = open(self.dumpfile, 'rb').read()
        except:
            raise MemoryDumpError("Unable to open dumpfile: %s" % (self.dumpfile, ))
        else:
            for target in self._extractionModules:
                self._loadedModules.append(eval("%s(self.dump)" % (target, )))

    def __getitem__(self, key):
        return self.items[key] 

    def __iter__(self):
        return self.items.iteritems()

    def analyze(self):
        """ find items for every loaded module in memory dump """

        for module in self._loadedModules:
            if len(module):
                module.analyze()
                self.items.update({module.MODULE_NAME: module.items})

    def extract(self):
        """ extract the found items from memory dump and save them to disk """

        for module in self._loadedModules:
            if len(module):
                if not len(self.items.keys()):
                    module.analyze()
                module.save()

class SQLite3Database(MemoryDumpModule):
    """ Extract SQLite3 Databases from Memory Dumps """

    MODULE_NAME = "sqlite"
    HEADER_PATTERN = re.escape("\x53\x51\x4c\x69\x74\x65\x20\x66\x6f\x72\x6d\x61\x74\x20\x33\x00")
    HEADER_SIZE = 100

    header_spec = {}
    header_spec['page_size'] = (16, 2, '>H')
    header_spec['page_num'] = (28, 4, '>I')

    def analyze(self):
        header = {}

        if not len(self):
            return None

        for dump_offset in self.offsets:
            for attrib, value in self.header_spec.iteritems():
                offset, length, format = value
                header[attrib] = unpack(format, self.dump[dump_offset:][offset:][:length])[0]

            self.items[dump_offset] = self.HEADER_SIZE + (header['page_num'] * header['page_size'])

        return len(self.items.keys())

class PEMPrivateKey(MemoryDumpModule):
    """ Extract RSA/DSA Private Keys in PEM format from Memory Dumps """

    MODULE_NAME = "privatekey"
    HEADER_PATTERN = r'-+BEGIN [A-Z]{3} PRIVATE KEY'
    FOOTER_PATTERN = r'-+END [A-Z]{3} PRIVATE KEY-+'

    def analyze(self):
        if not len(self):
            return None

        for dump_offset in self.offsets:
            key_len = int(re.search(self.FOOTER_PATTERN, self.dump[dump_offset:]).end())
            self.items[dump_offset] = key_len

        return len(self.items.keys())

class PEMCertificate(MemoryDumpModule):
    """ Extract Certificates in PEM format from Memory Dumps """

    MODULE_NAME = "certificate"
    HEADER_PATTERN = r'-+BEGIN CERTIFICATE'
    FOOTER_PATTERN = r'-+END CERTIFICATE-+'

    def analyze(self):
        if not len(self):
            return None

        for dump_offset in self.offsets:
            key_len = int(re.search(self.FOOTER_PATTERN, self.dump[dump_offset:]).end())
            self.items[dump_offset] = key_len

        return len(self.items.keys())

def main():
    print "[*] MemoryDump analyzer / extraction utility v0.1"

    if len(sys.argv) < 2:
        print "usage: %s <memory dump>" % (sys.argv[0], )
        return

    filename = sys.argv[1]
    try:
        memdump = MemoryDump(filename)
        memdump.analyze()
    except MemoryDumpError, err:
        print "[-] Error: %s" % (str(err), )
        return

    for module, items in memdump:
        print "[*] Modul: %s [ %d items ]\n [+]" % (module, len(items.keys())),
        print "\n [+] ".join([ "offset: 0x%08x - length: %d" % (offset, length) for offset, length in items.iteritems() ])
    #memdump.extract()

if __name__ == '__main__':
  main()
