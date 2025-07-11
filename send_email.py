import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username ="username@gmail.com"
    password = "password"

    receiver = "receiver@gmail.com"
    context = ssl.create_default_context()

    # message = """\
    # Subject: Test email
    # Hi,
    # This is a test email
    # Thanks
    # """
    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver, message)
        
# send_email()