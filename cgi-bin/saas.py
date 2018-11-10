#!/usr/bin/python2
print "content-type:text/html\n"
print 

 
import os,cgi,commands,cgitb
cgitb.enable()
content=cgi.FormContent()
os.system("sudo iptables -F")
os.system("sudo setenforce 0")
p=content['saas_pass'][0]
u=content['saas_user'][0]
app=content['app'][0]
a=commands.getstatusoutput("cat /var/www/cgi-bin/mariadb.txt |grep "+u+"|  cut -d':' -f2")
if u in a[1]:
	os.system("sudo yum install openssh-server -y >/dev/null 2>/dev/null")
	os.system("sudo systemctl restart sshd")
	if app == "firefox" :
		os.system("sudo touch /p.py")
		os.system("sudo chmod 777  /p.py")		
		f=open('/p.py','w')	
		f.write("#!/usr/bin/python2\n")
		f.write("import os\n")
		f.write("os.system('setenforce 0')\n")
		f.write("os.system('iptables -F')\n")
		f.write("os.system('touch /etc/yum.repos.d/client.repo')\n")
		f.write("p=open('/etc/yum.repos.d/client.repo','w')\n")
		f.write("p.write('[client]\\n')\n")
		f.write("p.write('baseurl=ftp://192.168.43.163/pub/yum/Packages/\\n')\n")
		f.write("p.write('gpgcheck=0\\n')\n")
		f.write("p.close()\n")
		f.write("os.system('yum install openssh-clients -y >/dev/null 2>/dev/null')\n")
		f.write("os.system('yum install sshpass -y >/dev/null 2>/dev/null')\n")
		f.write("os.system('sshpass -p redhat ssh  -o  StrictHostKeyChecking=no  -X -l root 192.168.43.163  firefox')\n")
		f.close()
		commands.getstatusoutput("sudo tar -cvf /var/www/html/p.tar /p.py")
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.163/p.tar\">\n"
	elif app == "gnome-terminal" :
		os.system("sudo touch /q.py")
		os.system("sudo chmod 777  /q.py")		
		f=open('/q.py','w')	
		f.write("#!/usr/bin/python2\n")
		f.write("import os\n")
		f.write("os.system('setenforce 0')\n")
		f.write("os.system('iptables -F')\n")
		f.write("os.system('touch /etc/yum.repos.d/client.repo')\n")
		f.write("p=open('/etc/yum.repos.d/client.repo','w')\n")
		f.write("p.write('[client]\\n')\n")
		f.write("p.write('baseurl=ftp://192.168.43.163/pub/yum/Packages/\\n')\n")
		f.write("p.write('gpgcheck=0\\n')\n")
		f.write("p.close()\n")
		f.write("os.system('yum install openssh-clients -y >/dev/null 2>/dev/null')\n")
		f.write("os.system('yum install sshpass -y >/dev/null 2>/dev/null')\n")
		f.write("os.system('sshpass -p redhat ssh  -o  StrictHostKeyChecking=no  -X -l root 192.168.43.163  gnome-terminal')\n")
		f.close()
		commands.getstatusoutput("sudo tar -cvf /var/www/html/q.tar /q.py")
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.163/q.tar\">\n"
	elif app == "wireshark" :
		os.system("sudo touch /r.py")
		os.system("sudo chmod 777  /r.py")		
		f=open('/r.py','w')	
		f.write("#!/usr/bin/python2\n")
		f.write("import os\n")
		f.write("os.system('setenforce 0')\n")
		f.write("os.system('iptables -F')\n")
		f.write("os.system('touch /etc/yum.repos.d/client.repo')\n")
		f.write("p=open('/etc/yum.repos.d/client.repo','w')\n")
		f.write("p.write('[client]\\n')\n")
		f.write("p.write('baseurl=ftp://192.168.43.163/pub/yum/Packages/\\n')\n")
		f.write("p.write('gpgcheck=0\\n')\n")
		f.write("p.close()\n")
		f.write("os.system('yum install openssh-clients -y >/dev/null 2>/dev/null')\n")
		f.write("os.system('yum install sshpass -y >/dev/null 2>/dev/null')\n")
		f.write("os.system('sshpass -p redhat ssh  -o  StrictHostKeyChecking=no  -X -l root 192.168.43.163  wireshark')\n")
		f.close()
		commands.getstatusoutput("sudo tar -cvf /var/www/html/r.tar /r.py")
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.163/r.tar\">\n"

else:
	print "not authorised"












