#!/usr/bin/python36
print("content-type: text/html")
print()


import subprocess as sp
import cgi

form = cgi.FieldStorage()
cname=form.getvalue("s")
cmd="sudo docker stop {}".format(cname)
x=sp.getoutput(cmd)
print('<meta http-equiv="refresh" content="2; url= http://192.168.29.76/cgi-bin/tanmay_cgi/ak/docker_live_menu.py">')
