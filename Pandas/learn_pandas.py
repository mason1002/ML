# coding:utf-8

import pandas as pd

# Reading a csv into Pandas.
df = pd.read_csv('uk_rain_2014.csv')

# Changing column labels.
df.columns = ['water_year', 'rain_octsep', 'outflow_octsep', 'rain_decfeb', 'outflow_decfeb', 'rain_junaug',
              'outflow_junaug']

# print(df.head(5))

# how many rows
len(df)

# Basic statistical info on the dataset
pd.options.display.float_format = '{:,.3f}'.format
# Limit output to 3 decimal places.
df.describe()

# Getting a column by label
# print(df['rain_octsep'])
df.rain_octsep

# Creating a series of booleans based on a condition
var = df.rain_octsep < 1000
# print(var)

# Filtering by multiple conditions
var2 = df[(df.rain_octsep < 1000) & (df.outflow_octsep < 4000)]
# print(var2)

# Filtering by String
var3 = df[df.water_year.str.startswith('199')]
# print(var3)


# Getting a row via a numerical index
var4 = df.iloc[30]

# Setting a new index from an existing column
df = df.set_index(['water_year'])
df.head(5)

# Getting a row via a label-based index
var5 = df.loc['2000/01']

# Getting a row via a label-based or numerical index
# NOT　GOOD　var6 = df.ix['1999/00']

# inplace=True to apple the sorting in place
# df.sort_index(ascending=False).head(5)

# Returning an index to data
df = df.reset_index('water_year')
df.head(5)


# Applying a function to a column
def base_year(year):
    base_year = year[:4]
    base_year = pd.to_datetime(base_year).year
    return base_year


df['year'] = df.water_year.apply(base_year)
df.head(5)

# Manipulating structure (groupby, unstack, pivot)
# Groupby
df.groupby(df.year // 10 * 10).max()
