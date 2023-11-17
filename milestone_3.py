import random

def get_random_word(words):
    """Return a random word from the list."""
    return random.choice(words).lower()

def check_guess(guess, word):
    """Check if the guess is in the word, converting the guess to lowercase."""
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(prompt, word):
    """Prompt the user for a single alphabetical character and check the guess."""
    while True:
        user_input = input(prompt)
        if len(user_input) == 1 and user_input.isalpha():
            check_guess(user_input, word)
            break
        else:
            print("Oops! That is not a valid input.")

def main():
    favorite_fruits = ['Apple', 'Banana', 'Cherry', 'Orange', 'Mango']
    print("Favorite Fruits:", favorite_fruits)

    random_word = get_random_word(favorite_fruits)
    print(f"Random Fruit: {random_word}")  # Optional: for debugging or display.

    ask_for_input("Please enter a single character: ", random_word)

if __name__ == "__main__":
    main()
