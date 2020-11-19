# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:54:55 2020

@author: anwar
"""

data = []
file_name = input("Provide a name of a file of data")

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
    fh.close() #close file even if fail
    
gradesData = []
if data:
    for student in data:
        try:
            gradesData.append([student[0:2], [student[2]]])
            
        except IndexError:
            gradesData.append([student[0:2], []])