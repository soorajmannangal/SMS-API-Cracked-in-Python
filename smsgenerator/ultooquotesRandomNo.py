#ULtoo randsms generator send upto 50 sms
import time
import pyPdf
import cookielib
import urllib2
from getpass import getpass # for unix only, comment this line if using in windows
import sys
import re
from urllib import urlencode
import datetime
from random import randint
username = '9037755659'
password='47951'
message = None
number = None
CONNECTION_ERROR = -1
SUCCESS = 1

def login(username, password, opener):
 
  
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
print "Enter first 6 digit of a mobile no : "
mob = raw_input()
if len(mob) != 6 :
  print "Not a six digit number"
  sys.exit(1)
print "Enter no of messages to send : "
nomsg=int(raw_input())
nomsg = nomsg +1
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent','Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:8.0) Gecko/20100101 Firefox/8.0')]
f = open ("The Thirty-Nine Steps [John Buchan].txt","r")
data = f.read()
rep = 1
start =1
end = randint(10,60)
op = urllib2.build_opener()
url='http://www.goodreads.com/quotes/tag/'		  
l=[]
l.append(url)
l.append('wish')
url=''.join(l)
intake=op.open(url)
page=intake.read()
line=page.split('\n')
new=set([])
count = 0
for i in range (len(line)) :
  if count == nomsg :
    break;
  mat1=re.match(r'.*dquo;(.*?)&rdquo.*',line[i])
  if mat1 :
    str0= mat1.group(1)
    str2 = str0.replace("<br />","  ")
    new.add(mat1.group(1))
    i = i +2
    mat2 = re.match(r'.*">(.*?)<.*',line[i])
    str3="hai"
    if mat2 :
      str3= mat2.group(1)
      if str3 != "hai": 
	#print str2+",by :"+str3
	return_code = login(username, password, opener)
	if return_code == CONNECTION_ERROR:  
	  print "\nConnection error\n"
	elif return_code == SUCCESS:
	  print "\nsuccess login\n"
	  return_code = sms_send(mob+str(randint(1500,9999)),str2+",by :"+str3,opener)
	  count = count +1
	  print str(count)+" : "+ str2+",by :"+str3 + ":\t"+mob+str(randint(1500,9999))
  i = i+1
print "\nSMS Sending finished  Count="+str(count)
b=raw_input()



