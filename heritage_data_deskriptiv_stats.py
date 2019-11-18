#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:37:06 2019

@author: torkellingvarsson
"""
import pandas as pd
import numpy as np

# calculate arithmetic mean
import statistics
 
print(statistics.mean([1,9,5,6,6,7]))
print(statistics.mean([4,-11,-5,16,5,7]))


 
#Create a DataFrame
d = {
    'Name':['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
   'Rahul','David','Andrew','Ajay','Teresa'],
   'Score1':[62,47,55,74,31,77,85,63,42,32,71,57],
   'Score2':[89,87,67,55,47,72,76,79,44,92,99,69]}
 

df = pd.DataFrame(d)
# beregner mean på tværs af columns
df.mean()

# column mean of the dataframe
df.mean(axis=0)

# regner ud mean på tværs af rows altså denne vej -->
df.mean(axis=1)

# mean of the specific column
df.loc[:,"Score1"].mean()

# MEDIAN UDREGNING

# calculate median or middle value
 
print(statistics.median([1,9,5,6,8,7]))
print(statistics.median([4,-11,-5,16,5,7,9]))

d2 = {
    'Name':['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
   'Rahul','David','Andrew','Ajay','Teresa'],
   'Score1':[62,47,55,74,31,77,85,63,42,32,71,57],
   'Score2':[89,87,67,55,47,72,76,79,44,92,99,69],
   'Score3':[56,86,77,45,73,62,74,89,71,67,97,68]}
 
df2 = pd.DataFrame(d2)
df2

# median of the dataframe
df2.median()

# column median of the dataframe
df2.median(axis=1)

# median of the specific column
df2.loc[:,"Score1"].median()