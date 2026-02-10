import json
from colorama import Fore

# 1. THE LIBRARIAN'S FUNCTION
def load_questions():
    with open('questions.json', 'r') as file:
        return json.load(file)

# 2. THE REFEREE'S MAIN LOOP
def play_game():
    questions = load_questions()
    score = 0
    
    print("--- WELCOME TO THE IT QUIZ BATTLE ---")
    
    for q in questions:
        print("\n" + q['question'])
        for option in q['options']:
            print(option)
            
        guess = input("Your Answer (A/B/C/D): ").upper()
        
        if guess == q['answer']:
            print(Fore.GREEN + "Correct! +10 points.")
            score += 10
        else:
            print(Fore.RED + f"Wrong! The answer was {q['answer']}.")
            
    print(f"\nGame Over! Final Score: {score}")

if __name__ == "__main__":
    play_game()
