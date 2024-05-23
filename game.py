import random
def chooseword():
  tries, index = 10, 0
  words = ["pizza", "banana", "poopoo", "griddy", "program", "money", 
  "python", "coding", "school", "books", "word", "list", 
  "guess", "letter"]
  chosenWord = words[random.randint(0, len(words) - 1)]
  guess, guessString = "", ""
  letters = list(chosenWord)
  ans = ["_"] * len(chosenWord)
  while tries > 0 or guess != chosenWord:
    guess = input("Guess a letter: ").strip().lower()
    if guess in letters:
      for index, letter in enumerate(letters):
        if letter == guess:
            ans[index] = guess
            guessString = "".join(ans)
      if ans == letters:
        print(f"You guessed the word! The word was {guessString}")
        break
    tries -= 1
    if tries >= 0:
      print("Current letters:", ans)
      print("You have", tries, "trie(s) left")
      print()
    elif tries < 0:
      print("You lost!")
      print("The word was", chosenWord)
      break
    
if __name__ == "__main__":
  chooseword()