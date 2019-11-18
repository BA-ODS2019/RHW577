#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:33:04 2019

@author: torkellingvarsson
"""

import requests
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize

# variable med min API-key til Trove
api_key = '6majqpp3si922qkj'
print('Your API key is: {}'.format(api_key))

api_search_url = 'https://api.trove.nla.gov.au/v2/result'

# søge parametre nå vi søger i response
params = {
        'q': 'mahatma+gandhi',
        'zone': 'newspaper',
        'key': api_key,
        'n': '100',
        'encoding': 'json' 
        }
response = requests.get(api_search_url, params=params)
print (response)

json = response.json()


df = json_normalize(json['response']['zone'][0]['records']['article'])
df.head()

# data typer
df.dtypes

# fjerner columns vi ikke har brug for
to_drop = ['category',
          'edition',
          'pageSequence',
          'relevance.score',
          'relevance.value',
           'snippet',
          'troveUrl',
          'url']
# isteder for axis=1 skriver jeg columns= og fjerner herved de columns jeg ikke vil have
df.drop(columns=to_drop, inplace=True)

df['id'].is_unique

# sæt vores index til at være values fra "id" fordi disse values er unikke
# erstatter index med "id"
df.set_index('id', inplace=True)

# plukker ud de første fire tal i column "date"
# sætter dem ind i variabel extr og opretter en column "year" som indeholde første 4 tal fra "date" som ligger i variabel extr
extr = df['date'].str.extract(r'^(\d{4})', expand=False)

df['year'] = pd.to_numeric(extr)
# ved at se på df variabel kan man nu se en column der hedder year

# her gør man det samme som med "years" men laver en column der hedder title
title = df['title.value'].str.extract(r'^(.*?)\s\(', expand=False)

df['title'] = title

df.head()

# Nu laver vi en column for at se hvilke byer vi kan finde
# har valgt 3 byer i tillæg til dem som var skrevet
# det bliver så sat ind i column "city" igennem "np.where"
# Desuden sætter den NaN der hvor der ingen byer er

city = df['title.value']

sydney = city.str.contains('Sydney')
brisbane = city.str.contains('Brisbane')
perth = city.str.contains('Perth')
adelaide = city.str.contains('Adelaide')
melbourne = city.str.contains('Melbourne')



df['city'] = np.where(sydney, 'Sydney',
                      np.where(brisbane, 'Brisbane',
                               np.where(perth, 'Perth',
                                        np.where(adelaide, 'Adelaide',
                                                 np.where(melbourne, 'Melbourne',
                               np.nan)))))
# view the first 20 cities
df['city'].head(20)



to_drop = ['title.value',
          'title.id']
# drop the columns listed in "to_drop" in the dataframe
df.drop(to_drop, inplace=True, axis=1)
# view the first 5 rows of the df
df.head()
















