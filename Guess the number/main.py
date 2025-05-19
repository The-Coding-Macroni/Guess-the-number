import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I am thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # Generate a random number
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.\n")
            elif guess > number_to_guess:
                print("Too high! Try again.\n")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.\n")

if __name__ == "__main__":
    guess_the_number()