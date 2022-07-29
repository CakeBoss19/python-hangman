from randomize import randomize
print("This here's a game of Hangman!")
print("You know the rules, try and guess the word!")
print("Each guess will cost you 1 try!")

secret_word = randomize()
word_list = list(secret_word)
i = 20
print(f"The secret word is {len(word_list)} characters long")
def letter_guess(player_guess): 
  for letter in word_list:
    if player_guess == letter:
      word_list.remove(letter)

while i > 0:
  if bool(word_list) == False:
    print('Game over! You won!')
    break
  else:
    player_guess = input('Guess a letter: ')
    letter_guess(player_guess)
  i = i - 1
  print(f"Trys left: {i}")