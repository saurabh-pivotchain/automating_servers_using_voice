#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()
form = cgi.FieldStorage()
u = form.getvalue('q')
a = sp.getoutput("sudo touch " + u)
print("File created")


