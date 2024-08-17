import random

NUM_DIGITS = 3
MAX_GUESSES = 10

INTRO_STRING = f"""Bagels, a deductive logic game.
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.
"""

def main():
    print(INTRO_STRING)

    # Game loop
    while True:
        secret_num = get_secret_num()
        print(f'I have thought up a number. You have {MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""

            # parameter check guesses
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}')
                guess = input('> ')
            
            clues = get_clues(guess, secret_num)

            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print(f'You ran out of guesses. The answer was {secret_num}.')

    
        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def get_secret_num() -> str:
    return str(random.randint(100, 999))

def get_clues(guess: str, secret_num: str) -> str:
    if guess == secret_num:
        return 'Nice job! You got it!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
        
    if len(clues) == 0:
        return 'Bagels'
    
    clues.sort()
    return ' '.join(clues)

if __name__ == '__main__':
    main()