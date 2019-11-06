#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:11:08 2019

@author: emre
"""

#digitalRoot
def digitalRootCalc(n):
    n=str(n)
    counter=0
    while len(n)!=1:
        for i in n:
            counter += int(i)
        n=str(counter)
        counter=0
        print(n)
    return int(n)

print(digitalRootCalc(45893))