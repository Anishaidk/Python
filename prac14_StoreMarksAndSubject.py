""" enter marks of 3 subjects from the user and store them in a dictionary  Start with an empty dictioary & add one by one. Use subjects name as key and marks as value"""
marks={}
x=int(input("Enter marks in chem"))
marks.update({"chem":x})
y=int(input("Enter marks in phy"))
marks.update({"phy":y})
z=int(input("Enter marks in maths"))
marks.update({"math":z})
print(marks)