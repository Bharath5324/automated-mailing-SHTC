import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

EMAIL_ADDRESS = 'bharath.s@ieee.org'
EMAIL_PASSWORD = 'xxxxxxxxxx'
contacts = ["amitony@ieee.org", "rosiajohny04@gmail.com", "aednakurian6451@gmail.com"]
try:
  text = open('./mail.html', 'r')
except FileNotFoundError:
  print("Please insert the required files(mail.html)")
  exit()
html = text.read()
subject = 'SHTC Test Mail'
msg = MIMEMultipart()
msg['From'] = EMAIL_ADDRESS
msg['Subject'] = "Invitation to Students Humanitarian Technology Conference"
msg.preamble = 'Multipart massage.\n'
part2=MIMEText(html,'html')
msg.attach(part2)
attachment = open('./invite.ics')
part = MIMEBase('text/calendar',' ;name="%s"'%"invite.ics") 
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= invite.ics")
msg.attach(part)
text = msg.as_string()
with smtplib.SMTP_SSL('mail.google.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.sendmail(EMAIL_ADDRESS, contacts, text)
    print ("Email Sent!!")
del attachment
print('deleted')
