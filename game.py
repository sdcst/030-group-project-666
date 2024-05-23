import random

tries, index = 10, 0
words = ["pizza", "banana", "poopoo", "griddy", "program", "money", 
 "python", "coding", "school", "books", "word", "list", 
 "guess", "letter"]
chosenWord = words[random.randint(0, len(words) - 1)]
guess, guessString = "", ""
letters = list(chosenWord)
ans = ["_"] * len(chosenWord)
while tries != 0 or guess != chosenWord:
  guess = input("Guess a letter: ")
  if guess in letters:
      for index, letter in enumerate(letters):
        if letter == guess:
            ans[index] = guess
            guessString = "".join(ans)
  elif ans == letters:
    print("You guessed the word!")
    break
  tries -= 1
  print("Current words:", ans)
  print("You have", tries, "trie(s) left")
  print()
  if tries == 0:
    print("You lost!")
    print("The word was", chosenWord)
    break