#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:43:11 2019

@author: emre
"""

#DNA Question


def countDnaMax(DNA):
    count=1
    maximum=0
    maxNukteotit=""
    
    for i in range(len(DNA)-1):
        if DNA[i]==DNA[i+1]:
            count+=1
        else:
            #print(count)
            if count >maximum:
                maximum=count
                maxNukteotit=DNA[i]
            count =1
                
            
    print(maximum)
    print(maxNukteotit)


countDnaMax("GGGGGGTACGAGTTTTTTTTTTTACAA")