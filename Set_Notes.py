# SET IN PYTHON
#set -> Unordered collection of data's,{},immutable,does't contain a duplicate value, can't use index, it's also mutable
# everytime we run the code the set will be printed in a different order

Set1={1,2,3,54,5,4,5,0}
# duplicated values are ignored 
print("The values of Set1 is ",Set1)
print(type(Set1))
print(len(Set1)) #total number of items (Repeated items are ignored)
#print(Set1[2])        # See as here we can't use index values

# Empty set
print("Empty Set")
print("to print empty set we cannot simply write set={} because this is the syntax for empty dictionaryso we have to write set=set() to print empty set")
Set=set()
print("Empty set is ",Set)
print(type(Set))
#Add  (In sets if you want to add data use .add method)
print("Add  (In sets if you want to add data use .add method)")
Set1.add(567)
print(Set1)

# Union() -> It's use to combine the values/elements of sets
print("Union() -> It's use to combine the values/elements of sets")
Set2 = {1,2,"ABC",4,5,6,7,False,9,114.32} 
Set3=Set1.union(Set2)
print(Set3)

Set4={56,564,31,256,15,31,2}
Set5=Set1|Set2|Set3|Set4   
print("This | also stands for union",Set5)   # This | also stands for union

# Intersection -> Shows the elements that are common
Set6=Set1.intersection(Set2)
print("Intersection -> Shows the elements that are common",Set6)

Set7=Set2&Set3&Set4     
print("This & also stands for intersection",Set7)     # This & also stands for intersection

# clear-> to remove all the element of the set
Set1.clear()
print("clear-> to remove all the element of the set",Set1)

# Converting Sets from immutable to mutable
a=frozenset(["E","F"])
print("Converting Sets from immutable to mutable",a)