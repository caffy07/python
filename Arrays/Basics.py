#Arrays in python are dynamic sized arrays whereas arrays in c/c++ are fixed sized

import array as arr    #or use 'from array import *'

#array syntax
arr1 = arr.array('i', [2,4,5,6,10,12,15,128,190])
print(arr1)                         #output: array('i', [2, 4, 5, 6])

#Accessing array elements
print(arr1[1])                      #output: 4

#length of array
print(len(arr1))                    #output: 9

#another way of defining arrays in python is using list:
arr1 = [1,2,3,4,5]
