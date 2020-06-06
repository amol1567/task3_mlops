f=open("/task3_ws/accuracy.txt","r")
acc_data=[]
file=f.readlines()
for line in file:
	acc_data.append(float(line.strip()))
accuracy=str(y[0])
f.close()
print("accuracy for your model:",accuracy)

import smtplib, ssl
port=465 #For SSL
smtp_server = "smtp.gmail.com"
sender_email="jainamol677@gmail.com"
password="1567amoljain"
receiver_email="sharmilajain686@gmail.com"
if accuracy > "0.95"
    message="""  Subject: Report | Prediction Program
    
    Hey Developer, Your model is trained.
    CONGRULATIONS!!!!!
    Your code achieved {}% accuracy.""".format(accuracy)
    
context=ssl.create_default_context()
with smtp.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email, receiver_email, message)