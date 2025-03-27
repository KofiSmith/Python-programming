#Uding numpy for data manipulation and statistics 
import numpy as np

c = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(c)
#Change a column
c[:,1] = [3,3]
print(c)

#Creating a 3D array
print("Creating a 3D array")
d = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])
print(d)
print(d.shape)
print(d.dtype)

print("Accessing a 3D array value")
print(d[1,1,1])
print(d[2,0,0])

#Crating an array of zeros
d = np.zeros((3,3,3))
print(d)
#Creating an array of ones
e = np.ones((3,4,5))
print(e)

#Creating an array of number choice, say 5
f=np.full((3,3,3), 5)
print(f)

#Creating an array of random float numbers
g = np.random.rand(3,3,3)
print(g)

#Creating an array of random int numbers

h= np.random.randint(7,size=(3,3,3))
print(h)
