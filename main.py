"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Pavel Nováček
email: gippel@seznam.cz
"""

import random

# Funkce
def number_generator() -> list:
    '''
    Generates random 4 digit number which cant begin with "0".
    \nReturns list of strings.
    '''
    number = []
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while True:
        number = random.sample(digits, 4)
        if number[0] == "0":
            continue
        else:
            return number
            
def duplicity_check(number: list) -> bool:
    '''
    Checks duplicite digits in a number.
    '''
    digits = set()
    for digit in number:
        if digit in digits:
            return False   
        digits.add(digit) 
    return True

def bulls_and_cows(number_1:list, number_2:list) -> str:
    '''
    Checks how many digits from the number_2 
    are in the number_1 
    and are at the same position. (bull_count)
    or checks how many digits from the number_2 
    are in the number_1 (cow_count).
    Args:
        number_1 = ["1", "2", "3", "4"]
        number_2 = ["1", "2", "5", "6"]

    Returns: 
        2 bulls, 2 cows
    '''
    count = 0
    bull_count = 0
    cow_count = 0
    for digit in number_2:
        if digit in number_1 and number_2[count] == number_1[count]:
            bull_count +=1
        elif digit in number_1:
            cow_count += 1
        count += 1    
    if bull_count == 1 and cow_count == 1:
        return "1 bull, 1 cow"
    elif bull_count == 1 and cow_count != 1:
        return f"1 bull, {cow_count} cows"
    elif bull_count != 1 and cow_count == 1:
        return f"{bull_count} bulls, 1 cow"
    else:
        return f"{bull_count} bulls, {cow_count} cows"
                    
# Pozdravení uživatele
print("Hi there",
      "-" * 47,
      "I've generated a random 4 digit number for you.",
      "Let's play a bulls and cows game.",
      "-" * 47,
      sep="\n"
    )

# Generace náhodného čísla
number = number_generator()

# Vstup uživatele a jeho kontrola vůči vygenerovanému číslu
guess_count = 0

while True:
    player_guess = input("Enter a number: ")
    if player_guess.isdigit() is False:
        print("Invalid input.")
        continue
    elif len(player_guess) < 4:
        print("Number is too short.")
        continue
    elif len(player_guess) > 4:
        print("Number is too long.")
        continue
    elif player_guess[0] == "0":
        print("First digit can not be 0.")
        continue
    elif duplicity_check(player_guess) == False:
        print("Duplicite digits not allowed")
        continue
    else:
        guess_count += 1
        if list(player_guess) == number:
            print(">>> " + player_guess,
                "Correct, you've guessed the right number",
                "in " + str(guess_count) + " guesses!",
                "-" * 47,
                sep="\n"
                )
            break
        else:
            print(">>> " + player_guess,
                bulls_and_cows(number, player_guess),
                "-" * 47,
                sep="\n"
                )
    
    
        
        
