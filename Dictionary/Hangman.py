import random

#constants
HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|   -+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|    |
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|    |
|    |
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|    |
|    |
|   |
|   |
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|    |
|    |
|   | |
|   | |
|
----------
"""
)

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("OVERUSED", "CLAM", "BIKE", "CHAIR", "PYTHON")

#Initialize Variables
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

#The main loop
print("Welcome to Hangman. Good luck!")

while wrong<MAX_WRONG and so_far!=word:
    print(HANGMAN[wrong])
    print("\n You have used the following letters:\n",used)
    print("\nSo far the word is:\n",so_far)
    #Getting the Players Guess
    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed the letter", guess)
        
        guess = input("\n\nEnter your guess: ")
        guess = guess.upper

    used.append(guess)
    #Checking the Guess
    if guess in word:
        print("\nYes!",guess,"is in the word!")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new+=guess
            else:
                new+=so_far[i]
        so_far = new
    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")
    print("\nThe word was", word)

