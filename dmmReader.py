# -*- coding: utf-8 -*-

import pydmm.pydmm as pd
import smtplib
from email.mime.text import MIMEText

initial_voltage = 5;
# charges = {0: [1, "Mens Bathroom (Front)"], 1: [5, "Mens Bathroom (Rear)"], 
#            2: [3.2, "Women's Bathroom (Front)"], 3: [-3, "Women's Bathroom (Rear)"]}

charges = {0: 1, 1: 5, 2: 3.2, 3: -3}

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
    if charges[i] <= initial_voltage - 0.5:
        print("Send email, sound silent alarm with location at port " + str(i))
        

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
