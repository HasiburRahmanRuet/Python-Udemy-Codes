# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 15:21:37 2020

@author: Naznin
"""


card='4321650103394909'
sum_d=0
for i in range(2,len(card),2):
    sum_d+=(int(card[-i])*2)
print(sum_d)
for i in range(1,len(card),2):
    sum_d+=(int(card[-i]))
print(sum_d)
if sum_d%10==0:
    print("Valid")
else:
    print("Invalid")    