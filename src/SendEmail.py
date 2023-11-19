import smtplib
from email.mime.text import MIMEText

def format_body(): 
    return "This is the body of the text message"

subject = "Thông báo phân tích lưu lượng"
body = format_body()
sender = "votiendat08112001@gmail.com"
recipients = ["n19dcat016@student.ptithcm.edu.vn"]
password = "owpiaogxnyhoupkw"




def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)