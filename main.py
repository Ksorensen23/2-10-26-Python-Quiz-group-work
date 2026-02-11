import json
import colorama import Fore


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
    score = 0

    name = input("Enter Your name\n")
    print("Welcome " + name)
    print("\n--- WELCOME TO THE IT QUIZ BATTLE ---")
    
    for q in questions:
        print("\n" + q['question'])
        for option in q['options']:
            print(option)
            
        guess = input("Your Answer (A/B/C/D): ").upper()
        
        if guess == q['answer']:
            print(Fore.GREEN + "Correct! +10 points.")
            score += 10
            print("\n Your score is:", score)
        else:
            print(Fore.RED + f"Wrong! The answer was {q['answer']}.")
            
            
    print(f"\nGame Over! Final Score: {score}")
    save_score(name, score)


    
if __name__ == "__main__":
    play_game()
