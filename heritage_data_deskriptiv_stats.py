#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:37:06 2019

@author: torkellingvarsson
"""
import pandas as pd
import numpy as np

    # MEAN UDREGNING 
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


    # MODE UDREGNING


# calculate mode or most repeated value


print(statistics.mode([1,5,5,7,5,6,8,7]))
print(statistics.mode(['lion', 'cat', 'cat','dog','tiger']))

#Create a DataFrame
d3 = {
    'Name':['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
   'Rahul','David','Andrew','Ajay','Teresa'],
   'Score1':[62,47,55,74,47,77,85,63,42,32,71,57],
   'Score2':[89,87,67,55,47,72,76,79,44,67,99,69],
   'Score3':[56,86,77,45,73,62,74,89,71,67,97,68]}
 
 
 
df3 = pd.DataFrame(d3)
df3

df3.mode()

df3.mode(axis=0)


# mode of the specific column
df3.loc[:,"Score1"].mode()


    # Descriptive / Summary stats i pandas
    
# creation of DataFrame

 
#Create a Dictionary of series
d4 = {'Name':pd.Series(['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
   'Rahul','David','Andrew','Ajay','Teresa']),
   'Age':pd.Series([26,27,25,24,31,27,25,33,42,32,51,47]),
   'Score':pd.Series([89,87,67,55,47,72,76,79,44,92,99,69])}
 
#Create a DataFrame
df4 = pd.DataFrame(d4)
print(df4)

# Describe funktion
print(df4.describe())

# summary statistics of character column
 
print (df4.describe(include=['object']))

# summary statistics of character column
 
print (df4.describe(include='all'))





