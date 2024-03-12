<h2>Description</h2>
This repository serves as documentation for me setting up email automation using Python, specifically focusing on connecting Python to Gmail's SMTP server. The process involves configuring two-factor authentication (2FA) for added security and generating an app-specific password to authenticate Python with Gmail.
</br>
- The primary objective of this project is to explore email automation techniques via scripting, and then explore the security implications associated with email communication, and then finding out how they are used as an attack vector. 
</br>
- It includes the implementation of a cybersecurity attack. For this case, Ive included a modified code that can simulate an Email Bombing attack.

<h2>Languages Used</h2>

- Python

<h2>Utilities Used</h2>

- Visual Studio Code Codespaces


---

<h2>Steps Taken</h2>

# First, Setting Up Two-Factor Authentication for Gmail
youll need to set this up since app passwords need 2FA enabled to acess it.

</br>
   
1. **Visit Google Account Settings**: Begin by accessing your Google account settings through [myaccount.google.com](https://myaccount.google.com).
   
2. **Access Security Settings**: Navigate to the "Security" tab within your Google account settings.
   
3. **Enable 2-Step Verification**: Scroll down to locate the option for "2-Step Verification" and enable it for enhanced security.

   
4. **Initiate Setup**: Follow the on-screen prompts to initiate the setup process for 2FA.
<p align="center">
<img src="https://iili.io/JVmRc0P.png" height="85%" width="85%" alt="Google 2-Step Verification Setup"/>
</p>
   
5. **Login Authentication**: Re-enter your account password for authentication purposes.

6. **Provide Verification Method**: Choose your preferred method for receiving verification codes, either via phone number or the Google Authenticator app.
   
   - **Using Phone Number**:
     - Enter your phone number and proceed as instructed.
     - Verify your phone number by entering the received verification code.

   - **Using the Google Authenticator App**:
     - Download and install the Google Authenticator app from your device's app store.
     - Scan the QR code displayed on-screen with the app.
     - Enter the generated verification code into the designated field.

7. **Turn on 2-Step Verification**: Once the verification method is selected and verified, proceed to turn on 2FA.
   
8. **Verification Confirmation**: Confirm the successful activation of 2FA through the displayed confirmation message.

9. **Final Confirmation**: Ensure that 2FA is indeed enabled by verifying the status in your Google account settings.

</br>

# Next, Generating App-Specific Password for Python

After completing the setup for two-factor authentication (2FA), you'll need to generate an app-specific password to allow Python to connect to Gmail's SMTP server securely. Follow these steps to generate the app-specific password:

1. **Access Google Account Settings**: Navigate to [myaccount.google.com](https://myaccount.google.com) using your web browser.

2. **Access Security Settings**: In the sidebar, find and click on "Security" to access your Google account's security settings.

3. **Enable Two-Factor Authentication (2FA)**: Then you can scroll down and find "2-Step Verification" in the "How you sign in to Google" section, and click on it. You'll likely be prompted to re-enter your email password for authentication.
   - Note: If you havent enabled it, go back up and read up on how to set up 2FA. 
<p align="center">
<img src="https://iili.io/JVmE4Qn.png" height="85%" width="85%" alt="Google Account Security Settings"/>
</p>

5. **Find App Passwords Section**: After clicking on 2FA, scroll down to the bottom of the page until you find the "App passwords" section.

6. **Navigate to App Passwords**: Click on the "App passwords" option to proceed to the app-specific password generation page.

7. **Authenticate Your Account**: If prompted, enter your email password again to authenticate your account and access the app passwords section.

8. **Name Your App**: On the app passwords page, you'll need to provide a name for the application you're generating the password for. Choose a relevant name, such as "Python SMTP."
<p align="center">
<img src="https://iili.io/JVmONt4.png" height="85%" width="85%" alt="Google App Passwords Page"/>
</p> 

9. **Generate Password**: After naming your application, click on the "Generate" button to generate the app-specific password.

10. **Copy the Password**: Once the password is generated, copy the provided app-specific password. This password will be used within your Python script to authenticate with Gmail's SMTP server securely.

Now that you've successfully generated the app-specific password, you can proceed to use it in your Python script for sending emails via Gmail's SMTP server.

---

<h2>Now, To Send Emails via Python</h2>

### Code for Sending Emails

```python
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
subject = 'Greetings'
body = """
Just wanted to say Hi!

This is a test email.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

em.set_content(body)

# Create SSL context for secure connection
context = ssl.create_default_context()

# Establish connection with Gmail's SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # Authenticate with sender's email and password
    smtp.login(email_sender, email_password)
    # Send email
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("Email has been sent to sender!")
```
Note:  adopted from the code in the youtube video https://www.youtube.com/watch?v=g_j6ILT-X0k&t=260s by The PyCoach

#### Code Explanation:

- **Loading Environment Variables**: The `load_dotenv()` function loads environment variables from a `.env` file into the script.
   - This allows sensitive information, the email password in this case, to be stored securely outside of the codebase.
   - Your app password should be placed in the environment variable that you create, in the `.env` file. In my case, im calling upon the variable, named `EMAIL_PASS`, in `os.environ.get("EMAIL_PASS")`

- **Establishing Secure Connection with SSL**: The `ssl.create_default_context()` function creates a secure SSL context for establishing a secure connection with Gmail's SMTP server (`smtp.gmail.com`).
   - SSL (Secure Sockets Layer) is a standard security technology that encrypts data transmitted between the server and the client, ensuring secure communication.

- **Sending Email via SMTP**: The `smtplib.SMTP_SSL()` function creates an SMTP connection with Gmail's SMTP server over SSL/TLS.
   - It includes parameters such as the server address (`smtp.gmail.com`), port number (`465` for SMTP over SSL), and SSL context. The `login()` method authenticates the sender's email and password with the SMTP server, while the `sendmail()` method sends the email message (`em`) from the sender to the receiver.

#### Security Considerations:

- **SSL (Secure Sockets Layer)**: SSL encrypts the data transmitted between the client and server, preventing interception or tampering by attackers.
   - In this script, SSL is used to establish a secure connection with Gmail's SMTP server, ensuring the secure transmission of email credentials and message content.

- **Two-Factor Authentication (2FA)**: Although we dont actually implement this in the code script, enabling 2FA for your Gmail account adds an extra layer of security. Its still kind of relevant since you cant acess app passwords without it.
   - With 2FA, even if an attacker obtains your email password, they would still need a secondary authentication factor (e.g., a verification code sent to your mobile device) to access your account.

- **App-Specific Password**: When 2FA is enabled for your Gmail account, you can generate an app-specific password to authenticate with Gmail's SMTP server.
   - This password, used instead of your regular Gmail password, provides a secure way to access your email account from external applications, like this python script in our case.

---

This documentation serves as a record of the steps taken to set up email automation using Python and Gmail's SMTP server, including the configuration of 2FA and the generation of an app-specific password for authentication purposes.
