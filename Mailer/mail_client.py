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
email_subject = "Email from Python"
email_body = """\
Hi,
This is a test email from Python.
It Works!"""

msg = MIMEMultipart()
msg["From"] = senders_email
msg["To"] = recipient_email
msg["Subject"] = email_subject
msg.attach(MIMEText(email_body, "plain"))

# adding an attachment
filename = "document.pdf"  # If not in the same directory use full path to file
attachment = open(filename, "rb")

# Open file then encode so it can be sent by email
part = MIMEBase("application", "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)

# Adding header to attachment part
part.add_header(
  "Content-Disposition",
  f"attachment; filename= {filename}",
)

# Attaching to message & converting to string type
msg.attach(part)
text = msg.as_string()

# Sending the email
server.sendmail(senders_email, recipient_email, text)
