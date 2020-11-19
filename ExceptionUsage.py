# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:22:16 2020

@author: anwar
"""

# Example Exception Usage

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("Input not an integer; try again")
print("Correct input of an integer!")
