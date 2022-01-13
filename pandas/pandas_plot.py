# %%
import pandas as pd
import matplotlib.pyplot as plt
test = pd.read_csv("test2.csv", index_col=0, parse_dates=True)

test.plot.area(figsize=(12, 12), subplots=True)
test.plot.bar(subplots=True)
test.plot.barh()
test.plot.density()
test.plot.hexbin(x='x', y='y')
test.plot.hist()
test.plot.kde()
test.plot.line()
test.plot.pie(subplots=True)
test.plot.scatter(x='x', y='z')

# %%
