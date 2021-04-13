import smtplib

def send_email(user , pwd , recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type (recipient) is list else[recipient]
    SUBJECT = subject
    TEXT = body

    message = "From: %s\nTo: %s\nSubject: %s\n\n%s" %(FROM,", ".join(TO),SUBJECT,TEXT)

    server = smtplib.SMTP("smtp.gmail.com",587)

    server.ehlo()
    server.starttls()
    server.login(gmail_user,gmail_pwd)
    server.sendmail(FROM,TO,message)
    server.close()
    print "successfully sent the mail"

    print "failed to sent mail"
    
if __name__ == "__main__":
    send_email("harshitchourasiya97@gmail.com","Event Management","2015pietcsharshit@poornima.org","fake","dear harshit")
