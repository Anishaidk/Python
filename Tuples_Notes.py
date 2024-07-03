"""TUPLES IN PYTHON
A tuple is an immutable datatype in python
a()->empty tuple
a(1,)->tuple with only one element needs a comma 
if we dont put a comma python will think of it as an integer value
a(1,2,3,4)->tuple with more than one element
Once defined a tuple can't be altered or manipulated
a[0]=5->this assignment is not allowed for tuples

"""
# creating and printing tuples
print("creating and printing tuples")
a=()
print(type(a))
print(a)
b=(1,)
print(b)
print(type(b))
c=(1,2,3,4)
print(c)
print(type(c))
print("tuple with only one element needs a comma if we dont put a comma python will think of it as an integer value")
d=(1)
print(type(d))
print(d)
print("Slicing in tuples")
# slicing in tuples is same as slicing in python
print(c)
print(c[:1])
print(c[2:])
"""TUPLE METHODS"""
print("TUPLES METHODS")
c=(1,2,3,4,2,3,2,2,2,2)
print(c.count(2))#counting the number of times a value is present in a tuple
print(c.index(2))#gives the index of the first occurence of the value in

