# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:27:08 2020

@author: anwar
"""

# Example: Conrol Input
data = []
file_name = input("Provide a name of a file of data ")

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') # remove trailing \n
            data.append(addIt)
finally:
    fh.close() # close file even if fail