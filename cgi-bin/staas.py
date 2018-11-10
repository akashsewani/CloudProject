#!/usr/bin/python2
print "content-type:text/html\n"
print ""

import cgi,cgitb,commands
cgitb.enable()
content=cgi.FieldStorage()
vg="staas"
u=content.getvalue('staas_user')
p=content.getvalue('staas_pass')
r=content.getvalue('r')
ro=content.getvalue('ro')
print u

s=content.getvalue('size')
commands.getstatusoutput("sudo iptables -F")
commands.getstatusoutput("sudo setenforce 0")
if r=='object':
		if ro=='non-encrypted':
			commands.getstatusoutput("sudo lvcreate --name "+u+"_lv --size "+s+" "+vg)
			commands.getstatusoutput("sudo mkfs.ext2 /dev/"+vg+"/"+u+"_lv >/dev/null 2>/dev/null")
			commands.getstatusoutput("sudo mkdir /home/"+u+"/directory")
			commands.getstatusoutput("sudo mount /dev/"+vg+"/"+u+"_lv /home/"+u+"/directory")
			commands.getstatusoutput("sudo yum install nfs-utils -y >/dev/null 2>/dev/null")		
			z=commands.getstatusoutput("cat /etc/exports|grep "+u)
			if u in z[1]:
				print "STORAGE ALREADY EXISTS!!!!!!!"
			else:
				f=open("/etc/exports","a")
				f.write("/home/"+u+"/directory *(rw,no_root_squash)\n")
				f.close()
				commands.getstatusoutput("sudo exportfs -r")
				commands.getstatusoutput("sudo systemctl restart nfs-server >/dev/null 2>/dev/null")
				commands.getstatusoutput("sudo touch /staas_nenc_"+u+".py")
				commands.getstatusoutput("sudo chmod 777  /staas_nenc_"+u+".py")	
				f=open('/staas_nenc_'+u+'.py','w')	
				f.write("#!/usr/bin/python2\n")
				f.write("import commands\n")
				f.write("commands.getstatusoutput('setenforce 0')\n")
				f.write("commands.getstatusoutput('iptables -F')\n")
				f.write("commands.getstatusoutput('sudo yum install nfs-utils -y >/dev/null 2>/dev/null')\n")
				f.write('''commands.getstatusoutput("sudo mkdir /media/'''+u+'''")\n''')
				f.write('''commands.getstatusoutput("sudo mount 192.168.43.163:/home/'''+u+'''/directory /media/'''+u+'''")\n''')
				f.close()
				commands.getstatusoutput("sudo tar -cvf /var/www/html/staas_nenc_"+u+".tar /staas_nenc_"+u+".py")
				print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.163/staas_nenc_"+u+".tar\">\n"
		elif ro=='encrypted':
			commands.getstatusoutput("sudo lvcreate --name "+u+"_lv1 --size "+s+" "+vg)
			commands.getstatusoutput("sudo mkfs.ext2 /dev/"+vg+"/"+u+"_lv1 >/dev/null 2>/dev/null")
			commands.getstatusoutput("sudo mkdir /home/"+u+"/directory1")
			print commands.getstatusoutput("sudo mount /dev/"+vg+"/"+u+"_lv1 /home/"+u+"/directory1")
			commands.getstatusoutput("sudo yum install openssh-server -y >/dev/null 2>/dev/null")
			commands.getstatusoutput("sudo chown "+u+" /home/"+u+"/directory1")
			commands.getstatusoutput("sudo chmod 777 /home/"+u+"/directory1")
			commands.getstatusoutput("sudo systemctl restart sshd >/dev/null 2>/dev/null")
			commands.getstatusoutput("sudo touch /staas_enc_"+u+".py")
			commands.getstatusoutput("sudo chmod 777  /staas_enc_"+u+".py")	
			f=open('/staas_enc_'+u+'.py','w')	
			f.write("#!/usr/bin/python2\n")
			f.write("import commands\n")
			f.write("commands.getstatusoutput('setenforce 0')\n")
			f.write("commands.getstatusoutput('iptables -F')\n")
			f.write("commands.getstatusoutput('touch /etc/yum.repos.d/client.repo')\n")
			f.write("p=open('/etc/yum.repos.d/client.repo','w')\n")
			f.write("p.write('[client]\\n')\n")
			f.write("p.write('baseurl=ftp://192.168.43.163/pub/yum/Packages/\\n')\n")
			f.write("p.write('gpgcheck=0\\n')\n")
			f.write("p.close()\n")
			f.write("commands.getstatusoutput('sudo yum install fuse-sshfs -y >/dev/null 2>/dev/null')\n")
			f.write('''commands.getstatusoutput("sudo mkdir /media/'''+u+'''_enc")\n''')
			f.write('''commands.getstatusoutput("echo redhat | sudo sshfs 192.168.43.163:/home/'''+u+'''/directory1 /media/'''+u+'''_enc --stdin")\n''')
			f.close()
			commands.getstatusoutput("sudo tar -cvf /var/www/html/staas_enc_"+u+".tar /staas_enc_"+u+".py")
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.163/staas_enc_"+u+".tar\">\n"	
elif r=='block':
		commands.getstatusoutput("sudo lvcreate --name "+u+"_lv2 --size "+s+" "+vg)
		commands.getstatusoutput("sudo yum install scsi-target-utils -y >/dev/null 2>/dev/null")
		commands.getstatusoutput("sudo touch /etc/tgt/conf.d/"+u+".conf")
		commands.getstatusoutput("sudo chmod 777 /etc/tgt/conf.d/"+u+".conf")
		f=open("/etc/tgt/conf.d/"+u+".conf","a")
		f.write("\n<target "+u+"_target>\nbacking-store /dev/"+vg+"/"+u+"_lv2 \n</target>\n")
		f.close()
		commands.getstatusoutput("sudo touch /block"+u+".py")
		commands.getstatusoutput("sudo chmod 777  /block"+u+".py")		
		f=open('/block'+u+'.py','w')	
		f.write("#!/usr/bin/python2\n")
		f.write("import commands\n")
		f.write("commands.getstatusoutput('setenforce 0')\n")
		f.write("commands.getstatusoutput('iptables -F')\n")
		f.write("commands.getstatusoutput('touch /etc/yum.repos.d/client.repo')\n")
		f.write("p=open('/etc/yum.repos.d/client.repo','w')\n")
		f.write("p.write('[client]\\n')\n")
		f.write("p.write('baseurl=ftp://192.168.43.163/pub/yum/Packages/\\n')\n")
		f.write("p.write('gpgcheck=0\\n')\n")
		f.write("p.close()\n")
		f.write("commands.getstatusoutput('yum install iscsi-initiator-utils.i686 -y >/dev/null 2>/dev/null')\n")
		f.write("commands.getstatusoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.43.163 --discover')\n")
		f.write("commands.getstatusoutput(' iscsiadm --mode node --targetname "+u+"_target --portal 192.168.43.163:3260 --login  >/dev/null 2>/dev/null')\n")
		f.close()
		commands.getstatusoutput("sudo tar -cvf /var/www/html/block"+u+".tar /block"+u+".py")
		commands.getstatusoutput("sudo systemctl  restart tgtd  >/dev/null 2>/dev/null")		
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.163/block"+u+".tar\">\n"
		

		


		
		
			


