already_guessed = "ijklm"
while True:  # Loop will keep asking the player for a letter until
        # they enter a letter that hasn't already been guessed
        guess = input("Guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1:  # if guess is not a single letter
            print("Please enter a single letter.")
        elif guess in already_guessed:  # if letter has already been guesssed
            print("Come on! You've already guessed that letter please \
try again: ")
        elif guess.isalpha() == False:  # Checks for alpha letter
            print("Please enter a LETTER")
        else:
            print(guess)  # if all the conditions are false then the else
            # statement executes and returns the value of the guess letter
