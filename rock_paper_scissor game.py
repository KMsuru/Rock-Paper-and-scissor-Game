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

game_image = rock, paper, scissors

while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
    
    if user_choice >= 0 and user_choice <= 2:
        print(game_image[user_choice])
        
        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_image[computer_choice])
        
        if user_choice == 0 and computer_choice == 1:
            print("You Lose! Please try again!")
        elif user_choice == 0 and computer_choice == 2:
            print("You Win! Congrats!")
            break 
        elif user_choice == 0 and computer_choice == 0:
            print("Tie!")
        elif user_choice == 1 and computer_choice == 0:
            print("You Win! Congrats!")
            break 
        elif user_choice == 1 and computer_choice == 1:
            print("Tie!")
        elif user_choice == 1 and computer_choice == 2:
            print("You Lose! Please try again!")
        elif user_choice == 2 and computer_choice == 0:
            print("You Lose! Please try again!")
        elif user_choice == 2 and computer_choice == 1:
            print("You Win! Congrats!")
            break 
        elif user_choice == 2 and computer_choice == 2:
            print("Tie!")
    else:
        print("Invalid choice, please try again.")