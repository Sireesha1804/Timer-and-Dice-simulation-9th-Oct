import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice ")
    dice_result = roll_dice()
    print(f"You rolled a {dice_result}!")  

    roll_again = input("Do you want to roll again? (y/n): ")
    if roll_again.lower() != 'y':
        print("Thanks for Playing!")
        break 
    


