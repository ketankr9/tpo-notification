#!/usr/bin/python
import pickle
import time
import dryscrape
import math
import sys
from way2sms import sendSMS
from bs4 import BeautifulSoup as bs
######################################################################
# fill all the required details below
# username for tpo portal
usr_tpo=""
# password for tpo portal login
pass_tpo=""
# your way2sms account registered phonenumber				
usr_sms=""
# your way2sms account password			
pass_sms=""
# a number on which you wish to receive SMS notification(NON DoNotDisturb)			 
notify_via=""  		
usr_proxy="068.1507xxxx"		# proxy username
pass_proxy="12345678"			# proxy password
proxy_server="10.1.1.45"		# proxy server e.g.,"10.1.1.45"
######################################################################
if 'linux' in sys.platform:
    dryscrape.start_xvfb()

sess = dryscrape.Session(base_url = 'https://www.placement.iitbhu.ac.in')
#uncomment below line if you are directly connected to internet or behind vpn 
sess.set_proxy(proxy_server,"80",usr_proxy,pass_proxy)
sess.set_attribute('auto_load_images', False)
first_time=True
while first_time:
	print "Signing in :)"
	try:
		sess.visit('/accounts/login/')
		login_box=sess.at_xpath('//input[@id="id_login"]')
		login_box.set(usr_tpo)
		pass_box=sess.at_xpath('//input[@id="id_password"]')
		pass_box.set(pass_tpo)
		pass_box.form().submit()
		first_time=False
	except:
		print "Failed login :("
		time.sleep(6)

def getHtml():		
	sess.visit('/company/calendar?page_size=250')
 	time.sleep(2)
	sess.render('companies.png')
	data=sess.driver.body()
	return data
	
count=0


while True:
	count+=1
	print "Attempt:",count
	try:
 		data=getHtml()
 		if data==None:
 			continue
	except:
		time.sleep(5)
		continue
	soup=bs(data,'html.parser')
	companies=soup.findAll('div',{"class":"row company"})
	try:
		com_list_old=pickle.load(open('com_list.p','rb'))
	except:
		pickle.dump(['x','y','z','a'],open('com_list.p','wb'))
		com_list_old=pickle.load(open('com_list.p','rb'))

	com_list,added_com=[],[]

	for i in xrange(len(companies)):
		ci=companies[i].find('div',{"class":"col-md-2 col-sm-6 col-xs-12"}).find('p',{"class":"company_name"}).string.encode('utf-8')
		com_list.append(ci)
		com_list.sort()

	#############################  for testing #########################################
	#uncomment at least a single line from below to test if the script is working or not
	# com_list_old.pop(0)
	# com_list_old.pop()
	# com_list_old.pop()
		
	flag=False
	for x in com_list:
		if x not in com_list_old:
			added_com.append(x)
			flag=True
			# print x
	pickle.dump(com_list,open('com_list.p','wb'))
	if len(added_com)==0:
		print "No new company added :("
	if flag==True:
		message="+"
		message+=":".join(added_com)
		for i in xrange(int(math.ceil(len(message)*1.0/140))):
			attempt_sms=0
			while sendSMS(notify_via,message[i*140:(i+1)*140],usr_sms,pass_sms)==False and attempt_sms < 10:
				print "Message sending failed:",attempt_sms
				attempt_sms+=1
	#recheck for company updates every 600 seconds
	time.sleep(600)