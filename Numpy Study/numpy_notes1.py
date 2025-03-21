#Numpy Note 1

import numpy as np

#creating nhmpy arra
a = np.array([1,2,3],dtype="int16")

print(a)

b = np.array([[7,0,8,0,5],[6,0,3,0,1]])

print(b)

#get dimension
print("Number of dimensions(a,b)")
print(a.ndim, b.ndim)

#get shapes of array
print("Shape of array a")
print(a.shape)
print("Shape of array b")
print(b.shape)

#checking data type of arrays
print("data type of array a")
print(a.dtype)
print("data type of array b")
print(b.dtype)
print(b.size)


#ACCESSING AND CHANGING ELEMENTS IN SPECIFIC ROWS, COLUMNS
print("Creating a 2D.numpy array")
c = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(c)

#Accessing a value in numpy 2D array
print(c[1,3])

#get a specific row
print("first row")
print(c[0,:])

print("second row")
print(c[1,:])

#getting a specific column
print("getting column")
print(c[:,2])

#changing an element
print("Changing an element")
c[1,2]= 30
print(c)
