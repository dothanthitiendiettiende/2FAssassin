#!/usr/bin/env python

import re
import sys, os


def insert():
    IE_script = '"C:\Program Files\Internet Explorer\iexplore.exe" https://2fassassin.com'
    filename = "/root/2fassassin/cert/transport/instruction/key.bat"
    with open(filename, "a") as myfile:
        myfile.write(IE_script)
        sys.exit()


'''
def replace():
    str = "C:\Program Files\Internet Explorer\iexplore.exe"
    print str.replace("C:\Program Files\Internet Explorer\iexplore.exe", ""C:\Program Files\Internet Explorer\iexplore.exe"")
'''

def test():
    print "you access writer module"
    sys.exit()

__all__ = ['insert']
