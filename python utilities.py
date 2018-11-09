import smtplib

host="smtp.gmail.com"
port=587
username="XYZ@gmail.com"#user Email id
password="USERPASSWORD"#userPassword
from_list=username
to_list=["ABC@gmail.com"]
email_conn=smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
email_conn.sendmail(from_list,to_list,"sABCGDHFLJKH")

email_conn.quit()
