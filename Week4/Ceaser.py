#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:05:22 2019

@author: emre
"""

#Sezar
import random


def ceasar(text,key):
    encodedText=""
    for i in text:
        encodedText += chr(ord(i)+key)
        

    return encodedText

text="Pskolog piskolog piskiyatr pskytr"
key=random.randrange (1,26,1)  

encodedText=ceasar(text,key)
print("Encoded {"+encodedText+"}")

decodedText=ceasar(encodedText,key*-1)
print("Decoded {"+decodedText+ "}")