#!/usr/bin/env python

from py.path import local
import glob
import os
import sys
import shutil

def keyhunt(path):
    file_ext = [".pem", ".key", ".pkcs12", ".pfx", ".p12", "pkcs12", "der", "asc"]
    file_names = ["key", "id_rsa"]
    return (path.ext in file_ext) or (path.purebasename in file_names)

print ""
print "############ Detect suspicious files ############ \n"

for path in local("/root/.msf4/loot/.").visit(keyhunt):
    src = path.strpath
    dst = '../loot/'
    print src + "   ----------> Potential private key found :) !!!\n"
    shutil.copy2(src,dst)  # copy potential private keys to ../loot/



print ""
print "\n\n############ Look deeper into the file content ############\n"

for files in glob.glob( "/root/.msf4/loot/*" ):
    if files=="getpriv.py":
        continue
    f = open( files, 'r' )
    file_contents = f.read()

    if "PRIVATE" or "key" in file_contents:
            print f.name + "  ----------> Potential private key found :) !!!\n"
            a = f.name
            b = '../loot/'
            shutil.copy2(a,b)   # copy potential private keys to ../loot/
    else:
        print f.name + "  ----------> NO private key found :( \n"
    f.close()


print ""
print "\n\n############ Potential private keys store @ ../loot ############\n"
print ".\n.\n"
print " ........... Done ........\n"

def main():
    try:
        keyhunt()
        pass
        store()
    except KeyboardInterrupt:
        print bcolors.RED+"\nCaught Ctrl-C, GraceFul Exit. POOOF"+bcolors.ENDC


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()
