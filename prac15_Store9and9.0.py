"""find a way to store 9 and 9.0 as values in a set"""
set1={9,9.0}
print(set1)
# python treats 9 and 9.0 as the same number, so when we print the set it only prints one value that is 9
set2={9,"9.0"}
print(set2)
# when we store 9.0 as a string python will treat both the numbers as different values and hence will print both the elements