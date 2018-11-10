#!/usr/bin/python2
print "content-type:text/html"
print ""
 
import os,cgi,commands,cgitb
cgitb.enable()
content=cgi.FieldStorage()
os.system("sudo iptables -F")
os.system("sudo setenforce 0")
u=content.getvalue('username')
p=content.getvalue('password')
a=commands.getstatusoutput("cat /var/www/cgi-bin/mariadb.txt |grep "+u+"| cut -d'|' -f1| cut -d':' -f2")
b=commands.getstatusoutput("cat /var/www/cgi-bin/mariadb.txt |grep "+u+"| cut -d'|' -f2| cut -d':' -f2")
print a 
print b

if u == a[1] and p == b[1] :
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.163/menu.html\">\n"
else:
	print "not authorised"
