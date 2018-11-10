#!/usr/bin/python2
print "content-type:text/html"
print 


import os,commands,cgi,cgitb
cgitb.enable()
content=cgi.FormContent()
os.system("sudo iptables -F")
os.system("sudo setenforce 0")
u=str(content['existing_user'][0])
p=str(content['existing_pass'][0])
h=commands.getstatusoutput("cat /port.txt |grep "+u+" |cut -d':' -f3")
aqw=h[1].split("\n")
print "<center><h1>operating system gallery</h1></center>"
for i in aqw:
		mybut=commands.getstatusoutput("cat /port.txt|grep "+i+"|cut -d':' -f1")
		print'''
	
	
				
				
		<form action="/cgi-bin/hi.py"><input type="submit" name="'''+i+'''" value="'''+mybut[1]+'''" ></form>'''	
				




					


				
	


