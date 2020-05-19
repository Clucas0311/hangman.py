secret_word = "otter"
blanks = "_" * len(secret_word)

correct_letters = "otter"
# for i in range(len(secret_word)):  # Replace blanks with correctly guessed letters
if secret_word[0] in correct_letters:
  blanks = blanks[:0] + secret_word[0] + blanks[0 + 1:]
print(blanks)

if secret_word[1] in correct_letters:
  blanks = blanks[:1] + secret_word[1] + blanks[1 + 1:]
print(blanks)

if secret_word[2] in correct_letters:
  blanks = blanks[:2] + secret_word[2] + blanks[2 + 1:]
print(blanks)

if secret_word[3] in correct_letters:
  blanks = blanks[:3] + secret_word[3] + blanks[3 + 1:]
print(blanks)

if secret_word[4] in correct_letters:
  blanks = blanks[:4] + secret_word[4] + blanks[4 + 1:]
print(blanks)
