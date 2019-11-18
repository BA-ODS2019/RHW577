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
        'n': '100',
        'encoding': 'json',
        'facet': 'year',
        'n': 0
        }
response = requests.get(api_search_url, params=params)
print (response)

json = response.json()

# laver nu en dataframe via pandas
df = json_normalize(json['response']['zone'][0]['facets']['facet']['term'])
df.head()