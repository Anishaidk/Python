import time
CLEAR="\1033[2J"
CLEAR_AND_RETURN="033[H"
def timer(seconds):
    time_elapsed=0
    while( time_elapsed<seconds):
        time.sleep(1)
        # time.sleep makes the printing statement take a 1 second break 
        time_elapsed+=1
        time_left=seconds-time_elapsed
        minutes_left=time_left//60 
        # //60 will give only the whole number part of the division
        seconds_left=time_left%60
        print(f"\rAlarm will go out in {minutes_left:02d}:{seconds_left:02d}", end='', flush=True)
        # :02d is used to format the time where it makes the time in digits like 01:03
        # the 0 is used to add padding to a single digit number and the 2d means it makes it into a 2 digit number
minutes=int(input("enter how many minutes to wait: "))
seconds=int(input("enter how many seconds to wait: "))
total_seconds=minutes*60+seconds
timer(total_seconds)