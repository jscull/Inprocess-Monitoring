import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import textwrap
from O365 import Message

def AutomateEmail(ra,n,bn,dr,exception,msl,mel,extra,et):
	toaddr = str(ra)

	body = """\
	Hi %s,

	Build %s has been completed and the images have been processed. 
	The images and timelapses can be found at: %s.
	"""%(n,bn,dr)
	if exception:
		body += """
	Please note, there are missing layers from the recording.
	Layers missing are pictures: %s through %s. Sorry for any trouble this may cause.		
	"""%(msl,mel)
	if extra:
		body += """
	%s
	"""%et
	body += """
	From Joseph Scull

	(This was sent via a script (Do not reply). If there are any issues with this please speak to me or drop me an email on joescull@hieta.biz)
	"""
	
	body = textwrap.dedent(body)
	auth = ('mechanic@hieta.biz','Plank65(dons')
	m = Message(auth=auth)
	m.setRecipients(toaddr)
	m.setSubject('Build %s Processed'%bn)
	m.setBody(body)
	m.sendMessage()

if __name__=='__main__':
	AutomateEmail(ra="joescull@hieta.biz",n="Joe",bn=101,dr="C:/",exception="False",msl=None,mel=None,extra=False,et="")

	###### 	CODE FOR SENDING EMAIL VIA GMAIL / OUTLOOK #######
	#	#fromaddr = 'joe.master.embot@gmail.com'			 #
	#	fromaddr = 'mechanic@hieta.biz'						 #
	#	toaddr = str(ra)									 #
	#	msg = MIMEMultipart()								 #
	#	msg['From'] = fromaddr								 #
	#	msg['To'] = toaddr									 #
	#	msg['Subject'] = "Build Processed"					 #
	#														 #
	#	#msg.attach(MIMEText(body,'plain'))					 #
	#	server = smtplib.SMTP('smtp.gmail.com', 587)         #
	#	server = smtplib.SMTP('smtp-mail.outlook.com', 587)  #
	#	server = smtplib.SMTP('outlook.office365.com')       #
	#	server.starttls()									 #
	#	server.login(fromaddr,'Botpasswordplsdonthack') #
	#	server.login(fromaddr,'pass')				         #
	#	text = msg.as_string()								 #
	#	server.sendmail(fromaddr,toaddr,text)			 	 #
	#	server.quit()										 #
	##########################################################
	
	
