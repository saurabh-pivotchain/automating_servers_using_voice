#!/usr/bin/python36
import subprocess as sp

print("content-type: text/html")
print()
print("<form action='http://192.168.29.76/cgi-bin/tanmay_cgi/ak/docker_run.py'>")
print("Enter your docker name : <input name='n' /><br>")

print("Enter your image name :")
print("<select name='img'>")

x = sp.getoutput("sudo docker images")
for i in x.split("\n")[1:]:
    j = i.split()
    print("<option>"+j[0]+":"+j[1])

print("</select>")
print("<br><input type='submit'>")
print("</form>")
