import pandas as pd

n = 0
pd_file = pd.read_csv(r'C:\Users\Administrator\Desktop\Luoyang\hisdb\SEP_DB20200813.csv', index_col=0)

print(pd_file)
pd_file.plot.line('rPT2401')
