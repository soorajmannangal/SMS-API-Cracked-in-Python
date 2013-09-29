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

# Default initializations (saves time)
username = '9037223519'
#password = '9054687'
password='SUITHG'
message = 'HAS Warning ---, Motion detected in house'
number = '9037223519'
#tonumber'9846105456'
TOTAL = 260

CONNECTION_ERROR = -1
SUCCESS = 1

def login(username, password, opener):
  '''
  This method takes care of logging onto the website
  '''
  
  
  print message
  #Logging into the SMS Site
  #url = 'http://www.site2sms.com/auth.asp'
  #url = 'http://ultoo.in/login.php'
  url='http://fullonsms.com/login.php'
  #MobileNoLogin=9037223519&LoginPassword=SUITHG&RememberMe=1&x=57&y=11&redirect=
  url_data = urlencode({'MobileNoLogin':username,'LoginPassword':password,'RememberMe':'1','x':'57','y':'11'})
  
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
  #ActionScript=%2Fhome.php&CancelScript=%2Fhome.php&HtmlTemplate=%2Fdisk1%2Fhtml%2Ffullonsms%2FStaticSpamWarning.html&
  #MessageLength=140&MobileNos=9037755659&Message=hello&SelTpl=defaultId&Gender=0&FriendName=Your+Friend+Name&ETemplatesId=&TabValue=contacts
  send_sms_url = 'http://fullonsms.com/home.php'
  send_sms_data = urlencode({'MessageLength':'140','MobileNos':number,'Message': message,'SelTpl': 'defaultId','Gender':'0','FriendName':'Your Friend Name','TabValue':'contacts'})
  
  #POST /quicksms.action HiddenAction=instantsms&catnamedis=Birthday&Action=sa65sdf656fdfd&chkall=on&MobNo=9037755659&textArea=hai+this+is+also+a+test

  opener.addheaders = [('Referer','http://fullonsms.com/home.php?show=contacts')]  
  
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
return_code = login(username, password, opener)

if return_code == CONNECTION_ERROR:
  print "Connection error press any key"
  b=raw_input()
  sys.exit(1)
elif return_code == SUCCESS:
  #print "success login press any key"
  count = 01
  #while (count < 100):
   # count = count + 1  
    #number =str(int(number)+3)
  return_code = sms_send(number, message, opener)
  #print number
    
     
  #print "Finish"
  #b=raw_input()
  



