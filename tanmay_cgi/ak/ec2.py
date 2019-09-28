#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()
a = sp.getoutput("sudo ansible-playbook my_ec2.yml")
print("ec2 instance launch")
