import random

fav_fruits = ['apple','orange', 'grapes', 'cheey', 'banana']
word_list = fav_fruits
print(word_list)


word = random.choice(word_list)


user_input = input('Please eneter a single character: ')

if len(user_input) ==1:
    print('You entered:', user_input)
else:
    print('Error: Please enter only one character')
