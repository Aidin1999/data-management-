import pandas as pd #for handeling the data
import pymysql#for having a connection

schema = pd.read_csv('data/schema.csv')#reading a csv
schema_values=schema.values#to be replaced in string

constituencies = pd.read_csv('data/constituencies.csv')
constituencies_values=constituencies.values


station = pd.read_csv('data/station.csv')
station_values=station.values

cropped1 = pd.read_csv('cropped1.csv')
cropped1_values=cropped1.values

cropped2 = pd.read_csv('cropped2.csv')
cropped2_values=cropped2.values

connection=pymysql.connect(host='localhost',user='root',db='data_management')#making connecrion
cursor=connection.cursor()#having its cursure

for i in range(schema_values.shape[0]) :#having a loop for each record to be stored in a string  
        cursor.execute(f"insert into `schema` values ('{schema_values[i,0]}','{schema_values[i,1]}','{schema_values[i,2]}')")#each parameter of a table  


for i in range(constituencies_values.shape[0]) :
        cursor.execute(f"insert into `constituencies` values ('{constituencies_values[i,0]}','{constituencies_values[i,1]}','{constituencies_values[i,2]}')")


for i in range(station_values.shape[0]) :
        cursor.execute(f'insert into `station` values ("{station_values[i,0]}","{station_values[i,1]}","{station_values[i,2]}","{station_values[i,3]}","{station_values[i,4]}")')



for i in range(cropped1_values.shape[0]) :
        cursor.execute(f"insert into `read` values ('{cropped1_values[i,0]}','{cropped1_values[i,1]}','{cropped1_values[i,2]}','{cropped1_values[i,3]}','{cropped1_values[i,4]}','{cropped1_values[i,5]}','{cropped1_values[i,6]}','{cropped1_values[i,7]}','{cropped1_values[i,8]}','{cropped1_values[i,9]}','{cropped1_values[i,10]}','{cropped1_values[i,11]}','{cropped1_values[i,12]}','{cropped1_values[i,13]}','{cropped1_values[i,14]}','{cropped1_values[i,15]}','{cropped1_values[i,16]}','{cropped1_values[i,17]}','{cropped1_values[i,18]}')")



connection.commit()#the commandes is commited
cursor.close()#the cursor is closed     
connection.close()

connection=pymysql.connect(host='localhost',user='root',db='data_management')#because we have over half million record of data for read it is better to have 2 connection for importing havlf of it for each 
cursor=connection.cursor()

for i in range(cropped2_values.shape[0]) :
        cursor.execute(f"insert into `read` values ('{cropped2_values[i,0]}','{cropped2_values[i,1]}','{cropped2_values[i,2]}','{cropped2_values[i,3]}','{cropped2_values[i,4]}','{cropped2_values[i,5]}','{cropped2_values[i,6]}','{cropped2_values[i,7]}','{cropped2_values[i,8]}','{cropped2_values[i,9]}','{cropped2_values[i,10]}','{cropped2_values[i,11]}','{cropped2_values[i,12]}','{cropped2_values[i,13]}','{cropped2_values[i,14]}','{cropped2_values[i,15]}','{cropped2_values[i,16]}','{cropped2_values[i,17]}','{cropped2_values[i,18]}')")



connection.commit()
cursor.close()    
connection.close()




    

