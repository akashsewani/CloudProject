#!/usr/bin/python2
print "content-type:text/html"
print ""

import commands,cgi,cgitb
cgitb.enable()

content=cgi.FormContent()
key=content.keys()
value=content.values(key[0])
commands.getstatusoutput("sudo virsh start "+value[0])

print "<body onload=\"javascript:window.open('http://192.168.43.163?host=192.168.43.163&port="+key[0]+"','_blank');\">"



