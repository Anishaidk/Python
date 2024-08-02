print("Welcome to my first game!!")
name=input("What is your name? ")
age=int(input("What is your age? "))
health=10
if(age<18):
  print("you are not old enough to play")
else:
  print("You are old enough to play the game")
  wants_to_play=input("Do you want to play?").lower()
  if (wants_to_play =="yes"):
      print("Let's play")
      print("you are starting with",health,"health")
      left_or_right=input("First choice...Left or Right(left/right)?").lower()
      if(left_or_right=="left"):
        ans=input("Nice, you follow the path and reach a lake...Do you swim across or go around(across/around)? ").lower()
        if(ans=="around"):
          print("You went around and reached the other side of the lake")
          print("You won")
        elif(ans=="across"):
           print ("you managed to get across, but were bit by a fish and lost 5 health")
           health-=5
           print("your health is now ",health)
           input_ans=input("You notice a house and a river. Which do you go to(river/house)?").lower()
           if(input_ans=="house"):
              print("You go to the house and are greeted by the owner...He doesn't like you and you lose 5 health")
              health-=5
              print("your health is now ",health)
              if(health<=0):
                print("You lost the game")
              else:
                print("you have survived")
           else:
              print("you fell in the river and lost")       
        else:
          print("You lost")     
      else:
        print("you fell down and lost")
  else:
    print("see you later..")