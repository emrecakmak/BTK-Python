#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:44:12 2019

@author: Emre
"""

sentence=input("Please enter a sentence:")
aWord=input("Please enter a word to search in your string:")
count=0

for i in sentence:
    if i==aWord:
        count+=1

print("Your chosen word ("+aWord+") used "+str(count)+" times in your sentence")
        