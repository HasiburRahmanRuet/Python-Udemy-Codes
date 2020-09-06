# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 15:33:35 2020

@author: Naznin
"""

def coin_dic_flip(n):
    head=True
    coin_dic={}
    for i in range(1,n+1):
       coin_dic[i]=head
    for i in range(2,n+1):
       for j in range(i,n+1,i):
            coin_dic[j]= not(coin_dic[j])
    print(coin_dic)

