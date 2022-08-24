#-*- coding: utf-8 -*-
#source: https://www.todaymart.com/578

import os
import socket
from plyer import notification
from time import strftime, localtime, time, sleep

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def logging_internet_status(type: str, now_status:None=None):
    with open('internet_status.log', 'a', encoding='utf-8') as f:
        now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
        if type == 'start':
            f.write("==\n")
            f.write(f"[{now_time}] program is starts: is internet disconnect? {now_status}\n")
        if type == 'closed':
            f.write(f"[{now_time}] internet is disconnect.\n")
        elif type == 'connected':
            f.write(f"[{now_time}] internet is connect with the IP address of {ipaddress}\n")
    
ipaddress=socket.gethostbyname(socket.gethostname())
if ipaddress=="127.0.0.1":
    is_internet_closed = True
else:
    is_internet_closed = False

logging_internet_status('start', is_internet_closed)

while 1:
    sleep(1)
    ipaddress=socket.gethostbyname(socket.gethostname())
    if ipaddress=="127.0.0.1":
        if is_internet_closed != True:
            is_internet_closed = True
            logging_internet_status("closed")
            notification.notify(
            title='Notice',
            message='Internet is down.',
            )
    else:
        if is_internet_closed != False:
            is_internet_closed = False
            logging_internet_status("connected")
            notification.notify(
            title='Notice',
            message='You are connected to the internet again.',
            )
