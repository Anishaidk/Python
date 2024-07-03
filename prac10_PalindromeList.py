list1=[1,2,3]
list2=[1,2,1]
list1_copy=list1.copy()
list1_copy.reverse()
list2_copy=list2.copy()
list2_copy.reverse()
print("for list 1:")
if(list1_copy==list1):
    print("palindrome")
else:
    print("not palindrome")
print("for list 2:")
if(list2_copy==list2):
    print("palindrome")
else:
    print("not palindrome")