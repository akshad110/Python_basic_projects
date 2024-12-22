import random
user_choice = int(input("Enter number for 0->For Rock\n1->For Paper\n2->For Scissor\n"))
if user_choice < 0 or user_choice > 2:
    print("Please enter correct no from options given below.")
else:
 comp_choice = random.randint(0,2)
 if comp_choice == user_choice:
    print("oops!It's a draw.")
 elif comp_choice == 0 and user_choice == 2:
    print("you loose")
 elif user_choice == 0 and comp_choice == 2:
    print("you win")
 elif comp_choice > user_choice:
    print("you loose.")
 elif user_choice > comp_choice:
    print("you win.")



