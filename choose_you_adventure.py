import time, os
while True:
  user_name = input("Type your name: ")
  
  print(f"welcome {user_name} to this adventure")
  
  answer = input("you are standing on a crosss road do you want to go right or left (type right/left): ").lower()
  
  if answer == "right":
    answer = input("You have come across a river do you want to swim or walk around the river(swim/walk): ").lower()
  
    if answer == "swim":
      print("You have chosen to swim across the river and you've been eaten by a crocodile! You lose")
    elif answer == "walk":
      print("You have walked across the river but its quite a distance, you have run out of breath and now you're dead. You Lose!")
    else:
      print("Enter a valid answer")
      
  elif answer == "left":
    answer = input("You are walking across a bridege and you meet a stranger are you talking to them or walking away?(talk/walk): ").lower()
    if answer == "talk":
      print("The stranger has been waiting for you, he has given you all his gold! You win!")
    elif answer == "walk":
      print("You have decided to walk away, there's no road ahead, and also no Gold for you, you lose!")
    else:
      print("Enter a valid answer")
      
  else:
    print("Enter a valid answer!")
    
  time.sleep(2.7)
  os.system('clear')
