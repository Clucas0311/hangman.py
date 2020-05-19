import random
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote \
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard \
llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python \
rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider \
stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

word_index = random.randint(0, len(words) - 1)
print(words[63])
#Create a random generator for the word list
# It is zero based meaning you have to subtract the total words by 1
# The variable name is words_index so every time the the randint pics a number from that particular index it will show.

# def get_random_word(word_list):
#     # This function returns a random string from the passed list of strings
#     word_index = random.randint(0, len(word_list) - 1)
#     return word_list[word_index]
# wordy = get_random_word(words)
# print(wordy)
