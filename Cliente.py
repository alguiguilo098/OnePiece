import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class Cliente:
    def __init__(self,emailsender,password,nickname):
        self.emailsender = emailsender
        self.password = password
        self.nickname = nickname
    def __str__(self):
        return f"{self.nickname}"
    
    def get_email(self):
        return self.emailsender
    def get_nickname(self):
        return self.nickname
    def set_email(self,email):
        self.emailsender = email
    
    def send_email(self, subject, message,emailrecive):
        msg = MIMEMultipart()
        self.emailrecive=emailrecive
        msg['From'] = self.emailsender
        msg['To'] = self.emailrecive
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.emailsender, self.password)
            server.sendmail(self.emailsender, self.emailrecive, msg.as_string())

