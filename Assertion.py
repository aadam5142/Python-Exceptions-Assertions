# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:45:11 2020

@author: anwar
"""

# Assertion Example

def avg(grades):
    assert not len(grades) == 0,  'no grades data'
    return sum(grades)/len(grades)
