import random
import time

def generate_sequence(length):
    return [random.randint(1, 9) for _ in range(length)]  
def memory_game():
    print("lcome to the Memory Game!")
    score = 0
    level = 1
    
    while True:
        print(f"\n🔹 Level {level}: Remember this sequence...")
        sequence = generate_sequence(level)
        print("👉"", *sequence)
        
        time.sleep(3)  
        print("\n" * 50)
        
        user_input = input("Enter the numbers in order (separate by space): ")
        user_numbers = list(map(int, user_input.split()))
        
        if user_numbers == sequence:
            print("✅ Correct! Moving to the next level...\n")
            score += 1
            level += 1
        else:
            print(f" Wrong! The correct sequence was {sequence}.")
            print(f"final Score: {score}")
            break

memory_game()
