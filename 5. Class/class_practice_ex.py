# # -*- coding: utf-8 -*-
# """
# Created on Sat Sep  5 13:13:04 2020

# @author: Naznin
# """


# class Patient():
#     '''Creating a python class'''
#     status='Patient'
    
#     def __init__(self,name="Default",age=1):
#         self.name=name
#         self.age=age
#         self.condition_p=[]
    
#     def get_details(self):
#         print(self.status,self.name,self.age,self.condition_p)
    
#     def condition(self,info):
#         self.condition_p.append(info)

# # azad=Patient("Azad",36)
# # Azad.get_details("Azad",36)
    
    
# class Infant(Patient):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#         self.vaccine=[]
    
#     def add_vaccine(self,vaccine_name):
#         self.vaccine.append(vaccine_name)
    
#     def infant_get_details(self):
#         super().get_details()
#         print(f'{self.vaccine}')


# class BankAccount(object):
#     balance=0
#     def __init__(self, acc_name='No name'):
#         self.acc_name=acc_name

    
#     def deposit(self,deposit_amount=0):
#         self.balance=self.balance+deposit_amount
#         print(f"You have diposited {deposit_amount} taka and current balance={self.balance}")
    
#     def withdraw(self,withdraw_amount=0):
#         if self.balance<=50:
#             print("You have not minimum balance for withdraw the amount")
#         elif self.balance>50 and (self.balance-50)<withdraw_amount:
#             print(f"Your current balance is {self.balance} taka but you want to withdraw {withdraw_amount} taka.")
#             print(f"You are short about {self.balance-(withdraw_amount+50)}")
#         else:
#             self.balance=self.balance-withdraw_amount
    
#     def display_info(self):
#         print(f"Name={self.acc_name}\nCurrent Balance = {self.balance}")

# import math
# class circle(object):
    
#     def __init__(self,radius):
#         self.result = math.pi*radius**2 
#     def ret_area(self):
#         return self.result






























