#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:14:29 2019

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

# søge parametre (dette svare til den URL som man laver i browser vinduet på Trove)
params = {
        'q': 'mahatma+gandhi',
        'zone': 'newspaper',
        'key': api_key,
        'n': 0,
        'encoding': 'json',
        'facet': 'year',
        }
response = requests.get(api_search_url, params=params)
print (response)

json = response.json()

# laver nu en dataframe via pandas
df = json_normalize(json['response']['zone'][0]['facets']['facet']['term'])
df.head()

# hvilke datatypes har vi med at gøre
df.dtypes

# ændre "count" column til numerisk data type
df['count'] = pd.to_numeric(df['count'])

# før var "count" = object, nu er den int64
df.dtypes

# nu skal columns "search" og "url" fjernes
df.drop(['search', 'url'], inplace=True, axis=1)

# derefter skal "display" column ændres til "year"
df.rename(columns={'display':'year'}, inplace=True)

# vis formateret DF:
df.head
# nu er der bare count og year tilbage som columns
# nu er der kun numeriske values tilbage som man kan beregne på
# se tutorial kode med mean/median/mode beregninger

    # MEAN

# mean for hele DF
df.mean()

# mean for specfik column
df.loc[: , "count"].mean()

    # MEDIAN

# median af DF
df.median()

    # summary stats
df.describe()

    # MODE
df.mode(axis=1)
# Giver nogle mærklige værdier, bl.a. nogle NaN værdier
# anderledes værdier også ved at skrive axis=0


