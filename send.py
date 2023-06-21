import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "bryantg1703@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "bryantg1703@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
    # The function expects arguments in order, but context is a few arguments down the list, so we have to be more specific
        server.login(username, password)
        server.sendmail(username, receiver, message)