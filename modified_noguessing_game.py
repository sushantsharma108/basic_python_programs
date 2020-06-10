# this is modified no. guessing game.
# in this game a user will input random no. and compiler will generate random no.

# import random
# guess = 1
# game_over = False
# winning_number = random.randint(1,50)
# user_input = int(input("Enter a No: "))


# while not game_over:                        
#     if user_input == winning_number:
#         print(f"You Win!!! & you guessed this no. in {guess} times.")
#         game_over = True 
#         print("GAME OVER !!!")
#     else:
#         if winning_number < user_input:
#             print("Too high")
#             guess += 1
#             user_input = int(input("Enter again: "))
#         else:
#             print("Too Low")
#             guess += 1
#             user_input = int(input("Enter again: "))

#                   DRY PRINCIPLE OF CODING: DON'T REPEAT YOURSELF.
# optimized code: But sometimes logic is not clear in this type of code.

import random         #You can also define your own winning_no.  instead of using random module which is built in module.
guess = 1
game_over = False
winning_number = random.randint(1,50)

while True:
    user_input = int(input("Enter the no: "))        #while True or while not game_over both are correct                        
    if user_input == winning_number:
        print(f"You Win!!! & you guessed this no. in {guess} times.")
        game_over = True 
        print("GAME OVER !!!")
        break
    else:
        if winning_number < user_input:
            print("Too high")
            
        else:
            print("Too Low")
        guess += 1
        continue

