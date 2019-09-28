#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()
form = cgi.FieldStorage()
b1 = form.getvalue('from')
b2 = form.getvalue('to')
b3 = form.getvalue('message')
print(b1)
print(b2)
print(b3)
f1 = open("smsfrom.yml",'w')
f1.write(f"from: {b1}\n")
f1.close()

print("<h3>dasjdgya</h3>")

f1 = open("smsfrom.yml",'a')
f1.write(f"to: {b2}\n")
f1.close()

print("dasjdgya")

f1 = open("smsfrom.yml",'a')
f1.write(f"message: {b3}\n")
f1.close()

print("<u>sending message</u>")
x = sp.getstatusoutput("sudo ansible-playbook sms.yml")
print("Message sent successfully.")


