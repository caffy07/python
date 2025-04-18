#https://realpython.com/linked-lists-python/

#Linked list is a linear collection of elements where each element points to next element in memory
#deletion in linked list is much faster than compared to arrays
#While lists use a contiguous memory block to store references to their data, linked lists store references as part of their own elements.
#They can be used to implement (spoiler alert!) queues or stacks as well as graphs. 
#collections.deque uses an implementation of a linked list in which you can access, insert, or remove elements from the beginning or end of a list with constant O(1) performance.

from collections import deque

#create empty linked list
LL = deque(['a','b','c'])           #output: deque(['a', 'b', 'c'])

#adding elements
LL.append('d')                      #output: deque(['a', 'b', 'c', 'd'])

#deleting last element (right most element)
LL.pop()                            #output: deque(['a', 'b', 'c'])

#adding and deleting elements from start
LL.appendleft('hello')              #deque(['hello', 'a', 'b', 'c'])
LL.popleft()                        #deque(['a', 'b', 'c'])
