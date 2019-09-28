#!/usr/bin/python36
import cgi
import subprocess as sb
print("content-type: text/html")
print()

form=cgi.FieldStorage()
b=form.getvalue("text")

if "adduser" in b or "useradd" in b:
        print('<meta http-equiv="refresh" content="1; url= http://192.168.29.76/tanmay_html/useradd.html">')
	#print("location: http://192.168.29.76/tanmay_html/useradd.html")
        print()

elif "docker" in b and "show" in b:
	print('<meta http-equiv="refresh" content="1; url= http://192.168.29.76/cgi-bin/tanmay_cgi/ak/docker_live_menu.py">')
	#print("location: http://192.168.29.76/cgi-bin/tanmay_cgi/ak/docker_live_menu.py")
	print()
elif "docker" in b and "add" in b:
	print('<meta http-equiv="refresh" content="1; url= http://192.168.29.76/tanmay_html/ak/docker.html">')
	#print("location: http://192.168.29.76/tanmay_html/ak/docker.html")
	print()
elif "machine" in b and "learning" in b or "train" in b:
	print('<meta http-equiv="refresh" content="1; url= http://192.168.29.76/cgi-bin/tanmay_cgi/ak/ml.py">')
	#print("location: http://192.168.29.76/cgi-bin/tanmay_cgi/ak/ml.py")
	print()
elif "send" in b and "SMS" in b:
	print('<meta http-equiv="refresh" content="1; url= http://192.168.29.76/tanmay_html/ak/sms.html">')
	#print("location: http://192.168.29.76/tanmay_html/ak/sms.html")
	print()
elif "S3" in b and "launch" in b:
	print('<meta http-equiv="refresh" content="1; url= http://192.168.29.76/tanmay_html/ak/s3.html">')	
	#print("location: http://192.168.29.76/tanmay_html/ak/s3.html")
	print()		 
elif "EC2" in b and "launch" in b:
	print('<meta http-equiv="refresh" content="1; url= http://192.168.29.76/cgi-bin/tanmay_cgi/ak/ec2.py">')	
	#print("location: http://192.168.29.76/cgi-bin/tanmay_cgi/ak/ec2.py")
	print()		
elif "send" in b and "mail" in b:
	print('<meta http-equiv="refresh" content="1; url= http://192.168.29.76/tanmay_html/ak/mail.html">')	
	#print("location: http://192.168.29.76/tanmay_html/ak/mail.html")
	print()		
elif "setup" in b and "hadoop" in b:
	#print('<meta http-equiv="refresh" content="1; url= http://192.168.29.76/cgi-bin/tanmay_cgi/ak/hadoop.py">')
	a=sb.getoutput('ansible-playbook ./hadoopnamenode.yml')
	print(a)
	print()
	#print("location: http://192.168.29.76/cgi-bin/tanmay_cgi/ak/hadoop.py")
	print()	
elif "setup" in b and "proxy" in b:
	#print('<meta http-equiv="refresh" content="1; url= http://192.168.29.76/tanmay_html/ak/docker.html">')
	a=sb.getoutput('ansible-playbook ./haproxy_project/myproject/site.yml')
	print(a)
	print()		 
		
	

