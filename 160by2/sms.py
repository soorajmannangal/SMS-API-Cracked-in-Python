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
username = '9037755659'
#password = '9054687'
password='555555'
message = 'Be Happy 3'
number = '9037755659'
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
   url='http://160by2.com/re-login'

  opener.addheaders = [('Referer','Http://160by2.com/')]  
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
  now = datetime.datetime.now() 
  send_sms_url = 'http://160by2.com/SendSMSAction'
  send_sms_data = urlencode({'hid_exists':'no','action1':'sf55sa5655sdf5','mobile1':number,'msg1':message,'sel_month':0,'sel_day':0,'sel_year':0,'sel_hour':'hh','sel_minute':'mm','sel_cat':0,'messid_0':'','messid_1':'','messid_2':'','messid_3':''})
  
  opener.addheaders = [('Referer','http://160by2.com/SendSMS?id=9AEF17EFFA4653F27EEFEC3CA5F4BA30.05')]  
  
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
  print "success login press any key"
  count = 01
  #while (count < 100):
   # count = count + 1  
    #number =str(int(number)+3)
  return_code = sms_send(number, message, opener)
  print number
    
     
  print "Finish"
  b=raw_input()
  



