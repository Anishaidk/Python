# Q1 Print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
# Q2 Print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1
# Q3 Print the multiplication table of number n
n=int(input("Enter a number:"))
i=1
while i<=10:
    print(n,"X",i,"=",n*i)
    i+=1
# Q4 print the elements of the following list using a loop
# (1,4,9,16,25,36,49,64,81,100)
i=1
while i<=10:
    print(i**2)
    i+=1
# Q5 search for a number X in the tuple using loop
# (1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number to be searched"))
i=1
while i<=10:
    print(i**2)
    if x==i**2:
        print("Number found",x,"at",i)
    else:
        print("Element Not Found")
    i+=1
# Q6 find the sum of N numbers
print("Sum of N numbers")
n=int(input("Enter the number of terms to be added"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print("sum=", sum)
# FACTORIAL OF N NUMBERS
print("Factorial of N numbers")
n=int(input("Enter the number to find factorial:"))
factorial=1
while (i<=n):
    factorial=factorial*i
    i+=1
print("factorial=",factorial)