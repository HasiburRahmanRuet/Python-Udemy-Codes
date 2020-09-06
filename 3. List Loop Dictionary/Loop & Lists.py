# # -*- coding: utf-8 -*-
# """
# Created on Thu Sep  3 14:16:43 2020

# @author: Naznin
# """


# # word='Bangladesh'
# # for country_ch in word:
# #     print(country_ch, end='\t')

# # print(type(word))

# # data=[10, 'A', 125, word]

# # print(type(data))
# # for element in data:
# #     print(element, end=' ')


# # for element_index in range(len(data)):
# #     print(data[element_index])


# # print()
# # for index in range(len(word)):
# #     print(word[index],end=" ");
    
# data_bubble=[10,8,78,9,15,65]
# data_bubble_copy=data_bubble[:]

# for i in range(len(data_bubble)):
#     for j in range(len(data_bubble_copy)-i-1):
#         if data_bubble_copy[j]>data_bubble_copy[j+1]:
#                 data_bubble_copy[j],data_bubble_copy[j+1]=data_bubble_copy[j+1],data_bubble_copy[j]
                
# print(data_bubble_copy)
# print(sorted(data_bubble, reverse=True))

# # help(sorted)

# my_list=data_bubble[:]
# my_list.extend([10,20,30])
# my_list.remove(20)
# my_list.pop();
# print(my_list)
# print(f'the list {my_list} after sorting is {sorted(my_list)}')

# auto_list=list(range(1,11))
# print(auto_list.count(1))

# print(sum(auto_list))

# import random
# #print(help(random))
# randint_list=list(range(random.randint(1,3),random.randint(90,101)))
# print(randint_list)
# random_list=random.randrange(0,10,1)
# print(random_list)

import random
rand_range_list=[]
for i in range(100):
    rand_range_list.append(random.randrange(10,20))

print(rand_range_list)

import webbrowser

# webbrowser.open("https://www.bubt.edu.bd")


















































            