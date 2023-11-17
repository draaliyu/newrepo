import random

#creating a list of 5 favourite fruits
favourite_fruits = ['Apple', 'Orange', 'Banana', 'Cheery', 'Mango']

#Assigning the list to a variable, word_list
word_list= favourite_fruits

#Printing the created list to the screen
print(word_list)

#Creating a random choice from the list and assign it to variable, word
word = random.choice(word_list)

#Printing out the choice word
print(word)

#Prompt the user for an input
guess = input('Please enter an input: ')

#Check that the user input is a single character
if len(guess) == 1 and guess.isalpha():
    print('Good Guess!')
else:
    print('Oops! This is not a valid input.')

