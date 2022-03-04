# Imported needed libraries
import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace the following with your SMTP server and Port
smtp_server = "smtp-relay.gmail.com"
port = 25  # Update port if using secured connection
server = smtplib.SMTP(smtp_server, port)

# Start the service
server.ehlo()

# For secure connection uncomment the following:
# context = ssl.create_default_context()
# server.starttls(context=context)

# Log into the server
account_email = input("Enter your email: ")
account_password = input("Enter your password: ")
server.login(account_email, account_password)

# Restart the service
server.ehlo()

# Compose Email
senders_email = "myemail@mydomain.com"
recipient_email = "test@test.com"

# The Subject below is needed so the first line gets registred as Email Subject
email_body = """\
Subject: Test Email from Python

This message is sent from Python.
It works!"""

# Sending the email
server.sendmail(senders_email, recipient_email, email_body)
