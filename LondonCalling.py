#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 08:56:47 2022

@author: marciobernardo
"""

# Let's import the pandas, numpy libraries as pd, and np respectively. 
import pandas as pd
import numpy as np
# Load the pyplot collection of functions from matplotlib, as plt 
from matplotlib import pyplot as plt


# importing data

url_LondonHousePrices = "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"

properties = pd.read_excel(url_LondonHousePrices, sheet_name='Average price', index_col= None)

# data visualisation

properties.head() # has NaNs

properties.dtypes

properties.shape

properties.info()




properties = properties.drop(properties.columns[[34,37,47]], axis=1)

NaT = properties.iloc[[0]]
properties = properties.iloc[1:]

properties.info()

properties.head()

properties = properties.rename(columns = {properties.columns[0]: 'Date'})

properties.head()

properties_long = properties.melt(id_vars = 'Date', var_name='Location', value_name ='Price')

properties_long.head(10)

properties_long.dtypes

properties_long.Price = properties_long.Price.astype(float, errors= 'raise')

properties_long.info()

ks = properties_long[properties_long['Location'] == 'Kensington & Chelsea']

ks.plot(x = 'Date', y = 'Price')

df1 = properties_long[['Location','Price']].groupby('Location').agg(['first', 'last', lambda x: (x.iloc[0] / x.iloc[-1]) *100])['Price']

df = properties_long[['Location','Price']].groupby('Location').agg(lambda x: (x.iloc[-1] / x.iloc[0]) *100)

df1.sort_values('last', ascending = False)
df.sort_values('Price', ascending = False)


london_boroughs = ['Barking & Dagenham', 'Barnet', 'Bexley', 'Brent' , 'Bromley','Camden','Croydon','Ealing','Enfield','Greenwich','Hackney', 'Hammersmith & Fulham','Haringey','Harrow', 'Havering','Hillingdon','Hounslow','Islington', 'Kensington & Chelsea','Kingston upon Thames','Lambeth ','Lewisham','Merton','Newham','Redbridge','Richmond upon Thames','Southwark','Sutton','Tower Hamlets','Waltham Forest','Wandsworth','Westminster']


len(london_boroughs)

df.sort_values('Price', ascending = False)



def create_price_ratio(loc):
    '''Function calculate the ratio between 1998 and 2018 average house prices of lacations in the LondonHousePrices database.'''
    properties_date = properties_long[(properties_long.Date >= '1998-01-01') & (properties_long.Date <= '2018-12-01')] 
    if type(loc) is list:
        df = properties_date[properties_date.Location.isin(loc)][['Location', 'Price']].groupby('Location').agg(lambda x: (x.iloc[-1] / x.iloc[0]))
        return df
    elif type(loc) is str:
        df = properties_date[properties_date['Location'] == loc]
        pr = df.Price.iloc[-1] / df.Price.iloc[0] 
        print(f'{loc}   {pr}')
    else:
        print('Please enter a valid location.')

create_price_ratio(london_boroughs)

create_price_ratio('Sutton')

