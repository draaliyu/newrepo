import random

fav_fruits = ['apple','orange', 'grapes', 'cheey', 'banana']
word_list = fav_fruits
print(word_list)

#select a random fruit
word = random.choice(word_list)

#prompt user for an input
user_input = input('Please eneter a single character: ')

#check if the user input is a single character
if len(user_input) ==1:
    print('You entered:', user_input)
else:
    print('Error: Please enter only one character')
