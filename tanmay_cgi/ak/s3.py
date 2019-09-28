#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()
form = cgi.FieldStorage()

print("tanmay")
b1 = form.getvalue('myfile')
f1 = open("s3data.yml",'w')
f1.write(f"file: {b1}")
f1.close()
print("<u>file uploading</u>"+"</br>")
a = sp.getstatusoutput("sudo ansible-playbook s3.yml")
print(a)
print("File uploaded.")

