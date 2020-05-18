import random
HANGMAN_PICS = ["""
  +---+
  |   |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
      |
      |
      |
==========""", """
  +---+
  |   |
  O   |
  |   |
  |   |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote \
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard \
llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python \
rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider \
stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
# Use split method to split large string into multiple little strings

def get_random_word(word_list):
    # This function returns a random string from the passed list of strings
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

def display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)]) # prints hangman board at the
    # index of the length of the missed letters
    print()

    print("Letters missed:", end= ' ') # Display the letters the user missed
    for letter in missed_letters:
        print(letter, end= ' ')
        print()

    blanks = "_" * len(secret_word) # Display the secret word with blanks

    for i in range(len(secret_word)): # Replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks: # Displays secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def get_guess(already_guessed):
    # Returns the letter the player entered. This function ensures the user
    # enters a single letter and doesn't duplicate the letter they chose
    while True: # Loop will keep asking the player for a letter until
        # they enter a letter that hasn't already been guessed
        guess = input("Guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1: # if guess is not a single letter
            print("Please enter a single letter.")
        elif guess in already_guessed: # if letter has already been guesssed
            print("Come on! You've already guessed that letter please \
try again: ")
        elif guess.isalpha() == False: # Checks for alpha letter
            print("Please enter a LETTER")
        else:
            return guess # if all the conditions are false then the else
            # statement executes and returns the value of the guess letter

def play_again(): # This function returns True if the player wants to
#play again; if not it will return False
    plays = input("Do you want to play again? (yes or no): ")
    return plays.lower().startswith('y') # Make sure that user input is
    # lower case and starts with the letter "y"

print("Lets play H A N G M A N") # Game title
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words) # selects random words from list
game_is_done = False

while True:
    display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)

    # Let the player enter a letter
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word: # checks to see if letter is in secret word
        correct_letters = correct_letters + guess

        # Check to see if the player has won
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Yes! the secret word is "' + secret_word +
'"! You have won')
            game_is_done = True
    else:
        missed_letters = missed_letters + guess # if user guesses incorrectly

        # Check to see if player has guessed too many times and lost.
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
            print('You have run out of guesses!\nAfter ' +
str(len(missed_letters)) + ' missed gusses and ' + str(len(correct_letters))
+ ' correct guesses, the word was "' + secret_word + '"')
            game_is_done = True
# Ask the player to play again if the game is done
    if game_is_done:
        if play_again(): # if player chooses yes everything must reset
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break
