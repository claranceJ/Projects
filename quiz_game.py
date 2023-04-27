print("Welcome to my computer quiz")
print()
playing = input("Do you want to play? ")
score = 0
if playing.lower() == "yes":
  print("Okay! Let's play: ")
else:
  quit()
#or you can add.lower() at the end of the input prompt
answer = input("What does CPU stand for? ")#.lower()
if answer.lower() == "central processing unit":
  print("Correct!")
  score+=1
else:
  print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
  print("Correct!")
  score+=1
  
else:
  print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print("Correct!")
  score+=1
else:
  print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
  print("Correct!")
  score+=1
else:
  print("Incorrect!")

print(f"You got {score} questions correct! ")
percentage=(score/4)*100
print(f"You got {percentage}% ")