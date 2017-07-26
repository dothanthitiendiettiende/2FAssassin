#!/usr/bin/python

import os
from getpass import getpass

import paramiko

def deploy_key(key, server, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, username="user3", password="password")
    client.exec_command('mkdir -p ~/.ssh/')
    client.exec_command('echo "%s" >> ~/.ssh/authorized_keys' % key)
    client.exec_command('chmod 644 ~/.ssh/authorized_keys')
    client.exec_command('chmod 700 ~/.ssh/')

key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()
username = os.getlogin()
password = getpass()
hosts = ["172.16.173.191", "172.16.173.187"]
for host in hosts:
    deploy_key(key, host, username, password)
