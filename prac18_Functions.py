#Q1. print the length of a list (take list as the parameter)
cities=["Delhi","Noida","mumbai","pune","Chennai","jamshedpur"]
heros=["batman","deadpool","wolverine","spiderman","ironman"]
def print_Len(list):
    print(len(list))
    return len(list)
print_Len(cities)
print_Len(heros)
# Q2. print the elements of a list in a single line (take list as the parameter)
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(heros)
print()
# Q3 print factorial of a number
def print_factorial(n):
    fact=1
    for i in range(1,n+1,1):
        fact*=i
    print(fact)
print_factorial(5)
#Q4. convert USD to INR (1usd=83inr)

def convert_usd_to_inr(USD):
    INR = USD * 83
    print("USD VALUE",USD,"in INR=",INR)
    return INR
convert_usd_to_inr(1982)
