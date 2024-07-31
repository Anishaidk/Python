import random
"""1--> Snake
-1--> Water
0--> Gun"""
computer=random.choice([-1,0,1])
youstr=input("Enter your choice from s,w and g")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",0:"Gun",-1:"Water"}
you=youDict[youstr]
print(f"You chose {reverseDict[you]}\n Computer Chose {reverseDict[computer]}")
if(computer==you):
    print("Its a tie")
else:
    if(computer==-1 and you==1):
        print("You win")
    elif(computer==-1 and you==0):
        print("You lose")   
    elif(computer==1 and you==0):
        print("You win")
    elif(computer==1 and you==-1):
        print("You lose")
    elif(computer==0 and you==1):
        print("You lose")
    elif(computer==0 and you==-1):
        print("You win")
    else:
        print("SOMETHING WENT WRONG")


