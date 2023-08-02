import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD =""
SENDER = ""
RECEIVER = ""

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = ""  # SUBJECT OF EMAIL
    email_message.set_content("")  # Body of email

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image" , subtype= imghdr.what(None,content))

    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(SENDER,PASSWORD)
    mail.sendmail(SENDER, RECEIVER, email_message.as_string())
    mail.quit()