import random
words_with_hints = {
    "python": "A popular programming language ",
    "developer": "A person who writes code ",
    "hangman": "A classic word-guessing game ",
    "astronaut": "A person who travels to space ",
    "rainbow": "A colorful arc seen after rain ",
    "giraffe": "The tallest animal in the world ",
    "library": "A place full of books ",
    "dolphin": "A highly intelligent sea creature ",
    "victory": "Winning a competition ",
    "journey": "A long trip or adventure "
}

def choose_word():
    word, hint = random.choice(list(words_with_hints.items()))
    return word, hint

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    print(" Welcome to Hangman!")

    mode = input("\nChoose mode: 1 Single Player | 2 Multiplayer (Enter 1 or 2): ")
    player_scores = {"Player 1": 0, "Player 2": 0}
    multiplayer = mode == "2"

    while True:
        word, hint = choose_word()
        guessed_letters = set()
        attempts = 6
        wrong_guesses = 0
        current_player = "Player 1"

        while attempts > 0:
            print(f" {current_player}'s Turn!")
            print(f" Hint: {hint}")
            print("Word:", display_word(word, guessed_letters))
            print(f"Attempts left: {attempts}")
            
            

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input! Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue
            
            guessed_letters.add(guess)

            if guess in word:
                print("Good guess!")
                if all(letter in guessed_letters for letter in word):
                    print(f"{current_player} wins! The word was: {word}")
                    player_scores[current_player] += 1  
                    break
            else:
                print(" Wrong guess!")
                attempts -= 1
                wrong_guesses += 1 
            if multiplayer:
                current_player = "Player 2" if current_player == "Player 1" else "Player 1"

        else:
            print(" Game Over! The correct word was:", word)

        print(" Scores:")
        for player, score in player_scores.items():
            print(f"{player}: {score} points")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! ")
            break 

play_hangman()
