#imported random library so words can be selected at random
import random
#imported word list so that word list can be used in the hangman game
from words import word_list

#Create a function for the words imported from the word list so that the game can have words generated from random
def get_word():
	word = random.choice(word_list)
	#Returns all words in upper case, easier flow
	return word.upper()

#Create a function for the game play that takes in the word varible
def play(word):
	#Represent the unguessed letter as underscore by multiplying underscores by the length of the word
	#This will create the underscore line so the user knows how many letters are in each word 
	word_completion = "_" * len(word)
	#Conditonal used for the while loop 
	guessed = False
	#create two list one for guessed letters and words - this will hold both the letters and words the user guesses 
	guessed_letters = []
	guessed_words = []
	#Create a variabe for the body parts that will be taken away from the tries function created. Based on the users incorrect guesses
	#The body has 6 parts head, two arms, two legs, and body = to six body parts
	tries = 6  
	#Print out guidelines to help the user for gameplay
	print("Hey, Let's play Hangman!!")
	#Need to display the intial hangman body for the beginning of game
	print(display_hangman(tries))
	#Need to display the intital state of the word with all underscores 
	print(word_completion)
	print("\n")

	#We need to create a while loop, and it will run until either the word is guessed or the user runs out of tries
	while not guessed and tries > 0: 
		#Since each go around of the loop corresponds to a turn for the user
		#We will need to prompt the user to guess either a letter or a word:
		#Store that guess into a variable and make sure to change it to all uppercase for consistency 
		guess = input("Please guess a letter or a word: ").upper()

		#Inside the loop we will have three different condtional branches each depends on what the user inputs:
		#User guesses a letter - they must only guess one letter and the letter has to be alphabetical
		if len(guess) == 1 and guess.isalpha(): 
			#Create another conditional block to check if the letter has been already guessed
			if guess in guessed_letters: 
				print("You already guessed that letter.", guess)
				#Or letter is not in the word
			elif guess not in word: 
				print(guess, "is not in the word.")
				#Since the user made an incorrect guess, the amount of tries is subtracted
				tries -= 1
				guessed_letters.append(guess)
				
			#User made a correct guessed letter
			else: 
				print("Great job ", guess, "is in the word")
				#Add the amount of guess letters to the guess list
				guessed_letters.append(guess)
				#Change the variable word completion from a string to a list so we are able to index into it:
				word_as_list = list(word_completion)
				#Find all the indices where guess occurs in the word:
				indices = [i for i, letter in enumerate(word) if letter == guess]
				for index in indices: 
					word_as_list[index] = guess
				word_completion = "".join(word_as_list)
				if "_" not in word_completion:
					guessed == True
				
		#User guesses word 
		elif len(guess) == len(word) and guess.isalpha():
			#Condtional if user guesses the same word twice
			if guess in guessed_words:
				print("You already guessed the word", guess)
			#If Guess is not in the word then decrease the number of tries by 1 
			elif guess != word:
				tries -= 1
				#Add guess to the guessed words list 
				guessed_words.append(guess)
			#If the user correctly guesses the word
			else: 
				guessed = True
				word_completion = word


		#Create and else statement for any choice that isn't a word or letter
		else: 
			print("Not a valid guess.")
		#After each guessed is handled reprint the current state of the hangman and the amount of words left over
		print(display_hangman(tries))
		print(word_completion)
		print("\n")
		#Check to see if the user guesses the word correctly or they ran out of tries?
	if guessed:
		print("Congrats you guessed the word! You WIN!!")
	else: 
		print(f"Sorry you ran out of tries. The word was {word}. Maybe next time!" )


def display_hangman(tries): 
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # head, and torso
                """
                   
                    --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, both arms, and one leg
                """
                  
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # initial full body state
                """
                --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   
                """
    ]
    return stages[tries]

#Create a main function to run the game
def main():
	word = get_word()
	play(word)
	#Create a loop for the user to play more than once 
	while input("Play Again? (Y/N) ").upper() == "Y":
		word = get_word()
		play(word)

#To run script on command line
if __name__ == "__main__":
	  main()



