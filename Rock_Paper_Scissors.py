import random
from random import choice

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

while(1):
    list = [rock, paper, scissors]

    choice = int(input("Let's game rock (1), paper (2), scissors (3), exit (4) take a choice: "))

    pc = random.randint(1, 3)

    if choice in range(1,4):
        print(f"Your choice:\n{list[choice-1]}\n\nPC:\n{list[pc-1]}")

        if choice == pc:
            print("It's a draw")
        elif (choice == 1 and pc == 2) or (choice == 2 and pc == 3) or (choice == 3 and pc == 1):
            print("You lost")
        else:
            print("You won")
    elif choice == 4:
        break
    else:
        print("Invalid choice")

