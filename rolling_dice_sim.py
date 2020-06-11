import random
min = 1
max = 6
print("Starting the Game...")

roll_again = "yes" or "y"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the Dices...")
    print("The values are... ")
    print(random.randint(min,max))
    print(random.randint(min,max))

    roll_again = input("Do You wanna roll the dices again ?")
    if roll_again == "No" or roll_again == "n":
        print("Game Over...")