print ("hello world")
print("Anisha jha","20") 
print(23)
print(23+43)
name="anisha" #String should be in ""
age=20
# is used for single line comment
print("My Name is:", name)
print("My Age is:", age)
age2=age
print(age2)
old=True #true or false should be written with captial 1st letter like True or False
age=None #none should also be written with capital first letter
print (type(name))
print(type(age)) #type() function is used to know the data type of a variable
print(type(old))
name1="anisha"
name2='anishaa'
name3='''anishaaa'''#string can be written inside single quotes, double quotes or triplequotes(''' ''')
#Arithmetc Operators
a=10
b=6
sum=a+b
print("Sum is:",a+b)
print("difference",a-b)
print("multiplication",a*b)
print("diviision",a/b)
print("remainder",a%b)
print("a to the power b",a**b)
# Relational Operators [ they return boolean value(true/false)]
a=50
b=20
print(a==b)#== means equal to
print(a!=b)#!= means not equal to
print(a>b)# > means greater than
print(a<b)# < means less than
print(a>=b)# >= means greater than or equal to
print(a<=b)# <= means less than or equal to
# Assignment Operator(==,+=,-=,/=,%=,**=)
num=10
num+=10
print(num)
num-=10
print(num)
num*=10
print(num)
num/=10
print(num)
num%=10
print(num)
num**=10
print(num)
#Logical Operator(not,and, or)
a=50
b=30
print( not False)
print(not(a>b))
val1=True
val2=True
print("And Operator", val1 and val2) #True and True returns true ; true and false returns false
print("Or Operator", (a==b) or (a>b))
# type conversion
a=2#int
b=4.25#float
sum=a+b#float is superior to int therefore python converts the int to float and then adds
print (sum)
# if we try to add string to float then it will show an error and python will not convert it to float therefor eno type conversion
c=int("2") #type casting it is done manually here we have converted string to int
d=2.212
sum=c+d 
print (type(c))
print(sum)
# input in python
#result for input() is string
# to convert input() to anything other than string we have to type cast it
name= input("enter your name")
age=int(input("enter age")) #type casted str to int
marks=float(input("enter marks"))#type casted str to float
print("your name is",name,type(name))
print("your age is",age,type(age))
print("your marks is",marks,type(marks))
