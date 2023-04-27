import random

top_range = input("Type your top range number: ")

if top_range.isdigit():
  top_range=int(top_range)
  
  if top_range <= 0:
    print("Type a number larger than 0 next time")
    quit()

else:
  print("Please type a number next time!")
  quit()
  
generate = random.randint(0,top_range)
guesses=0
while True:
  guesses+=1
  guess_number=input("Enter your guess: ")
  if guess_number.isdigit():
    guess_number = int(guess_number)
  else:
    print("Please Enter a number")
    continue
    
  if guess_number == generate:
    print(f"You got it right its {generate}")
    break
  elif guess_number < generate:
    print("Too low, try a higher number!")
  elif guess_number > generate:
    print("Too high, try a lower number!")
    
print(f"You have {guesses} guesses")
