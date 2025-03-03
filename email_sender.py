import smtplib
import ssl
import os

#Secured email password via os
email_password = os.getenv("EMAIL_PASSWORD")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "python.email12025@gmail.com"
    password = email_password

    receiver = "szymonstefanski1@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)