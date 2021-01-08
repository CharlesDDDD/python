import pandas as pd
import numpy as np

# 画图用
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# path
root_dir = 'C:\\Users\\weiha\\Desktop\\cif.mofcom.gov.cn\\'
read_file = root_dir + '批发价格行情_170120_西红柿.txt'

# read data
df = pd.read_csv(read_file)
columns = ['searchDate', 'title', 'AREA', 'COMMDITYNAME', 'COMMDITY_ID', 'COUNTY_ID', 'COUNTY_NAME', 'ENTERID', 'NAME', '当日价格', '前一日价格', '环比', 'RPT_DATE']
df.columns = columns

# drop duplicate records
df = df.drop_duplicates()

# sort
df.sort_values(by=columns, ascending=True)

# RPT_DATE: to datetime dtype
print(df['RPT_DATE'].dtypes)
df['RPT_DATE'] = pd.to_datetime(df['RPT_DATE'])  
print(df['RPT_DATE'].dtypes)

# keep RPT_DATE: 2015-01-01 to 2019-12-31
df = df[(df['RPT_DATE'] >= np.datetime64('2015-01-01')) & (df['RPT_DATE'] <= np.datetime64('2019-12-31'))]

# daily average
df['daily_average'] = df['当日价格'].groupby(df['RPT_DATE']).transform('mean')
df = df[ ['RPT_DATE', 'daily_average'] ]
df = df.drop_duplicates()

# monthly average
df['ym'] = df['RPT_DATE'].dt.to_period('M')
df['monthly_average'] = df['daily_average'].groupby(df['ym']).transform('mean')
df = df[ ['ym', 'monthly_average'] ]
df = df.drop_duplicates()
df.sort_values(by='ym', ascending=True)


ax = df.plot.line(x='ym', y='monthly_average', xticks=df['ym'].to_list(), figsize=(12, 6))
fig = ax.get_figure()
fig.savefig('C:\\Users\\weiha\\Desktop\\cif.mofcom.gov.cn\\fig.png')
