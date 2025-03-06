import time
import random

sentences = [
    "Python is fun to learn",
    "Code every day to improve",
    "Practice makes perfect",
    "Challenge yourself to grow"
]

def typing_game():
    sentence = random.choice(sentences)
    print(" Type this as fast as you can:\n")
    print(f"{sentence}\n")
    
    input("Press ENTER to start...")
    start_time = time.time()

    user_input = input("\nStart typing: ")
    end_time = time.time()

    time_taken = round(end_time - start_time, 2)

    if user_input == sentence:
        print(f"Correct! You took {time_taken} seconds.")
    else:
        print(f"Incorrect! Try again.")

    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again == "yes":
        typing_game()
    else:
        print("\nThanks for playing!")

typing_game()
