import smtplib
from email.message import EmailMessage
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('dasariprasana21@gmail.com','tdvh wgyj rymk tpar')
    msg=EmailMessage()
    msg['FROM']='dasariprasana21@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    print('msg sent')
    server.close()
