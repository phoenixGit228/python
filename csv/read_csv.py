# %%
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print(dir(csv))
# print(dir(csv.writer()))

# %%
csv_file = 'test.csv'

with open(csv_file, 'r') as file1:
    data = file1.read()
data = data.split(',')
print(data)
# for i in data:
# print(i)

# %%
data = pd.read_csv(
    r'C:\Users\Administrator\Desktop\20200616\SEPSIM3.0\log\SEP_DBHisData1600_V3_bak.csv', index_col='TIME')

data
plt.line(data['SZB_CYCTIME::KCATW71'])
plt.show()
# %%
