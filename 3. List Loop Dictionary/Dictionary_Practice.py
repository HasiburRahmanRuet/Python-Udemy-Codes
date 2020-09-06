# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 15:43:37 2020

@author: Naznin
"""



# capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
#             'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
#             'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
#             'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
#             }

# user_inp=(input("Enter the country to find it's capital\n>>")).capitalize()
# while user_inp not in capitals:
#     print('Wrong Input')
#     user_inp=(input("Enter the valid country to find it's capital\n>>")).capitalize()
# print(f'The capital of {user_inp} is {capitals[user_inp]}') 

# a=0
# b=1
# fibb_dict={}
# for i in range(1,13):
#     fibb_dict[i]=a
#     a,b=b,a+b
# print(fibb_dict)


# companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
# key_names = ['Open','High','Low','Close']
# prices = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
# [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]


# # c_key_P={}
# # for i in companies:
# #     key_dic={}
# #     for j in range(len(key_names)):
# #         key_dic[key_names[j]]=prices[j]
# #     c_key_P[i]=key_names[j]
        
# d_1={}    
# for i in range(len(prices)):
#     d_1[companies[i]]=dict(zip(key_names,prices[i]))
        
        
        
# import datetime
# time1 = datetime.timedelta(days=365,hours=23, minutes=59, seconds=59)
# time2 = datetime.timedelta(366)
# print(time2-time1)

# birthday=datetime.date(1994, 7, 21)
# age=datetime.date.today()-birthday

import random
ran_char_dict={}
letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for ch in letter:
    ran_char_dict[ch]=random.randint(1, 101)
print(ran_char_dict)

import matplotlib.pyplot as plt
x,y=zip(*ran_char_dict.items())
plt.bar(x,y)

























