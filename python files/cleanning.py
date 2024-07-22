import pandas as pd# importing a library to handle csv files
import numpy as np#for cleaning we need this laibrary
data=pd.read_csv('data/Air_Quality_Continuous.csv')#reading the csv file

data_optimized=data[(data['Date_Time']>='2015/01/01 00:00:00+00') & (data['Date_Time']<='2023/10/22 24:00:00+00')]#cropping data

data_optimized=data_optimized[data_optimized['Site_ID'].notnull()]#removing unvalid records

data_optimized=data_optimized.replace({'NOx'    : data_optimized[data_optimized['NOx']<0]['NOx'].values},         np.nan)#replacing unvalid values with nan
data_optimized=data_optimized.replace({'NO2'    : data_optimized[data_optimized['NO2']<0]['NO2'].values},         np.nan)
data_optimized=data_optimized.replace({'PM10'   : data_optimized[data_optimized['PM10']<0]['PM10'].values},       np.nan)
data_optimized=data_optimized.replace({'O3'     : data_optimized[data_optimized['O3']<0]['O3'].values},           np.nan)
data_optimized=data_optimized.replace({'NVPM10' : data_optimized[data_optimized['NVPM10']<0]['NVPM10'].values},   np.nan)
data_optimized=data_optimized.replace({'VPM10'  : data_optimized[data_optimized['VPM10']<0]['VPM10'].values},     np.nan)
data_optimized=data_optimized.replace({'NVPM2_5': data_optimized[data_optimized['NVPM2_5']<0]['NVPM2_5'].values}, np.nan)
data_optimized=data_optimized.replace({'PM2_5'  : data_optimized[data_optimized['PM2_5']<0]['PM2_5'].values},     np.nan)
data_optimized=data_optimized.replace({'VPM2_5' : data_optimized[data_optimized['VPM2_5']<0]['VPM2_5'].values},   np.nan)
data_optimized=data_optimized.replace({'CO'     : data_optimized[data_optimized['CO']<0]['CO'].values},           np.nan)
data_optimized=data_optimized.replace({'RH'     : data_optimized[data_optimized['RH']<0]['RH'].values},           np.nan)
data_optimized=data_optimized.replace({'SO2'    : data_optimized[data_optimized['SO2']<0]['SO2'].values},         np.nan)

data_optimized.drop_duplicates(subset=['Date_Time', 'Site_ID'], keep='last')# removing duplicates


#this data is clean by implementing two condition
data_optimized1=data_optimized[:250000]
data_optimized2=data_optimized[250000:]
data_optimized.to_csv('cropped.csv', index=False,encoding='utf-8')#this is the way we store the csv
data_optimized1.to_csv('cropped1.csv', index=False,encoding='utf-8')
data_optimized2.to_csv('cropped2.csv', index=False,encoding='utf-8')

task6_sorted = data_optimized.sort_values(by='NOx', ascending=False).copy()

task6=task6_sorted[task6_sorted['Site_ID']== 501].head(10000)

task6.to_csv('task6.csv', index=False,encoding='utf-8')
