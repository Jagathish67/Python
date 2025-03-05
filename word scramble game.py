import random
import time

words = ["python", "coding", "developer", "program", "challenge"]

def scramble(word):
    return "".join(random.sample(word, len(word)))  

def word_scramble_game():
    score = 0
    print(" Welcome to the Word Scramble Game with Hints!")

    for i in range(3):
        word = random.choice(words)
        scrambled = scramble(word)
        print(f" Unscramble this word: {scrambled}")

        start_time = time.time()
        hint_given = False
        guess = None
            
        guess = input("Your answer: ").lower()
        """if guess:  
            break"""  

        if not guess:  
                print(f"Time's up! The correct word was '{word}'.\n")
        elif guess == word:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct word was '{word}'.\n")

    print(f" Game Over! Your final score: {score}/3")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "yes":
        word_scramble_game()
    else:
        print("\nThanks for playing! ")

word_scramble_game()
