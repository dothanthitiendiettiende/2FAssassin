#!/usr/bin/env python


import paramiko
from paramiko import rsakey


def cracker():
    kf = open("testkey", "r")
    dlist = ["foo", "bar", "foobar", "klunssi", "xyzzy", "testing"]
    for d in dlist:
        kf.seek(0)
        try:
            nk = rsakey.RSAKey.from_private_key(kf, password=d)
            print "success", d
        except paramiko.ssh_exception.SSHException:
            print "fail", d


def main():
    try:
        cracker()
    except KeyboardInterrupt:
        print bcolors.RED+"\nCaught Ctrl-C, GraceFul Exit. POOOF"+bcolors.ENDC


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()
