# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
int_input= input("Input an integer within the range (1-5):\n>>>")
if int_input.isdigit():
    if int(int_input) >=1 and int(int_input)<=5:
        print ("The inputed number is = " + str(int_input))
    else:
        print("Out of Range")
else:
    print("Wrong input")
