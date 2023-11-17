import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the Hangman game."""
        self._word = random.choice(word_list).lower()
        self._word_guessed = ['_' for _ in self._word]
        self._num_letters = len(set(self._word))
        self.num_lives = num_lives
        self._list_of_guesses = []

    def _update_word_guessed(self, guess):
        """Update the word guessed list with the correct guess."""
        for i, letter in enumerate(self._word):
            if letter == guess:
                self._word_guessed[i] = guess

    def check_guess(self, guess):
        """Check if the guess is in the word and update the game state."""
        guess = guess.lower()
        if guess in self._word:
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
            self._num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """Prompt the user for a guess and process it."""
        while True:
            guess = input("Guess a letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self._list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self._list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost! The word was:", game._word)
            break
        elif game._num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

# Test the game
word_list =['Apple', 'Banana', 'Cherry', 'Orange', 'Mango']
play_game(word_list)

