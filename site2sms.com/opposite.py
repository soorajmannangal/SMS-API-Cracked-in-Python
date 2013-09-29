from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import urllib2
import re
import sets
import sys
import cookielib
from urllib import urlencode
import cgi
import urllib
import wsgiref.handlers
from google.appengine.ext import db
from google.appengine.api import users

class Contacts(db.Model):
  """Models an individual Guestbook entry with an author, content, and date."""
  name = db.StringProperty()   #name of user
  userid = db.StringProperty()  #mobile number of user
  password = db.StringProperty() #password of site2sms
  code = db.StringProperty()  #table id 

def guestbook_key(guestbook_name):
  """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
  return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

class MainPage(webapp.RequestHandler): 
      def get(self):
	    usrname=None
	    userid = None
	    password = None
	    msg = None
	    tonumber = None
	    TOTAL = 260
	    self.response.headers['Content-Type'] = 'text/html'
	    
	    message=self.request.get_all('message')
	    self.response.out.write("<html><body>") 
	    
	    if message is None:
	      sys.exit(1)
		    
	    data=[]
	    data=message[-1].split(None,1)
	    if data[0] == 'send' and len(data)==2:
	      
		  self.response.out.write("Received" )
		  
		  smsdata=data[1].split('>',3)
		  operation=smsdata[0]
		  if operation == 's' or operation == 't' or operation == 'v' or operation == 'u':   #send sms
		    
			tonumber=smsdata[1]
			if operation == 't':
			  tonumber='9'+smsdata[1]
			if operation == 'u':
			  tonumber='8'+smsdata[1]
			if operation == 'v':
			  tonumber='7'+smsdata[1]			
			
			
			code=smsdata[2]
			#msg=smsdata[3]
			#self.response.out.write("code " +str(code) + str(len(data))) 
			    #would get login name and password from data base based on code
			rslt = db.GqlQuery("SELECT * FROM Contacts WHERE ANCESTOR IS :1 AND code =:2",
							guestbook_key('ContactTable'),code).get()			    
			if rslt is not None:
			  password=rslt.password
			  userid=rslt.userid
			  usrname=rslt.name
			else:
			  sys.exit(1)
			  #self.response.out.write("usr not registerd") 
			my_text=smsdata[3]
			my_text = my_text.replace('_', ' ')
			
			msg='('+ usrname +') '+ my_text
			  
			#self.response.out.write("userid " +str(usrname)) 	    			    
			#password='9054687'
			#userid='9037755659'
			cj = cookielib.CookieJar()
			opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
			opener.addheaders = [('User-Agent','Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:8.0) Gecko/20100101 Firefox/8.0')]
			url = 'http://www.site2sms.com/auth.asp'
			url_data = urlencode({'txtCCode':'91','userid':userid,'Password':password,'Submit':'Login'})	    	    
			usock = opener.open(url, url_data)
			send_sms_url = 'http://www.site2sms.com/user/send_sms_next.asp'
			send_sms_data = urlencode({'txtCategory':'40','txtGroup':'0','txtLeft': len(msg) - TOTAL,'txtMessage': msg, 'txtMobileNo': tonumber,'txtUsed':len(msg)})      
			opener.addheaders = [('Referer','http://www.site2sms.com/user/send_sms.asp')]  
			sms_sent_page = opener.open(send_sms_url,send_sms_data)	
			
		  elif operation == 'r':  #register user
			uname=smsdata[1]
			unumber=smsdata[2]
			upassword=smsdata[3]
			deleteContact = db.GqlQuery("SELECT * FROM Contacts WHERE ANCESTOR IS :1 AND userid =:2", guestbook_key('ContactTable'),unumber) 
			#deleteContact = db.GqlQuery("SELECT * FROM Contacts WHERE ANCESTOR IS :1", guestbook_key('ContactTable')) 
			if deleteContact is not None:
			  db.delete(deleteContact)
			#cd = db.GqlQuery("SELECT code FROM Contacts WHERE ANCESTOR IS :1 ORDER BY code DESC", guestbook_key('ContactTable')).get() 
			cd = db.GqlQuery("SELECT * FROM Contacts WHERE ANCESTOR IS :1 ", guestbook_key('ContactTable')).get() 
			
									
			id=[]
			if cd is None:
			  id='aa'
			else:
			  id=cd.code
			a=id[0]
			b=id[1]
			if id !='zz':
			    if b != 'z':
			      b=chr(ord(b)+1)
			    else:
			      b='a'
			      a=chr(ord(a)+1)
			    code=a+b
			    guestbook_name ='ContactTable'
			    greetings2 = Contacts(parent=guestbook_key('ContactTable'))			
			    greetings2.name = uname
			    greetings2.userid=unumber
			    greetings2.password=upassword
			    greetings2.code=code
			    greetings2.put()	
			    msg="Application activated    |Activation code|"+a+b+"|"
			    cj = cookielib.CookieJar()
			    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
			    opener.addheaders = [('User-Agent','Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:8.0) Gecko/20100101 Firefox/8.0')]
			    url = 'http://www.site2sms.com/auth.asp'
			    url_data = urlencode({'txtCCode':'91','userid':unumber,'Password':upassword,'Submit':'Login'})	    	    
			    usock = opener.open(url, url_data)
			    send_sms_url = 'http://www.site2sms.com/user/send_sms_next.asp'
			    send_sms_data = urlencode({'txtCategory':'40','txtGroup':'0','txtLeft': len(msg) - TOTAL,'txtMessage': msg, 'txtMobileNo': unumber,'txtUsed':len(msg)})      
			    opener.addheaders = [('Referer','http://www.site2sms.com/user/send_sms.asp')]  
			    sms_sent_page = opener.open(send_sms_url,send_sms_data)
			    #send to me
			    cd2 = db.GqlQuery("SELECT * FROM Contacts WHERE ANCESTOR IS :1 AND userid =:2", guestbook_key('ContactTable'),'9037755659').get() 
			    password=cd2.password
			    #password='9054687'
			    msg="New user Registerd         "+"Name : "+uname+"         "+"    No : "+unumber
			    opener.addheaders = [('User-Agent','Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:8.0) Gecko/20100101 Firefox/8.0')]
			    url = 'http://www.site2sms.com/auth.asp'
			    url_data = urlencode({'txtCCode':'91','userid':'9037755659','Password':password,'Submit':'Login'})	    	    
			    usock = opener.open(url, url_data)
			    send_sms_url = 'http://www.site2sms.com/user/send_sms_next.asp'
			    send_sms_data = urlencode({'txtCategory':'40','txtGroup':'0','txtLeft': len(msg) - TOTAL,'txtMessage': msg, 'txtMobileNo': '9037755659','txtUsed':len(msg)})      
			    opener.addheaders = [('Referer','http://www.site2sms.com/user/send_sms.asp')]  
			    sms_sent_page = opener.open(send_sms_url,send_sms_data)			   			    
			    
			else:
			    msg="Registration Closed"
			    cj = cookielib.CookieJar()
			    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
			    opener.addheaders = [('User-Agent','Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:8.0) Gecko/20100101 Firefox/8.0')]
			    url = 'http://www.site2sms.com/auth.asp'
			    url_data = urlencode({'txtCCode':'91','userid':number,'Password':password,'Submit':'Login'})	    	    
			    usock = opener.open(url, url_data)
			    send_sms_url = 'http://www.site2sms.com/user/send_sms_next.asp'
			    send_sms_data = urlencode({'txtCategory':'40','txtGroup':'0','txtLeft': len(msg) - TOTAL,'txtMessage': msg, 'txtMobileNo': number,'txtUsed':len(msg)})      
			    opener.addheaders = [('Referer','http://www.site2sms.com/user/send_sms.asp')]  
			    sms_sent_page = opener.open(send_sms_url,send_sms_data)		  
	
						
		  
	    else:
		  op = urllib2.build_opener()
		  url='http://thesaurus.com/browse/'		  
		  #self.response.out.write("<html><body>")
		  l=[]
		  l.append(url)
		  l.append(data[0])
		  url=''.join(l)
		  intake=op.open(url)
		  page=intake.read()
		  line=page.split('\n')
		  new=set([])
		  for i in range (len(line)) :
			mat1=re.match(r'.*Antonyms:.*',line[i],re.M)
			if mat1:
			      i=i+2
			      self.response.out.write(" <br/> " + "Opposite of " + data[0] + " : ")
			      while 1 :
				    mat2=re.match(r'</span></td>',line[i])
				    if mat2 :
					  break
				    mat2=re.match(r'.*>(.*?)<.*>(.*?)',line[i])
				    mat3=re.match(r'(.*)<.*>(.*?)<.*',line[i])
				    if mat2:
					  new.add(mat2.group(1))
					  new.add(mat2.group(2))
				    if mat3:
					  new.add(mat3.group(1))
					  new.add(mat3.group(2))
				    i=i+1            			
			      break
		  for i in new:  
			self.response.out.write(i)
	    self.response.out.write("</body></html>")
	    
	    	    
application = webapp.WSGIApplication(
    [('/', MainPage)],
    debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
	main()		                       
                        
