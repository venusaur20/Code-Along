import random, math

COLORS = ["R", "B", "W", "Y", "G", "P"]
ATTEMPTS = 10
CODE_LENGTH = 4


def generate_code():
    code = []
    
    for _ in range(CODE_LENGTH):
        code.append(random.choice(COLORS))
    return code

code = generate_code()

def player_guess():
    while True:
        
        guess = input("\nGuess: ").upper().split(" ")
        

        if len(guess) != CODE_LENGTH:
            print(f"Your guess must be {CODE_LENGTH} long. Try again.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invanlid color: {color}. Try again.")
                break
        else:
            break
    return guess
 

def compare(guess,code):
        correct_letter = 0
        correct_position = 0

        for letter in range(len(guess)):
            if guess[letter] in code:
                correct_letter +=1
                if guess[letter] == code[letter]:
                    correct_position += 1

        return correct_letter, correct_position

def game():
    print(f"Welcome to MASTERMIND, you have {ATTEMPTS} tries to get the code... \nThe valid colors are ", *COLORS)
    
    code = generate_code()
    for attempts in range(ATTEMPTS):
        guess = player_guess()
        correct_letter, correct_position = compare(guess,code)
        
        if correct_position == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break
        
        print(f"Correct Positions: {correct_position} | Correct Letters: {correct_letter}")

    else:
        print("You ran out of tries, the code was: ", *code)

while True:
    game()
    replay = input("Do you want to play again? ").upper()
    if "Y" in replay:
        continue
    else:
        break