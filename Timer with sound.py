import time
from playsound import playsound

def countdown_timer(seconds):
    while seconds:
        print(f"{seconds} seconds remaining", end='\r')  
        
        time.sleep(1)
        seconds -= 1
    playsound("C:/users/shire/OneDrive/Siri's/Siri's Python/Python Folder/level-up-47165.mp3")

    print("\nTime's up!")
    

try:
    seconds = int(input("Enter the number of seconds for the countdown: "))
    countdown_timer(seconds)
except ValueError:
    print("Please enter a valid integer for the countdown time.")


