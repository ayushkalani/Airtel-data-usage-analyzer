#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib,smtplib,re,getpass
try:
	webpage = urllib.urlopen('http://122.160.230.125:8080/planupdate/').read()
	soup = BeautifulSoup(webpage,"lxml")
	airtel=soup.find_all("div",{"class":"description"})
	i=0
	for index in airtel:
		h=index.find_all('span')
		i=i+1
		#1st value is total gb , 2nd value is gbs left , 3rd is no of days , 4th is DSL_number
		if(i==2):
			#convert set into string using repr fucntion
			temp1=re.findall(r'\d+\.\d+',str(h[0]))
			gb = map(float, temp1)
			gb_left=str(gb[0])
		if(i==3):
			temp2=re.findall(r'\d+',str(h[0]))
			dy=map(int,temp2)
			days_left=str(dy[0])

	sender='airtel-internet-usage@gmail.com'
	rec=raw_input('Enter Space Seprated recevier(s) email address:')

	receviers=map(str,rec.split())
	OGmsg='Your remaining Internet balance is :-  '+ gb_left + ' so please use it carefully . Because only ' + days_left+ ' day(s) are left !!!'
	msg = "\r\n".join(["From: airtel-internet-usage@airtel.in","To: DearGuysUseItRealSlow","Subject: Airtel Internet Usage","",OGmsg])
	
	username=raw_input('Your Email (gmail only):')
	password=getpass.getpass('Password:')
	server = smtplib.SMTP('smtp.gmail.com:587')
	try:
		server.starttls()
		server.login(username,password)
		server.sendmail(sender, receviers, msg)
	except Exception:
		print('Send Email failed')
	server.quit()
except IOError:
	print "Net nahi chl rha h bhai , load mat le , airtel ko call kar aur gaali de"


