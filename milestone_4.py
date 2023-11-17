import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """Check if the guess is in the word."""
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")


    def ask_for_input(self):
    
        while True:
            
            guess = input('Guess a letter: ').lower()
            if not guess.isalpha() and len(guess) != 1:
                print('Invalid letter. Please, enter a single aphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

#Test the code
if __name__ == '__main__':
    favourite_fruits = ['Apple', 'Banana', 'Cherry', 'Orange', 'Mango']
    game = Hangman(favourite_fruits)
    game.ask_for_input()
