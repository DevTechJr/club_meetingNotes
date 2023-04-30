import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Load the email addresses from the JSON file
with open('records.json', 'r') as f:
    emails = json.load(f)['emails']

# Read the message from the text file
with open('message.txt', 'r') as f:
    message = f.read()

# Create the email subject with the current date
today = datetime.today().strftime('%Y-%m-%d')
subject = f"HSS Meeting Notes - {today}"

# Set up the email message
msg = MIMEMultipart()
msg['From'] = 'vangara.anirudhbharadwaj@gmail.com'
msg['To'] = ', '.join(emails)
msg['Subject'] = subject
msg.attach(MIMEText(message))

# Set up the email server and send the message
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('vangara.anirudhbharadwaj@gmail.com', 'password-here')
server.sendmail(msg['From'], emails, msg.as_string())
server.quit()