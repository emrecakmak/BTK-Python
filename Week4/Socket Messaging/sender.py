#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:24:20 2019

@author: emre
"""

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
    inputMessage=input("Message: ")
    message=bytes(inputMessage,"utf-8")
    clientSocket.sendto(message,('localhost',12000))