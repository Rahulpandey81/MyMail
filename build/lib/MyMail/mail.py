import smtplib

def send(SENDER_EMAIL,PASSWORD,RECEIVER_MAIL,SUBJECT,MESSAGE):
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
#specify server and port as per your requirement
        server.starttls()
        server.login(SENDER_EMAIL,PASSWORD)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (SENDER_EMAIL, RECEIVER_MAIL, SUBJECT, MESSAGE)
        server.sendmail(SENDER_EMAIL,RECEIVER_MAIL,message)
        server.quit()
        print('successfully sent the mail')
    except Exception as e:
        print(e)
        print("failed to send mail")

