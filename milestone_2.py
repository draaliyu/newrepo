import random

def get_random_word(word):
    """Reurn a random word from the created list"""
    return random.choice(word)

def get_single_character_input(user_prompt):
    """Promt the user to enter a single character"""
    while True:        
        usr_input = input(user_prompt)
        if len(usr_input) == 1 and usr_input.isalpha():
       	     return usr_input
        print("Oops! That is not a valid input.")

def main():
    #Creating a list of 5 favourite fruits
    favourite_fruits = ['Apple', 'Orange', 'Banana', 'Cheery', 'Mango']

    #Assigning the list to a variable, word_list
    word_list= favourite_fruits

    #Printing the created list to the screen
    print(word_list)

    #Creating a random choice from the list and assign it to variable, word
    word = get_random_word(word_list)

    #Printing out the choice word
    print(f"Random Fruit: {word}")

    #Prompt the user for an input
    guess = get_single_character_input('Please enter an input: ')
    print('Good Guess!')

if __name__ == "__main__":
    main()
