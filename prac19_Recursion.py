#Q1 Write a recursive function to calculate the sum of first n natural numbers.
n=int(input("enter a number"))
def sum(n):
    if n == 1:
        return 1
    else:
        return(n+sum(n-1))
print("sum=",sum(n))
# Q2 Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *
n=int(input("enter a number"))
def pattern(n):
    if n==0:
        return
    print("*"*n)
    pattern(n-1)
print("pattern:",pattern(5))
#Q3 write a recursive function to print all the elements in a list

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
l=["delhi","mumbai","kolkata","jamshedpur","dhanbad","Bhubaneshwar"]
print_list(l)