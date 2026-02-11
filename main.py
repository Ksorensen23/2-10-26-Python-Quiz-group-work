import json
import colorama import Fore, init
init(autoreset=True)

# 1. THE LIBRARIAN'S FUNCTION
def load_questions():
    with open('questions.json', 'r') as file:
        return json.load(file)

# Keagan work, save player score to a text file
def save_score(name, score):
    s = score
    n = name
    with open("PlayerScore.txt" , "a") as file:
        file.write("Name: " + str(n) + " " + "|" + " " + "Score: " + str(s) + "\n") 
    with open("PlyaerScore.txt") as file:
        print(file.read())

# 2. THE REFEREE'S MAIN LOOP
def play_game():
    questions = load_questions()
    p1Score = 0
    p2Score = 0
    player = 1

    print("--- WELCOME TO THE IT QUIZ BATTLE ---")
    score = 0

    name = input("Enter Your name\n")
    print("Welcome " + name)
    print("\n--- WELCOME TO THE IT QUIZ BATTLE ---")
    
    for q in questions:
        
        print("\n" + q['question'])
        for option in q['options']:
            print(option)
            
        guess = input("\nPlayer" + f" {player} " + "Answer (A/B/C/D): ").upper()
        
        if guess == q['answer']:

            # if player one, add to their score
            if player == 1:
                print(Fore.GREEN + "Correct! Player 1 +10 points.")
                p1Score += 10
                print("\n Player 1 score is:", p1Score)
                
            # if player two, add to their score
            elif player == 2:
                print(Fore.GREEN + "Correct! Player 2 +10 points.")
                p2Score += 10
                print("\n Player 2 score is:", p2Score)
                
        else:
            print(Fore.RED + f"Wrong! The answer was {q['answer']}.")
            
        # This changes which player is active
        #   it must be put here otherwise it would need to be
        #   duplicated in the correct and incorrect logic conditions
        if player == 2:
            player = 1
        elif player == 1:
            player = 2
            
    print(f"\nGame Over! Final Score: {score}")
    save_score(name, score)


    
if __name__ == "__main__":
    play_game()

