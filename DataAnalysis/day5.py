# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\coding\py\DataAnalysis\dataset.csv')
print(data.head(3))
print(data.columns)

# %%
# how many countires in this list
total_countries = data['Country_Region']
print(total_countries.unique().size)
print(total_countries.nunique())
print(total_countries.count())

# %%
# total confirmed and death in US
total_in_US = data[data['Country_Region']
                   == 'US'][['Confirmed', 'Deaths']].sum()
print(total_in_US)

# %%
# Total confirmed in each country
confirmed_in_each_country = data[['Country_Region', 'Confirmed']].groupby(
    'Country_Region').agg('sum')

print(confirmed_in_each_country)
print(confirmed_in_each_country.index)

# %%
result = confirmed_in_each_country.sort_values(
    by='Confirmed', ascending=False).head(10)
print(result)

# %%
result = confirmed_in_each_country.head(10)
x = result['Country_Region']
y = result['Confirmed']
plt.bar(range(len(x)), y)
plt.show()

# %%
total_in_china = data

# %%

# %%
