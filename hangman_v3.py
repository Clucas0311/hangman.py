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
=========""", """
 +---+
 |   |
[O  |
/|\  |
/ \  |
     |
=========""", """
+---+
|   |
[O]  |
/|\  |
/ \  |
    |
========="""]

words = {'Colors': 'red orange yellow green blue indigo violet white black brown'.split(), \
'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon heptagon octagon'.split(),\
'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(), \
'Animals': 'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

# Use split method to split large string into multiple little strings


def get_random_word(words_dict):
    # This function returns a random string from the dictionary list of strings and its keys
    # First randomly select a key from the dictionary
    word_key = random.choice(list(words_dict.keys()))
    # Secondly randomly select a word from the key's list in the dictionary:
    word_index = random.randint(0, len(words_dict[word_key]) - 1)

    return [words_dict[word_key][word_index], word_key] # So whatever index random generator chooses a word will be created


def display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])  # prints hangman board at the
    # index of the length of the missed letters
    print()

    print("Letters missed:", end=' ')  # Display the letters the user missed
    for letter in missed_letters:
        print(letter, end=' ')
        print()

    blanks = "_" * len(secret_word)  # Display the secret word with blanks

    for i in range(
            len(secret_word)):  # Replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:  # Displays secret word with spaces in between each letter
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    # Returns the letter the player entered. This function ensures the user
    # enters a single letter and doesn't duplicate the letter they chose
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
            return guess  # if all the conditions are false then the else
            # statement executes and returns the value of the guess letter


def play_again():  # This function returns True if the player wants to
    # play again; if not it will return False
    plays = input("Do you want to play again? (yes or no): ")
    return plays.lower().startswith('y')  # Make sure that user input is
    # lower case and starts with the letter "y"


print("Lets play H A N G M A N")  # Game title
# Makes the board hard based on user choice deletes board based on user selection
difficulty = input('Enter difficulty: E - Easy, M - Medium, H - Hard: ' )
difficulty = difficulty.upper()
while difficulty not in 'EMH':
    if difficulty == 'M':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
    if difficulty == 'H':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[5]
        del HANGMAN_PICS[3]

missed_letters = ''
correct_letters = ''
secret_word, secret_set = get_random_word(words)  # selects random words from list
game_is_done = False

while True:
    print(' The secret word is in the set: ' + secret_set)
    display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)

    # Let the player enter a letter
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:  # checks to see if letter is in secret word
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
        missed_letters = missed_letters + guess  # if user guesses incorrectly

        # Check to see if player has guessed too many times and lost.
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(
                HANGMAN_PICS,
                missed_letters,
                correct_letters,
                secret_word)
            print('You have run out of guesses!\nAfter ' +
                  str(len(missed_letters)) +
                  ' missed gusses and ' +
                  str(len(correct_letters)) +
                  ' correct guesses, the word was "' +
                  secret_word +
                  '"')
            game_is_done = True
# Ask the player to play again if the game is done
    if game_is_done:
        if play_again():  # if player chooses yes everything must reset
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word, secret_set = get_random_word(words)
        else:
            break
