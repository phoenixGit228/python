
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\FMI\Desktop\python\day5\dataset.csv')
print(data.head(3))

# how many countries in this list
total_countries = data['Country_Region'].nunique()
print("total countries : {}".format(total_countries))
# Total confirmed and deaths in US
total_in_US = data[data['Country_Region'] == 'US'][['Confirmed', 'Deaths']].sum()
print("total confirmed and death in US :{}".format(total_in_US))

# Total confirmed in each country, sorted by most to least(print top 10)
confirmed_in_each_country = data[['Country_Region', 'Confirmed']].groupby('Country_Region', as_index=False).agg("sum")
confirmed_sort_in_each_country = confirmed_in_each_country.sort_values(by='Confirmed', ascending=False).head(10)

# bar graph for the result above
# x = confirmed_sort_in_each_country['Country_Region']
# y = confirmed_sort_in_each_country['Confirmed']
# plt.bar(range(len(x)), y, color='green')
# plt.xticks(range(len(x)), x)
# plt.title("confirmed in each country")
# plt.show()

# Total confirmed in China
total_in_China = data[data['Country_Region'] == 'China'][['Confirmed', 'Active']].sum()
print("total confirmed and death in China :{}".format(total_in_China))

# Confirmed and active in each province in China
# sorted by Confirmed from most to least
info_for_China = data[data['Country_Region'] == 'China'][['Province_State', 'Confirmed', 'Active']]
print(info_for_China.sort_values(by='Confirmed', ascending=False))

# Print the country where the deaths number larger than the deaths number China.
number_in_China = data[data['Country_Region'] == 'China']['Deaths'].sum()
deaths = data[['Country_Region', 'Deaths']].groupby('Country_Region', as_index=False).agg("sum")
countries_more_than_China = deaths[deaths['Deaths'] > number_in_China]
print(countries_more_than_China)




import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\FMI\Desktop\python\day5\time_series.csv")
print(data.head(3))
print(data[data["Country/Region"] == 'US'])
transform_data = data[data["Country/Region"] == 'US'].T
filter_data = transform_data[-14:].T
print(filter_data)
date = filter_data.columns
print(len(date))
print(filter_data.values.tolist()[0])
plt.plot(range(len(date)), filter_data.values.tolist()[0])
plt.xticks(range(len(date)), date, rotation=90)
plt.show()


