name1 = input("What is first player name: ")
name2 = input("What is second player name: ")

score1 = 0
score2 = 0

current_chooser = name1
current_guesser = name2

while score1 < 3 and score2 < 3:
    print(f"\nCURRENT SCORE: {name1}: {score1} | {name2}: {score2}")
    print(f"ROUND START: {current_chooser} picks, {current_guesser} guesses.")
    
    target = int(input(f"{current_chooser}, enter the secret number: "))
    print("\n" * 50) 
    
    guess = 0
    tries = 0  
    round_won = False 

    while guess != target and tries < 5:
        tries += 1
        guess = int(input(f"Attempt {tries}/5 - {current_guesser}, enter guess: "))
        
        if guess == target:
            print(f"BRAVO {current_guesser}! You got it.")
            round_won = True
            if current_guesser == name1:
                score1 += 1
            else:
                score2 += 1
        elif tries == 5:
            print(f"OUT OF TRIES! The number was {target}.")
        else:
            print(f"Wrong! {5 - tries} tries left.")

    # --- THE FIX: SWAP ROLES FOR THE NEXT ROUND ---
    if current_chooser == name1:
        current_chooser = name2
        current_guesser = name1
    else:
        current_chooser = name1
        current_guesser = name2

print("\n--- MATCH OVER ---")
if score1 == 3:
    print(f"THE GRAND WINNER IS {name1}!")
else:
    print(f"THE GRAND WINNER IS {name2}!")