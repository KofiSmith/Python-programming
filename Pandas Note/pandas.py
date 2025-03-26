import pandas as pd

#Create a table of the data
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['A','B','C'], index=['X','Y','Z'])

print(df.head()) #Prints few rows

print(df.columns.tolist()) #Prints the columns of the table

print(df.index.tolist()) #Prints the rows

print(df.info()) #Prints an info of the dataset

print(df.describe()) #Gives statistics of the data

print(df.nunique()) #Gives the number of unique items in each column

print(df.shape) #Gives the shape of the data

print(df.size) #Returns the total number of items in the dataset
