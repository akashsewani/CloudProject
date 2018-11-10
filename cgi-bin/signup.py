#!/usr/bin/python2
print "content-type:text/html"
print
import os,cgi,commands,cgitb
cgitb.enable()
content=cgi.FormContent()
u=content['username'][0]
p=content['password'][0]
a=commands.getstatusoutput("cat /var/www/cgi-bin/mariadb.txt")
if u in a[1]:
	print "user already exists"
	print'''<html id="qwe">
	<head>
	<script>
	function login():
	{
		document.innerHTML='signup.html';
	}
	</script>
	</head>
	<center><a href="http://192.168.43.163/signup.html" display="none"><input type='button' value='try again' /></a></center>
	</html>
	'''
else: 
	f=open('mariadb.txt','a')
	f.write('\nusername:'+u+'|  password:'+p+'\n')
	f.close()
	commands.getstatusoutput("sudo useradd "+u)
	commands.getstatusoutput("sudo echo -e "+p+"|passwd "+u+" --stdin")
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=/index1.html\">\n"



