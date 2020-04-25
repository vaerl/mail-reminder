#!/usr/bin/python

import smtplib
from conf import Conf
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import content

conf = Conf()

SERVER = conf.ConfigSectionMap("mail")["server"]
PORT = conf.ConfigSectionMap("mail")["port"]
SENDER = conf.ConfigSectionMap("mail")["sender"]
PASSWORD = conf.ConfigSectionMap("mail")["password"]
RECIPIENT = conf.ConfigSectionMap("mail")["recipient"]

# TODO add logging to file
# setup
server = smtplib.SMTP(SERVER, PORT)
server.connect(SERVER, PORT)
server.starttls()
server.login(SENDER, PASSWORD)
# message
msg = MIMEMultipart('alternative')
# TODO maybe use %B for full month-name?
msg['Subject'] = "Reminder for " + datetime.date.today().strftime("%b %d, %Y")
msg['From'] = SENDER
msg['To'] = RECIPIENT


# TODO get news -> use RSS-Feeds
results = [content.today(), content.up_next(),
           content.news(), content.status()]


# build message
msg.attach(MIMEText("".join(results), "html"))
# NOTE enabled for debugging
print(msg)
server.sendmail(SENDER, RECIPIENT, msg.as_string())
server.quit()
