#!/usr/bin/env python

import os, sys, time
import re
import subprocess
from subprocess import Popen 

def analyze():
    print "\n [Path] : [Type]"
    print "\n-------------------------------------------------"
    os.system("file /root/2fassassin/loot/*.pfx")
    print "\n-------------------------------------------------"
    print "\n"

    command = "openssl pkcs12 -info -in /root/2fassassin/loot/ClientCert.pfx -nomacver -noout -passin pass:unknown".split()

    def keyword (command):
        p = subprocess.Popen(command,
        stdout=subprocess.PIPE,
        bufsize=-1,
        stderr=subprocess.STDOUT)
        return iter(p.stdout.readline, b'')

    for line in keyword(command):
        print(line)

    word = "Encrypted"
    for line in keyword(command):
        if word in line:
            for _ in range(re.findall(r"\w+", line).count(word)):
                print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                print "   [Detected]:  SSL Client Certificate PKCS#12 (X509 certs family)   \n"
                print "                        (Password Protected)                         \n"
                print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"


'''
def searchpfx():
    directory = "/root/2fassassin/loot/"
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pfx'):
                return file


def generator():
    _FILE = searchpfx()
    print __FILE
    #keyword(__FILE)


def main():
    try:
        generator()
    except KeyboardInterrupt:
        print bcolors.RED+"\nCaught Ctrl-C, GraceFul Exit. POOOF"+bcolors.ENDC

if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()
'''
