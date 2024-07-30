"""RECURSION
Recursion is the process of defining something in terms of itself
"""
# EXAMPLE:
def factorial(n):
  if (n == 0 or n == 1):  #0! and 1!=1
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)
a=int(input("Enter the number"))
def fibonacci(n):
    if (n==0):
         return 0
    elif (n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range (a):
    print(fibonacci(i))