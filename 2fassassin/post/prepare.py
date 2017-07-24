#!/usr/bin/env python


from subprocess import call
import sys, os, re


out = "/root/.msf4/loot/usernames.txt"

def looted_user():
    '''
    fin = "ssh_login.txt"
    with open(fin,'r') as f:
        for line in f.readlines():
            if "home" in line:
                idx1 = line.find('"')
                idx2 = line.find('"', idx1+1)
                field = line[idx1+1:idx2-1]
            else:
'''
os.system("cat /root/.msf4/loot/ssh_login.txt | \
                awk '{ print $3 }' | \
                grep / | \
                awk '{print substr($0,7)}' | \
                awk -F/ '{print $1}' | grep -v .ssh | \
                sort -u > /root/.msf4/loot/usernames.txt")
                #print(field); f = open('out.txt', 'w');print >> f, 'output:', field  # or f.write('...\n')
                #f.close()
'''
                break
                orig_stdout = sys.stdout
                f = open('out.txt', 'w')
                sys.stdout = f
            for i in range(2):
                #print 'i = ', i
                sys.stdout = orig_stdout
                f.close()

'''

def clarify():
    with open(out, 'r') as fin:
        data = fin.read().splitlines(True)
        with open(out, 'w') as fout:
            fout.writelines(data[3:])

def root():
    with open(out, "a") as shit:
        shit.write("root")
        shit.write("")


__all__ = ['looted_user', 'clarify', 'root']
