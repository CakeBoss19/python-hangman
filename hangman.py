print("This here's a game of Hangman!")
print("You know the rules, try and guess the word!")
print("Each guess  ")
secret_word = input("Choose a word: ")
word_list = list(secret_word)
i = 10

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
  print(f"Guess's left: {i}")