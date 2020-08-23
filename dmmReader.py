# -*- coding: utf-8 -*-

import pydmm.pydmm as pd

initial_voltage = 5;
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