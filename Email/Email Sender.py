import smtplib
import credentials

def send_email(subject, msg, receiver):
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(credentials.SENDER, credentials.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(credentials.SENDER, receiver, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Test"
msg = "je test ta patience"
receiver="valentin.colin78@gmail.com"

send_email(subject, msg, receiver)
