#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 21:24:32 2017

@author: Mitnik
"""
import paramiko
import threading

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.0.2.15',username='Mitnik',password='crypto')
chan = client.get_transport().open_session()
chan.send('Hello! we connected')
print chan.recv(1024)
client.close


