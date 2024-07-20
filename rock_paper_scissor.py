import random
user_choice = int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)
print(f"computer chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 1 and computer_choice == 2:
    print("Computer Wins!")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
elif user_choice == 2 and computer_choice == 0:  
    print("Computer Wins!")
elif user_choice == 0 and computer_choice == 1:
    print("You Win!")
elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
elif user_choice == 2 and computer_choice == 2:
    print("It is tie")
elif user_choice == 1 and computer_choice == 1:
    print("It is tie")
elif user_choice == 0 and computer_choice == 0:
    print("It is tie")
