#Assignment 2: In this, I am encrypting multiple pdf files at a time in Hexadecimal form for Security and
#              those pdfs are password protected which can be open by getting correct password only.
#              Also I am making an automative e-mail template which say that this mail has pdf, its password and also its encrypted password.

import hashlib
import os
from datetime import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#encription is done
def password_encryption(password):
    import hashlib
    hash_func = hashlib.sha1()
    encode_string = password.encode()
    hash_func.update(encode_string)
    message = hash_func.digest()
    return  message

from PyPDF2 import PdfFileWriter, PdfFileReader

file=os.listdir(r"C:\Users\DELL\PycharmProjects\pythonProject")
print(file)

sender_person=input("Enter mail:" )
security_purpose=input("Enter password:")
receiver_person=input("Enter mail:")

#multiple pdf files are getting encrypted
for j, i in enumerate(file):
    if i.endswith(".pdf"):
        out = PdfFileWriter()
        input = PdfFileReader(f"C://Users//DELL//PycharmProjects//pythonProject//{i}")

        num = input.numPages
        for idx in range(num):
            page = input.getPage(idx)
            out.addPage(page)
        current_time = datetime.now().replace(microsecond=0)
        format = "%y_%b_%d_%H_%M_%S"
        new_time = datetime.strftime(current_time, format)
        password = new_time
        out.encrypt(password)
        with open(rf"C:\Users\DELL\PycharmProjects\pythonProject\{password}", "wb") as f:
            out.write(f)
        time.sleep(2)
        pas = password_encryption(password)
        #print(pas)

        #E-mail template creating

        body = '''Hello,This is your pdf and your password {} and also your encrypted password {}'''.format(
            password, pas)
        message = MIMEMultipart()
        message['From'] = sender_person
        message['To'] = receiver_person
        message['Subject'] = 'This email has an attachment'
        message.attach(MIMEText(body, 'plain'))
        pdfname = '{}'.format(password)
        binary_pdf = open(pdfname, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binary_pdf).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_person, security_purpose)
        text = message.as_string()
        session.sendmail(sender_person, receiver_person, text)
        session.quit()
        print('Mail is Sent to your mail Id..')







