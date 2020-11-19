# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:04:27 2020

@author: anwar
"""

try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
    print("Okay")
except:
    print("Bug in user input.")
print("Outside")
