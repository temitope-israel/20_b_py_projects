# This is a project that sends email - like an email service. A lite version.

from email.message import EmailMessage
from cred_store import sender, password
import ssl
import smtplib

# Example of sender is "icancode@gmail.com" (verbatim, wrap quotes around your mail just as seen...). You could store it in a variable if you wish.

email_sender = sender

# For security reasons, do not include your password in the file if you'll push it to git. Else, you could. Wrap quotes around your password - "mypassword"
email_password = password

# Use any email you like
# email_receiver = 'hakamam415@elixirsd.com'
email_receiver = 'topisco1@hotmail.com'


subject = "FIRST EMAIL APP USING PYTHON!"
body = """
This is my first email app using python. It wasn't that difficult BUT must be mastered...
Now I used a variable to store my password for security reasons.
"""

# Create an instance of the imported EmailMessage() method
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
