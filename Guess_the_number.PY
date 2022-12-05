#Number Guessing Game Objectives:
import random
from art import logo

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number=range(1,101)
choosen_number=int(random.choice(number))
level=input("Choose a difficulty. Type 'easy' or 'hard':").lower()




def easy():
    for attempts in range(1,11):
        a=11-attempts
        print(f"You have {a} attempts remaining to guess the number.")
        guess=int(input("Make a guess:").lower())
        if a==0:
            print("you are out of turns")
            return
        else:
            if guess > choosen_number:
                print("Too high.")

            elif guess == choosen_number:
                return (f"You got it! The answer was:{choosen_number}")
            else:
                print("Too low.")

def hard():
    for attempts in range(1,6):
        a=6-attempts
        print(f"You have {a} attempts remaining to guess the number.")
        guess2=int(input("Make a guess:").lower())
        if a==0:
            print("you are out of turns")
            return
        else:
            if guess2 > choosen_number:
                print("Too high.")

            elif guess2 == choosen_number:
                return (f"You got it! The answer was:{choosen_number}")
            else:
                print("Too low.")




if level=="easy":
    print(easy())
else:
    print(hard())