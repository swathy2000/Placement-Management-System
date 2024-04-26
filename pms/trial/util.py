import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "swathykrishna416@gmail.com"
password = "yklcpnwaqbqrtkzg"#'P@ssw0rd'

def send_email(receiver_email, message):
    print("mail..........",receiver_email,message)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    