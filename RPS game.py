import random

def get_computer():
    return random.choice(["rock", "paper", "scissors"])

def winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win! "
    else:
        return "Computer wins! "

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        
        if user_choice == "exit":
            print("Thanks for playing! Goodbye! ")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue

        computer_choice = get_computer()
        print("Computer chose:" ,computer_choice)

        result = winner(user_choice, computer_choice)
        print(result + "\n")


play_game()
