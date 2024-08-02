import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))
if(timestamp<12):
    print("Good Morning Sir")
elif(timestamp>=12 and timestamp<17):
    print("Good Afternoon Sir")
elif(timestamp>=17 and timestamp<21):
    print("Good Evening Sir")
elif(timestamp>=21 and timestamp<=4):
    print("Good Night Sir")
else:
    print("Invalid Time")  