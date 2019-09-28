#!/usr/bin/python36
print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()

docker_name=form.getvalue("n")
docker_image=form.getvalue("img")

x = sp.getoutput(f"sudo docker run -dit --name {docker_name}  {docker_image} ")
print(x)
