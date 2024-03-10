<h2>Description</h2>
This repository serves as a documentation of the steps taken to set up email automation using Python, specifically focusing on connecting Python to Gmail's SMTP server. The process involves configuring two-factor authentication (2FA) for added security and generating an app-specific password to authenticate Python with Gmail.

<h2>Languages Used</h2>

- Python

<h2>Utilities Used</h2>

- Visual Studio Code Codespaces

---

<h2>Steps Taken</h2>

# Setting Up Two-Factor Authentication for Gmail

1. **Visit Google Account Settings**: Begin by accessing your Google account settings through [myaccount.google.com](https://myaccount.google.com).
   
2. **Access Security Settings**: Navigate to the "Security" tab within your Google account settings.
   
3. **Enable 2-Step Verification**: Scroll down to locate the option for "2-Step Verification" and enable it for enhanced security.
<p align="center">
<img src="https://iili.io/JVmE4Qn.png" height="85%" width="85%" alt="Google Account Security Settings"/>
</p>
   
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

# Generating App-Specific Password for Python
After completing the 2FA setup, the next step is to generate an app-specific password for Python to connect to Gmail:

10. **Access App Passwords**: Modify the URL in your browser's address bar to be "myaccount.google.com/apppasswords" and navigate to this page.
  - The URL modification may include removing any additional parameters, such as "u/1/", that are specific to your account.
    <p align="center">
    <img src="https://iili.io/JVmjW8b.png" height="85%" width="85%" alt="Google Account Security Settings"/>
    </p>
    <p align="center">
    <img src="https://iili.io/JVmjBuR.png" height="85%" width="85%" alt="Google App Passwords Page"/>
    </p>
    <p align="center">
    <img src="https://iili.io/JVmjK8J.png" height="85%" width="85%" alt="Google App Passwords Page"/>
    </p> 
   
11. **Login Authentication**: Enter your account password when prompted to authenticate.

12. **Name Your App**: Give a relevant name to the application for which you're generating the password, such as "Python SMTP."
    - For example, in this case, the application is named "Python."
    <p align="center">
    <img src="https://iili.io/JVmONt4.png" height="85%" width="85%" alt="Google App Passwords Page"/>
    </p> 

13. **Generate Password**: After naming your application, proceed to generate the app-specific password by clicking on "Create".

14. **Copy the Password**: Once generated, copy the provided app-specific password. This password will be used within your Python script to authenticate with Gmail.

---

This documentation serves as a record of the steps taken to set up email automation using Python and Gmail's SMTP server, including the configuration of 2FA and the generation of an app-specific password for authentication purposes.
