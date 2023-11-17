import random

def get_random_word(word):
    """Reurn a random word from the created list"""
    return random.choice(word)

def get_single_character_input(user_prompt):
    """Promt the user to enter a single character"""
    usr_input = input(user_prompt)
    if len(usr_input) == 1 and usr_input.isalpha():
        print('Good Guess!')
    else:
        print("Oops! That is not a valid input.")

def main():
    #Creating a list of 5 favourite fruits
    favourite_fruits = ['Apple', 'Orange', 'Banana', 'Cheery', 'Mango']

    #Printing the created list to the screen
    print(favourite_fruits)

    #Creating a random choice from the list and assign it to variable, word
    random_word = get_random_word(favourite_fruits)

    #Printing out the choice word
    print(f"Random Fruit: {random_word}")

    #Prompt the user for an input
    guess = get_single_character_input('Please enter an input: ')
    

if __name__ == "__main__":
    main()
