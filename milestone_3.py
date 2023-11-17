import random

def get_random_word(words):
    """Return a random word from the list."""
    return random.choice(words).lower()

def prompt_user_for_guess(prompt, word):
    """Prompt the user for a single alphabetical character and check the guess."""
    while True:
        try:
            user_input = input(prompt).strip()
            if len(user_input) == 1 and user_input.isalpha():
                check_guess(user_input.lower(), word)
                break
            else:
                print("Oops! Please enter a single alphabetical character.")
        except Exception as e:
            print(f"An error occurred: {e}")

def check_guess(guess, word):
    """Check if the guess is in the word."""
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def main():
    favorite_fruits = ['Apple', 'Banana', 'Cherry', 'Orange', 'Mango']
    print("Favorite Fruits:", favorite_fruits)

    random_word = get_random_word(favorite_fruits)
    print(f"Random Fruit: {random_word}")

    prompt_user_for_guess("Please enter a single character: ", random_word)

if __name__ == "__main__":
    main()
