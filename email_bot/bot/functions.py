import smtplib, ssl


async def send_email(receiver_email, message):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "1999shohruhshahobiddinovich@gmail.com"
    password = "xlugzkmfqmhlovkk"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
