#!/usr/bin/env python


import sys, os

def remove(filename):
    openssl = ""
    openssl += "openssl rsa -in %s -out crack" %filename
    openssl += "expect "testing""
    os.system(openssl)
    sys.exit(0)

def main():
    try:
        keyname = "testkey"
        remove(keyname)
    except KeyboardInterrupt:
        print bcolors.RED+"\nCaught Ctrl-C, GraceFul Exit. POOOF"+bcolors.ENDC


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()
