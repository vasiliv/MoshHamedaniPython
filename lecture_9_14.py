from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "vasiliv2000@googlemail.com"
message["subject"] = "test"
message.attach(MIMEText("blablabla"))

with smtplib.SMTP("host = smtp.gmail.com", port=587) as smtp:
    #communication between the server and client hello message
    smtp.ehlo()
    #transport layer security (encrypted messages)
    smtp.starttls()
    #username and password
    smtp.login("vasiliv2000@googlemail.com","rafternba77")
    smtp.send_message(message)
    print("Email sent")