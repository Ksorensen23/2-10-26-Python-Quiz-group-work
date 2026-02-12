import json
import os
import time

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# 1. THE LIBRARIAN'S FUNCTION


def load_questions():
    try:
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "questions.json")

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(RED + "Error: questions.json not found." + RESET)
        return []
# Keagan work, save player score to a text file
def save_score(name, score1, name2, score2):
    s = score1
    n = name
    s2 = score2
    n2 = name2
    with open("PlayerScore.txt" , "a") as file:
        file.write("Player 1: " + str(n) + " " + "," + " " + "Score: " + str(s) + "|" + "Player 2: " + str(n2) + " " + "," + " " + "Score: " + str(s2) + "\n")
        file.close()

# 2. THE REFEREE'S MAIN LOOP
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game():
    questions = load_questions()
    score1 = 0
    score2 = 0
    player = 1

    name = input("Enter Name 1\n")
    name2 = input("Enter Name 2\n")

    ASCII_ART1 = r'''
        _____________
       | ___________ |
       ||.---------.||
       |||         |||
       |||         |||
       |||         |||
       ||'---------' |
       | """"""""""` |
       | ||  ^^^  () |
       |[  ]    ()   |
       | ||          |
       |     _ _     |
       |          :::|
       |         .::'|
       ---------------
    '''

    print("Welcome " + name + " and " + name2)
    print("\n--- WELCOME TO THE IT QUIZ BATTLE ---")
    print(BLUE + ASCII_ART1 + RESET)

    
    for q in questions:
        
        time.sleep(3)
        clear_screen()

        #displays who's turn it is
        if player==1:
            print(f"\n{name}'s turn!")
        elif player==2:
            print(f"\n{name2}'s turn!")
            
        print("\n" + q['question'])
        for option in q['options']:
            print(option)
            
        guess = input(f"\nAnswer (A/B/C/D): ").upper()
        
        if guess == q['answer']:

            # if player one, add to their score
            if player == 1:
                print(GREEN + "Correct! Player 1 +10 points." + RESET)
                score1 += 10
                print("\n Player 1 score is:", score1)
                
            # if player two, add to their score
            elif player == 2:
                print(GREEN + "Correct! Player 2 +10 points." + RESET)
                score2 += 10
                print("\n Player 2 score is:", score2)
                
        else:
            print(RED + f"Wrong! The answer was {q['answer']}." + RESET)
            
        # This changes which player is active
        #   it must be put here otherwise it would need to be
        #   duplicated in the correct and incorrect logic conditions
        if player == 2:
            player = 1
        elif player == 1:
            player = 2
            
    print(f"\nGame Over! Final Scores: \n\n{name} - {score1} Points\n{name2} - {score2} Points")
    # Save the total score for this game session

    save_score(name, score1, name2, score2)

    
if __name__ == "__main__":
    play_game()

