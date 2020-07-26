import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(
    r'C:\Users\Administrator\Desktop\20200616\SEPSIM3.0\log\SEP_DBHisData1600_V3_bak.csv', index_col='TIME')

data
plt.plot(data['PDI2704.PV'])
plt.show()
