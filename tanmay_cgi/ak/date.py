#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html \n")
print()
x = sp.getoutput("date")   
print("Output: "+ x)

                      
