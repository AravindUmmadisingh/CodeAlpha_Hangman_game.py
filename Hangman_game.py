import random
free colorama import init

def main():
    init()

print("Welcome to Hangman!\n You must try to guess the given word letter before you run out of your six attempts.\n A correct guess done not use up your attempts.")

print("******Good Luck!******")

play_again = True

while play_again:
     words = ["aravind", "lordganesha", "lordhanuman", "Vishnu", "Shiva"]

     chosen_word = random.choice(words).lower()
     player_guess = None
     guessed_letters = []
     word_guessed = []
     for letter in chosen_word:
         word_guessed.append("-")
      joined_word = None

      attempts = 6

     while (attempts != 0 and "-" in word_guessed):
         print(("\033[1;31m\n\nAttempts Remaining:
  {}").format(attempts))
          joined_word = "".join(word_guessed)
          print("\033[1;34mWord: " + joined_word)

          try:
              player_guess = str(input("\033[1;37m\nType in a letter: ")).lower()
          except:
               print("That is not valid input. Please try again.")

                continue 
          else:
               if not player_guess.isalpha():
                  print("That is not a letter. Please try again.")

                  continue 
          elif len(player_guess) > 1:
               print("That is more than one letter. Please try again.")

               continue 
          elif player_guess in guessed_letters:
               print("You have already guessed that letter. Please try again.")
               continue 
          else:
              pass

          guessed_letters.append(player_guess)

          for letter in range(len(chosen_word)):
             if player_guess == chosen_word[letter]:
                 word_guessed[letter] = player_guess

             if player_guess not in chosen_word:
                 attempts -= 1

        if "-" not in word_guessed:

  print(("\n\033[1;4m\033[1;32mCongratulations\033[0m\033[1;37m! You guessed the word, {}").format(chosen_word))

        else:
              print(("\n\033[1;4m\033[1;31mYou lose\033[0m\033[1;37m! The word was {}.").format(chosen_word))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y", "yeah", "yep", "1", "ok"):
             play_again = False
             exit()

print("\nThank you for playing!")

if __name__ = "__main__":
     main()

raw_input()
          
