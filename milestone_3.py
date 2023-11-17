import random

def get_random_word(word):
    """Reurn a random word from the created list"""
    return random.choice(word)

def ask_for_input(user_prompt):
    """Promt the user to enter a single character"""
    while True:        
        usr_input = input(user_prompt)
        if len(usr_input) == 1 and usr_input.isalpha():
       	     return usr_input.lower()# convert to lowercase
        print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(guess, word):
    #Check if the guess is in the word
    if guess in word:
        print(f'Good Guess! {guess} is in the word.')
    else:
        print('Sorry, {guess} is not in the word. Try again.')

def main():
    #Creating a list of 5 favourite fruits
    favourite_fruits = ['Apple', 'Orange', 'Banana', 'Cheery', 'Mango']

    #Printing the created list to the screen
    print('Favourite Fruits: ',favourite_fruits)

    #Creating a random choice from the list and assign it to variable, word
    random_word = get_random_word(favourite_fruits)

    #Printing out the choice word
    print(f"Random Fruit: {random_word}")

    #Prompt the user for an input
    guess = ask_for_input('Please enter a single character: ')
    check_guess(guess,random_word.lower())

    

if __name__ == "__main__":
    main()
