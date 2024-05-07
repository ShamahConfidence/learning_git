import random

def play_game():
    number = random.randint(1, 50)
    attempts = 0
    
    
    print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number b/n 1 and 50")
    
    while True:
        guess  = int(input("Take a guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")