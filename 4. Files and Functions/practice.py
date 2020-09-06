# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 23:18:03 2020

@author: Naznin
"""


# file=open('myfiletest.txt','w')
# file.write("I am Md. Hasibur Rahman.\nI am from my country!!")
# file.close()
# file=open('myfiletest.txt','r')
# print(file.read())
# file.close()

# with open('myfiletest.txt','r') as f:
#     line=f.readlines()
#     print(line,end='')


# def fib(n):
#     a=0
#     b=1
#     for i in range(n+1):
#         a,b=b,a+b
#     return a

# for i in range(12):
#     print(fib(i))

# def calc(*remain):
#     return sum(remain),len(remain)

# res,length=calc(10,20,30,40,50)
# print(res,length)

# def multiply(a=6,b=2):
#     return a*b

# print(f'The result is {multiply(8)}')

# file = open("capital.txt",'w')
# file.write("Dhaka,")
# file.write(" Rajshahi")
# file.close()

user_inp=input("Write a capitals name\n>>")
file=open("capital.txt",'a')
file.write(","+user_inp)
file.close()

def copy_files(file1,file2):
    f1=open(file1,'r')
    f2=open(file2,'w')
    f2.write(f1.read())
    
copy_files("capital.txt", "copy_capital.txt")


























