import json

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

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
    with open("PlayerScore.txt") as file:
        print(file.read())

# 2. THE REFEREE'S MAIN LOOP
def play_game():
    questions = load_questions()
    p1Score = 0
    p2Score = 0
    player = 1
    
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
                print(GREEN + "Correct! Player 1 +10 points." + RESET)
                p1Score += 10
                print("\n Player 1 score is:", p1Score)
                
            # if player two, add to their score
            elif player == 2:
                print(GREEN + "Correct! Player 2 +10 points." + RESET)
                p2Score += 10
                print("\n Player 2 score is:", p2Score)
                
        else:
            print(RED + f"Wrong! The answer was {q['answer']}." + RESET)
            
        # This changes which player is active
        #   it must be put here otherwise it would need to be
        #   duplicated in the correct and incorrect logic conditions
        if player == 2:
            player = 1
        elif player == 1:
            player = 2
            
    print(f"\nGame Over! Final Scores: \n\nPlayer 1 - {p1Score} Points\nPlayer 2 - {p2Score} Points")
    # Save the total score for this game session
    total_score = p1Score + p2Score
    save_score(name, total_score)


    
if __name__ == "__main__":
    play_game()

