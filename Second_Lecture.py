# Strings in python
str1= "this is a string.\n this is also a string" #\n adds a new line
str2=''' this is also a string enclosed within\t triple quotes''' #add a tab space
print (str1)
print (str2)
print(str1+str2)#concatenation
print (len(str1)) #length of a string
print(str1[3])#access the character at index 3
str="Anisha Jha"
print(str[0:5])#access the characters from index 0 to 5 (Slicing of string)
print(str[7:len(str)]) #len starts counting from 1 
print(str[2:]) #if we dont write the index number we want to go to python automatically assumes that we want to go to the last index
print(str[:6])#[0:6]    
#in slicing of string, it does not include the last index matlab in 0:5 it will print from index 0 to index 4
#STRING FUNCTIONS
str3="i am a coder"
print(str3.endswith("er"))
print(str3.startswith("i"))
print(str3.capitalize())
print(str3.find("am"))
print(str3.count("a"))
print(str3.replace("am","an"))
print(str3.lower())
print(str3.upper())
