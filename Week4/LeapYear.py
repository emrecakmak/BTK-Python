#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:47:11 2019

@author: emre

"""


year=input("Please enter a year: ")

def leapYearCalc(year):
    if int(year)%4==0:
        print("This year is a leap year")
    else:
         print("This year is not leap year")
            
    
leapYearCalc(year)
    

#2
def leapCalc2(year):
    for i in range(1000,1501):
        if leapYearCalc(i):
            print(i)

leapCalc2(year)
