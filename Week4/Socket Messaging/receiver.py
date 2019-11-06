#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:51:43 2019

@author: emre
"""

import socket

receiverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiverSocket.bind(('',12000))
print("Reveiver is ready")

while 1:
    message, ipAddress=receiverSocket.recvfrom(2048)
    modifiedmessage = message.decode("utf-8")
    print(modifiedmessage)

    