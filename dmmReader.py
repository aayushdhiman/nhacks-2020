# -*- coding: utf-8 -*-

import pydmm.pydmm as pd
import smtplib, ssl
from email.mime.text import MIMEText

sender_email_password = input("Type your sender email's password and press enter: ")
sender_email = input("Type the email you would like the emails to be sent from and press enter: ")
receiver_email = input("Type the email you would like the emails to be sent to and press enter: ")
port = 465  # For SSL
# Create a secure SSL context
context = ssl.create_default_context()

initial_voltage = 5

def send_email(port, value, location):
    message: "Nicotine detected at port {}, with a volatage value of {} at {}".format(port, value, location)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, sender_email_password)
        server.sendmail(sender_email, receiver_email, message)

charges = {0: (1, "Mens Bathroom (Front)"), 
           1: (5, "Mens Bathroom (Rear)"), 
           2: (3.2, "Women's Bathroom (Front)"), 
           3: (-3, "Women's Bathroom (Rear)")}
# charges = {0: 1, 1: 5, 2: 3.2, 3: -3}

try:
    read_voltage = pd.read_dmm(port=0, timeout=3)
    initial_voltage = read_voltage
except:
    print("Error: Unable to detect DMM")
    
try:
    for i in range(len(charges)):
        read_voltage = pd.read_dmm(port=i, timeout=3)
        charges[i] = read_voltage
except:
    print("Error: Unable to detect DMM")
    
for i in range(len(charges)):
    if charges[i][0] <= initial_voltage - 0.5:
        send_email(str(i), str(charges[i][0]), charges[i][1])

# emailFile = open("emailMsg.txt", "w")
#   print >>email.File, "At port "
# emailFile.close()








# # Open a plain text file for reading.  For this example, assume that
# # the text file contains only ASCII characters.
# with open(textfile, 'rb') as fp:
#     # Create a text/plain message
#     msg = MIMEText(fp.read())

# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = 'Bathroom Nicotine Level Report'
# msg['From'] = me
# msg['To'] = you

# # Send the message via our own SMTP server, but don't include the
# # envelope header.
# s = smtplib.SMTP('localhost')
# s.sendmail(me, [you], msg.as_string())
# s.quit()
