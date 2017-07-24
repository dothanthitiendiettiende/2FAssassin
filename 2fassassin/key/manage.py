#!/usr/bin/env python


import paramiko
from paramiko import rsakey
import sys
import os

'''
def verify():
    exit()

def detect():
    exit()
'''

def crack():
    kf = open("../loot/cipher", "r")
    dlist = ["foo", "bar", "foobar", "klunssi", "xyzzy", "testing"]
    for d in dlist:
        kf.seek(0)
        try:
            nk = rsakey.RSAKey.from_private_key(kf, password=d)
            print "Passphrase correct: ", d
        except paramiko.ssh_exception.SSHException:
            print "Passphrase is not: ", d


def remove():
    print "Congrajulation, you got the right passphrase: ", d


'''
def remove(filename):
    openssl = ""
    openssl += "openssl rsa -in %s -out crack" %filename
    openssl += "expect "testing""
    os.system(openssl)
    sys.exit(0)

'''

def replace():
    # print
    exit()


def main():
    try:
        crack()
        remove()
    except KeyboardInterrupt:
        print bcolors.RED+"\nCaught Ctrl-C, GraceFul Exit. POOOF"+bcolors.ENDC


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()
