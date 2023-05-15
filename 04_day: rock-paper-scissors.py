# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
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

choice = {0: 'Rock', 
          1: 'Paper',
          2: 'Scissors'}

ascii_art = [rock, paper, scissors]

#Write your code below this line 👇
import random

hand_signal = int(input('what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))


if hand_signal >= 3 or hand_signal < 0:
  print('\nInvalid user input. You lose.')
else:
  print('\nYou chose: ', choice[hand_signal])
  print(ascii_art[hand_signal])
  
  computer_choice = random.randint(0,2)
  
  print('Computer chose: ', choice[computer_choice])
  print(ascii_art[computer_choice])
  
  if hand_signal == computer_choice:
    print('Match drawn!')
  elif (hand_signal == 0 and computer_choice == 1) or (hand_signal == 1 and computer_choice == 2) or (hand_signal == 2 and computer_choice == 0):
    print('You lose.')
  else:
    print('You won!')
