#!/usr/bin/python2
print "content-type:text/html"
print 

 

def port():
	return b	

import os,cgi,commands,cgitb,random
cgitb.enable()
content=cgi.FormContent()
os.system("sudo iptables -F")
os.system("sudo setenforce 0")
cpu=str(content['cpu'][0])
ram=str(content['ram'][0])
u=str(content['iaas_user'][0])
p=str(content['iaas_pass'][0])
name=str(content['name'][0])
os=str(content['os'][0])
a=str(random.randint(5900,6900))
b=str(random.randint(4000,5000))
q=commands.getstatusoutput("cat /port.txt|grep "+name+"|cut -d':' -f1|cut -d'_' -f2")
commands.getstatusoutput("qrencode -s 16 -o /var/www/html/qrencode/"+u+"_"+name+".png http://192.168.43.163/?port="+b)
print q

if name==q[1]:
	print "choose another name"
else: 
		f=open("/port.txt","a")
		f.write(u+"_"+name+":"+a+":"+b+"\n")
		f.close()
		z=commands.getstatusoutput("cat /port.txt|grep "+u+"|wc -l")
		commands.getstatusoutput("sudo qemu-img create -f qcow2 /iaas/{}_{}.qcow2 10G".format(u,name))
		commands.getstatusou0.tput("sudo virt-install --name "+u+"_"+name+" --memory "+ram+" --vcpus "+cpu+" --os-type linux --os-variant 		rhel7 --hvm --graphics vnc,port="+a+",listen=0.0.0.0  --disk /iaas/"+u+"_"+name+".qcow2 --cdrom /root/Desktop/rhel7.iso 		--noautoconsole")
		commands.getstatusoutput("/var/www/cgi-bin/websockify/run -D 192.168.43.163:{} 192.168.43.163:{}".format(b,a))
		print '''
			<style>
			iframe 
			{
			position:relative;
			margin:1%;
			width:20%;
			height:20%;
			}
			</style>
			<html>
			</form>
			</div>'''

		h=commands.getstatusoutput("cat /port.txt |grep "+u+" |cut -d':' -f3")
		print a,b
		aqw=h[1].split("\n")
		print "<center><h1>operating system gallery</h1></center>"
		for i in aqw:
			mybut=commands.getstatusoutput("cat /port.txt|grep "+i+"|cut -d':' -f1")
			print '''
				
				<div class="div"><a href="http://192.168.43.163?host=192.168.43.163&port='''+i+'''" target="_blank" >'''+mybut[1]+'''</a><div class="hover"><img src="http://192.168.43.163/qrencode/'''+u+'''_'''+name+'''.png"></img></div>
				</div>	
				




					


			<style>
			
					.div
					{
					background:url("/img/dot.jpg");
					display:inline-block;
					height:100px;
					width:400px;
					margin:10px;
					padding:0px;
					padding-top:75px;
					
					box-shadow:5px 5px 5px 2px	
					}
					
					a
					{
					font-size:40px;
					text-decoration:none;
					margin:25px;
					color:teal;
					}
	
					div:hover
					{
						
					box-shadow:5px 5px 5px 5px;
					}
					
					
					
					img
					{
					    	width:20px;
						height:20px;
						z-index:2;				
					}
						
					img:hover
					{
					    	width:200px;
						height:200px;
						z-index:2;				
					}

					
					</style>
			</style>'''
