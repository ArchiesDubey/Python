from datetime import date
import smtplib
import config

today=date.today()
day=today.weekday()
subject="Menu"
m=""
def menu(D):
    if(D==0):
         m="A"
    elif(D==1):
         m="B"
    elif(D==3):
         m="C"
    elif(D==4):
         m="D"
    else:
        m="E"
    return m

msg=menu(day)

def send_alert(subject,msg):
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.email,config.password)
        message="Subject:{}\n\n{}".format(subject,msg)
        server.sendmail(config.email,config.emailTo,message)
        server.quit()
        print("Email sent")
    except:
        print("FAILED!!!")


send_alert(subject,msg)


#print(today)
#print(day)