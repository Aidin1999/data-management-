import pandas as pd# importing a library to handle csv files
data=pd.read_csv('E:/dmf/final/diagram/Air_Quality_Continuous.csv')#reading the csv file
data_optimized=data[(data['Date_Time']>'2015/01/01 24:00:00+00') & (data['Date_Time']<'2023/10/22 24:00:00+00')]#cropping data
#this data is clean by implementing two condition
data_optimized1=data_optimized[:250000]
data_optimized2=data_optimized[250000:]
data_optimized.to_csv('E:/dmf/final/diagram/cropped.csv', index=False,encoding='utf-8')
data_optimized1.to_csv('E:/dmf/final/diagram/cropped1.csv', index=False,encoding='utf-8')
data_optimized2.to_csv('E:/dmf/final/diagram/cropped2.csv', index=False,encoding='utf-8')



