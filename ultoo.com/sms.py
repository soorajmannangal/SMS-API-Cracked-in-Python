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

import cookielib
import urllib2
from getpass import getpass # for unix only, comment this line if using in windows
import sys
from urllib import urlencode
import datetime

# Default initializations (saves time)
username = '9037755659'
#password = '9054687'
password='47951'
message = 'hello iam in busy'
number = '9037755659'
#tonumber'9846105456'

CONNECTION_ERROR = -1
SUCCESS = 1

def login(username, password, opener):
 
  print message
  #Logging into the SMS Site
  url = 'http://ultoo.in/login.php'
  url_data = urlencode({'LoginMobile':username,'LoginPassword':password,'RememberMe':'1','submit2':'LOGIN HERE'})
  try:
  	usock = opener.open(url, url_data)
  except IOError:
  	return CONNECTION_ERROR
  return SUCCESS

def sms_send(number, message, opener):
  # SMS sending
  now = datetime.datetime.now()
  print now.day
  print now.year
  print now.month
  day=now.day
  day2=str(day)
  if len(day2) == 1 :
    day2='0'+str(day)
  mon=now.month
  mon2=str(mon)
  if len(mon2) == 1 :
    mon2='0'+str(mon)   
  send_sms_url = 'http://ultoo.in/home.php'
  send_sms_data = urlencode({'MessageLength':'140','MobileNos':number,'Message': message,'SendNow': 'Send Now','SendNowBtn':'Send Now','Day':day2,'Month':mon2,'Year':now.year,'TimeInterval':'09:00 - 09:59','CCode':''})
  
  opener.addheaders = [('Referer','http://ultoo.com/home.php')]  
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
  sys.exit(1)
elif return_code == SUCCESS:
  print "success login"
  
  return_code = sms_send(number, message, opener)
  print "message sent"
  b=raw_input()



