#!/usr/bin/python
"""
--------------------------------------------------------------------------
Python script to send SMS using services like Way2SMS, FullOnSMS, Site2SMS
--------------------------------------------------------------------------
This script basically simulates a login, just as you would, while sending
the SMS using these websites. But, saves you time by automating stuff, plus
you can do other cool stuff with this script.

DISCLAIMER
The main intention for this script is for educational purposes only.

REFERENCES
http://docs.python.org/library/cookielib.html#examples
http://docs.python.org/library/urllib2.html

"""
import datetime

import cookielib
import urllib2
from getpass import getpass # for unix only, comment this line if using in windows
import sys
from urllib import urlencode
from random import randint
# Default initializations (saves time)
username = '9037755659'
#password = '9054687'
password='7638'
message = 'Be Happy 3'
number = '9037755659'
#tonumber'9846105456'
TOTAL = 260

CONNECTION_ERROR = -1
SUCCESS = 1
print message
def login(username, password, opener):
  '''
  This method takes care of logging onto the website
  '''
  
  
  
  #Logging into the SMS Site
  #url = 'http://www.site2sms.com/auth.asp'
  #url = 'http://ultoo.in/login.php'
  url='http://site4.way2sms.com/w2sauth.action'



  #url_data = urlencode({'txtCCode':'91','userid':username,'Password':password,'Submit':'Login'})
  #url_data = urlencode({'LoginMobile':username,'LoginPassword':password,'RememberMe':'1','submit2':'LOGIN HERE'})
  url_data = urlencode({'username':username,'password':password,'button':'Login'})
  
  # debug message
  # print url_data
  try:
  	usock = opener.open(url, url_data)
  	# debug message
  	# print usock.read()
  except IOError:
  	return CONNECTION_ERROR
  return SUCCESS

def sms_send(number, message, opener):
  # SMS sending
  #Referer: http://ultoo.in/home.php
  
  #send_sms_url = 'http://www.site2sms.com/user/send_sms_next.asp'
  #send_sms_data = urlencode({'txtCategory':'40','txtGroup':'0','txtLeft': len(message) - TOTAL, 'txtMessage': message,'txtMobileNo': number,'txtUsed':len(message)})
  now = datetime.datetime.now() 
  #request# GET http://site4.way2sms.com/generalconfirm.action?SentMessage=Message+has+been+submitted+successfully&Mnumber=9037755659&Mmess=hai&Token=27D32D241C5D41D5545CE1CD238DC67B.w808
#request# POST http://site4.way2sms.com/jsp/snd2sms.action

  #send_sms_url = 'http://site4.way2sms.com/quicksms.action'
  send_sms_url = 'http://site4.way2sms.com/jsp/snd2sms.action'
  #POST /jsp/snd2sms.action t_15_k_5=xAgBnf&i_m=sndsms&m_15_b=SutQfbcK&kriya=sa65sdf656fdfd&xNMgELX=&xAgBnf=27D32D241C5D41D5545CE1CD238DC67B.w808&catnamedis=Birthday&chkall=on&diffNo=14%3A56%3A12&SutQfbcK=9037755659&txtLen=130&textArea=hai+sooraj

  send_sms_data = urlencode({'t_15_k_5':'xAgBnf','i_m':'sndsms','m_15_b': 'SutQfbcK','kriya': 'sa65sdf656fdfd','catnamedis':'Birthday','chkall':'on','diffNo':'14%3A56%3A12','SutQfbcK':number,'txtLen':'130','textArea':message})
  
  #POST /quicksms.action HiddenAction=instantsms&catnamedis=Birthday&Action=sa65sdf656fdfd&chkall=on&MobNo=9037755659&textArea=hai+this+is+also+a+test
  
  opener.addheaders = [('Referer','http://site4.way2sms.com/jsp/snd2sms.action')]  
  
  try:
  	sms_sent_page = opener.open(send_sms_url,send_sms_data)
  except IOError:
  	return CONNECTION_ERROR
  return SUCCESS
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# To fool the website as if a Web browser is visiting the site
opener.addheaders = [('User-Agent','Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:8.0) Gecko/20100101 Firefox/8.0')]

# Send the SMS
f = open ("The Thirty-Nine Steps [John Buchan].txt","r")
data = f.read()
count = 1
rep = 1
start =1
end = randint(10,60)
while (end < len(data)-50):
  return_code = login(username, password, opener)
  if return_code == CONNECTION_ERROR:  
    print "\nConnection error\n"
  elif return_code == SUCCESS:
    print "\nsuccess login\n"
    return_code = sms_send("9495549708","hai",opener)    
    print "\n"+str(count)+"  "+ data[start:end] + "\n"
  start = end
  end =end+randint(10,60)
  count = count + 1
f.close()
b=raw_input()
  



