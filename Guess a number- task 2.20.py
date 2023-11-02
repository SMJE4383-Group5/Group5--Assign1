import random

# Get an initial guess
number = random.randint(1, 100)
guess_str = input("Guess a number: ")
guess = int(guess_str)  # Convert string to number

# While the guess is within the range, keep asking
while 0 <= guess <= 100:
    if guess > number:
        print("Guessed Too High.")
    elif guess < number:
        print("Guessed Too Low.")
    else:  # Correct guess, exit the loop
        print("You guessed it. The number was:", number)
        break  # Exit the loop when the correct guess is made

    # Keep going, get the next guess
    guess_str = input("Guess a number: ")
    guess = int(guess_str)
else:
    print("You quit early, the number was:", number)
