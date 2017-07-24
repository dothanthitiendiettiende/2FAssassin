#!/usr/bin/env python

import os, sys, time
import re
import subprocess
from subprocess import Popen #PIPEort subprocess



def run_command(command):
    p = subprocess.Popen(command,
    stdout=subprocess.PIPE,
    bufsize=-1,
    stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')



 '''
floppy = os.
system("ls /root/2fassassin/loot/*.pfx")

command = "openssl pkcs12 -info -in"
command += " "
command += +floppy
command += " "
command += "-nomacver -noout -passin pass:unknown".split()
'''

command = "openssl pkcs12 -info -in /root/2fassassin/loot/ClientCert.pfx -nomacver -noout -passin pass:unknown".split()


for line in run_command(command):
    print(line)



word = "Encrypted"
for line in run_command(command):
    if word in line:
        for _ in range(re.findall(r"\w+", line).count(word)):
            print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
            print "   Encrypted file detected! Let's cracking passwords!  \n"
            print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
