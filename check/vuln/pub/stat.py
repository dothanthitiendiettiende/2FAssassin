#!/usr/bin/env python

import sys, os

def origin(user_origin):
    print "The user '%s'" %user_origin +" is found on host:  "
    cmd = ""
    cmd += "cat /root/.msf4/loot/ssh_login.txt | grep Downloaded | grep /home/%s" %user_origin
    cmd += " | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' | sort -u"
    os.system(cmd)
    sys.exit()

def accountxxx(computer):
    print "\n #### These user accounts on host '%s'" %computer +" are potentially accessible ####  \n"
    cmd = ""
    cmd = "cat /root/.msf4/loot/ssh_login.txt | grep Downloaded | grep /home | grep %s" %computer
    cmd += " | grep authorized* |awk '{ print $3}' | sort -u"
    os.system(cmd)
    print "\n"
    sys.exit()

def userxxx():
    os.system("bash -c 'source /root/2fassassin/check/vuln/pub/sc; accessibility'")

def machinexxx():
    os.system("bash -c 'source /root/2fassassin/check/vuln/pub/sc; authorized'")

__all__ = ['user_origin', 'computer', 'userxxx', 'machinexxx']
