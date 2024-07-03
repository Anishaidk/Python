"""# What are Lists?
List is a data type where you can store multiple items under 1 name. More technically, lists act like dynamic arrays which means you can add more items on the fly.

Characterstics of a List:
Ordered
Changeble/Mutable
Hetrogeneous
Can have duplicates
are dynamic
can be nested
items can be accessed
can contain any kind of objects in python"""
# Creating a List
# Empty
print([])

# 1D -> Homo
print([1,2,3,4,5])
# 2D 
print([1,2,3,[4,5]])
# 3D
print([[[1,2],[3,4]]])

# Heterogenous
print([1,True,5.6,5+6j,'Hello'])

# Using Type conversion
print(list('hello'))
"""Accessing Items from a List
1.Indexing
2.Slicing"""
# indexing
L = [[[1,2],[3,4]],[[5,6],[7,8]]]
L1 = [1,2,3,4]

# Positive Indexing 
print(L1[1:4])
print(L[0][0][1]) # for 2

#How to extract 6
print(L[1][0][1])

# Negative indexing
L = [[[1,2],[3,4]],[[5,6],[7,8]]]
L1 = [1,2,3,4]
print(L[-1])

# how to extract 8 with negative 
print(L[-1][-1][-1])

# Slicing
L = [1,2,3,4,5,6]
print(L[::-1])
print("LIST METHODS/FUNCTIONS")
#Adding Items to a List
# Apend -> The append method is used to add an item to the end of a list.
print("Append Function")
L =  [1,2,3,4,5]
L.append(True)
print(L)

# Extend -> The extend method is used to append elements from an iterable (e.g., another list) to the end of the current list.
print("Extend Function")
L = [1,2,3,4,5]
L.extend([2])
print(L)
# Reverse-> reverses the list
print("Reverse Function")
L.reverse()
print(L)
# insert -> The insert method allows you to add an item at a specific position in the list. It takes two arguments: the index where you want to insert the item and the item itself.
print("Insert Function")
l = [1,2,3,4]
l.insert(1,100) 
print(l)
#sort -> sorts the list in ascending order
print("Ascending Order")
l=[1,3,24]
print(l.sort()) #sort function returns none
print(l)
# sort(reverse=True)-> sorts the list in descending order
print("Descending Order")
l.sort(reverse=True)
print(l)

# Editing items in a List
print("Editing items in a List")
l = [1,2,3,4,5,6]

# editing with indexing
print("editing with indexing")
l[-1] = 300
print(l)

# editing with slicing
print("editing with slicing")
l[1:4] = [200,300,400]
print(l)
# Deleting items from a List
# del -> The del statement is used to remove an item from a list based on its index.
print("Deleting items from a List")
l = [1,2,3,4,5]
#indexing
print("Deleting using indexing")
del l[2]
print(l)
# slicing
print("Deleting using slicing")
del l[2:4]
print(l)

# remove -> The remove method is used to remove the first occurrence of a specific value from the list.
print("Remove function")
l = [1,2,3,2,3,2,2,2]
print(l.remove(2)) #returns none
print(l)

# pop -> The pop method is used to remove and return an item from the list based on its index. 
# If you don't provide an index, it will remove and return the last item by default.
print("Pop function")
L = [1,2,3,4,5]
print(L.pop()) #returns the removed item
print(L)
# clear -> The clear method is used to remove all items from the list, effectively emptying it.
print("clear function")
L = [1,2,3,4,5]
L.clear()
print(L)