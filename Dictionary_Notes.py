print("DICTIONARY IN PYTHON")
#Dictionary -> It consists of key and values,{},
mydic={"Username":"Admin",
       "Password":123,
       "Brand":"Lenovo"}
print("original dictionary")
print(mydic)
print("The username is:",mydic['Username'])# In the square bracket you enter the key and it will show you the value of the key
# Nested Dictionary
print("Nested Dictionary")
student={"name":"anisha",
         "subjects":{
             "maths":90,
             "science":80,
             "english":70
            }}
print("Students subject and marks is:",student["subjects"])
print("marks in Maths is",student["subjects"]["maths"])
#Update
print("Update")
mydic['Username']= "Me"# You can change the values with the help of the key only not through index value
print(mydic)
#Add single value
print("Add single value")
mydic['Yearofmake']= "2023"
print(mydic)
#Add multipule values
print("Add multiple values")
mydic['Brand']= ["a","b","c"]
print(mydic)
# Adding a list to a dictinory
print("Adding a list to a dictionary")
list1 = [1,"bhca",3.260,4]  
mydic['List']=list1
print(mydic)
# merging two dictionarys
print("Merging two dictionarys")
mydic2={"Username":"Admin",
    "Password":123,
    "Brand":"Lenovo"}
mydic.update(mydic2)
print(mydic)
#Remove a value
print("Remove a value")
mydic.pop("Brand")
print(mydic)
#Delete the whole dictionary
print("Delete the whole dictionary")
del mydic
print(mydic2)
