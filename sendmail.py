import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
nn = 0
sbj = 0
#mail2 = ['mail','mail','mail']
while nn< 500:
 mail = "" #mail 
 fromaddr = ""
 #mail_sttr = mail2.pop(0)
 toaddr = ''#str(mail_sttr)
 mypass = ""#password
 
 msg = MIMEMultipart()
 msg['From'] = fromaddr
 msg['To'] = toaddr
 msg['Subject'] = str(sbj) #subject 
 
 body = random.choice(mail)
 msg.attach(MIMEText(body, 'plain'))
 
 server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
 server.login(fromaddr, mypass)
 text = msg.as_string()
 server.sendmail(fromaddr, toaddr, text)
 server.quit()
 nn += 1
 sbj += 1
 print(nn)








