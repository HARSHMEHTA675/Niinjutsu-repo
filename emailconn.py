import smtplib

host="smtp.gmail.com"
port=587
username = "priyanka27shaha@gmail.com"
password = "spriyanka2711"
from_email=username
to_list=["priyanka27shaha@gmail.com"]

email_conn=smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email,to_list,"Hi priyanka")
email_conn.quit()

from smtplib import SMTP

xyz= SMTP(host,port)
xyz.ehlo()
xyz.starttls()
xyz.login(userName,password)
xyz.sendmail(from_email, to_list, "Hii priyanka")
xyz.quit()

from smtplib import SMTP, SMTPAuthenticationError, SMTPException
xyz= SMTP(host,port)
xyz.ehlo()
xyz.starttls()
try:
    xyz.login(userName, password)
    xyz.sendmail(from_email, to_list, "Hii priyanka")
except:
    print("an error occured")
xyz.quit()
