# # print numbers from 1 to 100
# print("numbers from 1 to 100")
# for i in range(1, 101,1):
#     print(i)
# # print numbers from 100 to 1
# print("numbers from 100 to 1")
# for i in range(100, 0, -1):
#     print(i)
# # print multiplication table of a number n
# print("multiplication table of a number n")
# n = int(input("enter a number: "))
# for i in range(1, 11, 1):
#     print(n, "x", i, "=", n*i)
# # sum of n numbers
print("Sum of N numbers")
n=int(input("Enter the number of terms to be added"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum=",sum)