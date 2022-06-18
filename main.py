import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_input = input("What do you choose? Type Rock, Paper, or Scissors.\n")

#Random number to determine computer answer
computer_random = random.randint(0, 2)

computer_answer = " "
user_answer = user_input.lower()  #user input to lower case

print("\n")

#Determine User answer and set User answer
if user_answer == "rock":
  user_answer = 0
  print("You throw:\n" + "\nRock" + rock)
elif user_answer == "paper":
  user_answer = 1
  print("You throw:\n" + "\nPaper" + paper)
elif user_answer == "scissors":
  user_answer = 2
  print("User throw:\n" + "\nScissors" + scissors)
else:
  print("You type wrong input, you lose")

#print on next line
print("\n")

#Determine computer answer and set computer answer
if computer_random == 0:
  computer_answer = rock
  print("Computer throw:\n" + "\nRock" + computer_answer)
elif computer_random == 1:
  computer_answer = paper
  print("Computer throw:\n" + "\nPaper" + computer_answer)
else:
  computer_answer = scissors
  print("Computer throw:\n" + "\nScissors" + computer_answer)

print("\n")

#Determine Winner
if user_answer == 0 and computer_random == 2:
  print("You Win!!")
elif computer_random == 0 and user_answer == 2:
  print("You lose...")
elif computer_random > user_answer:
  print("You lose...")
elif user_answer > computer_random:
  print("You Win!!")
elif computer_random == user_answer:
  print("We have a tie")

  