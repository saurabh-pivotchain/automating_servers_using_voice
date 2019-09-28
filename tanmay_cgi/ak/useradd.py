#!/usr/bin/python36
import subprocess as sp
import cgi

print("content-type: text/html")
print()


mydata=cgi.FieldStorage()
b=mydata.getvalue('q')

y=sp.getoutput(f"sudo useradd {b}")
z=sp.getoutput(f"id {b}")
print(y)
print(z)
