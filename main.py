import json

# 1. THE LIBRARIAN'S FUNCTION
def load_questions():
    with open('questions.json', 'r') as file:
        return json.load(file)

# 2. THE REFEREE'S MAIN LOOP
def play_game():
    questions = load_questions()
    p1Score = 0
    p2Score = 0
    
    print("--- WELCOME TO THE IT QUIZ BATTLE ---")
    
    for q in questions:
        print("\n" + q['question'])
        for option in q['options']:
            print(option)
            
        guess = input("\nYour Answer (A/B/C/D): ").upper()
        
        if guess == q['answer']:
            
            if q % 2 == 0:
                print("Correct! Player 1 +10 points.")
                p1Score += 10

            elif q % 2 != 0:
                print("Correct! Player 2 +10 points.")
                p2Score += 10
                
        else:
            print(f"Wrong! The answer was {q['answer']}.")
            
    print(f"\nGame Over! Final Scores:\n\n Player 1 - {p1Score}\n\nPlayer 2 - {p2Score}")

if __name__ == "__main__":
    play_game()

