import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Keep asking until the guess is correct
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == secret_number:
        print("🎉 Correct! You guessed the number!")
        break  # Exit the loop
    else:
        print("❌ Wrong guess. Try again!")
