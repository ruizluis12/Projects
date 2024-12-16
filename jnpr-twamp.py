#!/usr/bin/env python3
import os
import time

time.sleep(1)

hostnames = [
    '172.29.2.254',
    '172.29.4.100',
]

for hostname in hostnames:
    print ('\n')
    response = os.system('ping -c 4 ' + hostname)

time.sleep(1)


print('\n \n-----TWAMP-2 is listening on UDP port 5000------')
os.system('/home/lab/twampy/./twampy.py' + ' responder' + ' 172.29.2.100:5000')
