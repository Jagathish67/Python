import random

def number_guessing_game():
    number = random.randint(1, 100) 
    attempts = 0  

    print(" Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f" Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print(" Invalid input! Please enter a number.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing! ")

number_guessing_game()
