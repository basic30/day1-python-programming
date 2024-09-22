import random

def guess_the_number():
    print("Welcome to 'Guess the Secret Number'!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            
            guess = int(input("Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            
            attempts += 1 
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

guess_the_number()
