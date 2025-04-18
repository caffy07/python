import array as arr
arr1 = arr.array('i', [2,4,5,6,10,12])

#Adding/Changing elements of an Array:
arr1.append(15)                         #output: array('i', [2, 4, 5, 6, 10, 12, 15])

arr1.extend([23,45,99])                 #output: array('i', [2, 4, 5, 6, 10, 12, 15, 23, 45, 99])

#Insert element at a particular position:  insert(index, value)
arr1.insert(7, 121)                     #output: array('i', [2, 4, 5, 6, 10, 12, 15, 121, 23, 45, 99])

#array concatenation:
a = [2,3,4,5]
b = [11,21,31,41]
c = a + b                                #output: [2, 3, 4, 5, 11, 21, 31, 41]

#Removing/ Deleting elements:
print(c.pop())                           #output: 41
print(c.pop(3))                          #output: 41

c.remove(31)
print(c)                                 #output: [2, 3, 4, 11, 21]

#slicing of array:
print(c[0:3])
