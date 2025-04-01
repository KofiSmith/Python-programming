import pandas as pd

#Loading Data from Files
cars = pd.read_csv('cars.csv')
print(cars.head())
print("")
#Accessing first 10 rows
print(cars.head(10))

print("")
print(cars.describe())
print("")
#Last 4 rows
print(cars.tail(4))

print("")
print(cars.info())
print("")

print(cars.sample(10)) #To access and sample 10 rows 
print("")
#Accessing Specific Values with loc and iloc

print(cars.loc[1]) #Accessing the row at index 1
print("")

print(cars.loc[5:]) #returns the rows from the 5th index
print("")

print(cars.loc[5:8, ["Brand","Year of Manufacture"]]) #Returns the 5th to 7th rows with spe ified columns in array
print("")

#NB: iloc takes the index of rows and index of columns instead of name of columns

#Editing a valus
cars.loc[1, "Brand"]="Ferrari" #Acessing row 1 and Brand column and assigning the value to a different value
print(cars)
print("")

print(cars.sort_values(["Year of Manufacture"],ascending=True)) #Sorting the data by year of manufacture


