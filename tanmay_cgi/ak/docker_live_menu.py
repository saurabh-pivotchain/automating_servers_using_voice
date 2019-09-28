#!/usr/bin/python36
print("content-type: text/html")
print()

import subprocess as sp

print(f'''
<table border='5' width='100%'>
<tr>
<th>docker name</th>
<th>docker image</th>
<th>Status</th>
<th>start</th>
<th>stop</th>
<th>terminate</th>
<th>console</th>
</tr>
''')


x = sp.getoutput("sudo docker ps -a")
cont_list = x.split("\n")

for c in cont_list[1:]:
	c_name=c.split()[-1]
	c_image=c.split()[1]
	if 'Up' in c:
		cstatus='running'
	elif 'Exited' in c:
		cstatus='stopped'
	else:
		cstatus='unknown'
	print(f'''
        <tr>
	<td>{c_name}</td>
	<td>{c_image}</td>
	<td>{cstatus}</td>
	<td><a href='http://192.168.29.76/cgi-bin/tanmay_cgi/ak/docker_start.py?s={c_name}'>Start</a></td>
	<td><a href='http://192.168.29.76/cgi-bin/tanmay_cgi/ak/docker_stop.py?s={c_name}'>Stop</a></td>
	<td><a href='http://192.168.29.76/cgi-bin/tanmay_cgi/ak/docker_terminate.py?s={c_name}'>Terminate</a></td>
	<td><a target='myconsole' href='http://192.168.29.76:4200'>console</a></td>
	</tr>''')


print("</table>")
