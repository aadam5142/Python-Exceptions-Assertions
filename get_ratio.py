# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:13:08 2020

@author: anwar
"""

# Example: Raising an Exception

def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
    Returns: a list containing L1[i]/L2[i]"""
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios


    
    