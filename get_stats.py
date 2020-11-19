# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:34:09 2020

@author: anwar
"""

def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elf[1])])
    return new_stats

def avg(grades):
    return sum(grades)/len(grades)