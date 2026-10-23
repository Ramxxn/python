import random


code_word = {1: "Stone", 0: "Paper", -1:"Scissor"}

def game():
    system_choose = random.choice([1, 0, -1])

    try:
        user_choose = int(input("Enter Number: "))
    except ValueError:
        print("Invalid Input! Please enter a number.")
        return


    if not(user_choose == 1 or user_choose == 0 or user_choose == -1):
        return print("Kindly enter 1, 0 or -1")

    print(f"User Choose: {code_word[user_choose]}\nSystem Choose: {code_word[system_choose]}")

    if(system_choose == user_choose):
        print("Match Has been draw!")
    else:
        if((system_choose == 1 and user_choose == -1) or (system_choose == 0 and user_choose == 1) or (system_choose == -1 and user_choose == 0)):
            print("you loose, Try next time!")
        else:
            print("You Won, Congratulation!")


game()