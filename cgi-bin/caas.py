#!/usr/bin/python2
print "content-type:text/html"
print 
import os,cgi,commands,cgitb,random
cgitb.enable()
content=cgi.FormContent()
os.system("sudo iptables -F")
os.system("sudo setenforce 0")
u=str(content['caas_user'][0])
p=str(content['caas_pass'][0])
n=content['container'][0]
for i in range(int(n)):
	a=str(random.randint(5000,7000))
	commands.getstatusoutput("sudo docker run -itd -p "+a+":4200 --name "+u+"_"+a+" caas")
	q=commands.getstatusoutput("sudo docker exec "+u+"_"+a+" hostname -i")
	print "<a href='http://192.168.43.163:"+a+"' target='_blank'>"+q[1]+"</a>"

