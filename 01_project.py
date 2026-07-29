# user_input = input('Enter the word to get its meaning : ')

# word = ['star', 'unknown', 'astronaut', 'space']

# if user_input == word[0]:
#     print(f' star : A huge bright object in space.')
# elif user_input == word[1]:
#     print(f' unknown : Something that is not known.')
# elif user_input == word[2]:
#     print(f' astronaut : Man in space.')
# elif user_input == word[3]:
#     print(f' space : A vast empty cosmos outside Earth.')
# else:
#     print('Word not found')



# 2nd attempt

# user_input = input('Enter the word to get its meaning : ')

# word = {
#         'star' : 'a huge bright object in space',
#         'unknown' : 'something that is not known',
#         'astronaut' : 'man in space',
#         'space' : 'an empty cosmos'
# }

# if user_input == 'star':
#     print(word['star'])
# elif user_input == 'unknown':
#     print(word['unknown'])
# elif user_input == 'astronaut':
#     print(word['astronaut'])
# elif user_input == 'space':
#     print(word['space'])
# else:
#     print('word not found')



# attempt 3 removing all the if elif else line to maket the code shorter and myself smarter engineer

user_input = input('Enter the word to get its meaning : ')

word = {
         'star' : 'a huge bright object in space',
         'unknown' : 'something that is not known',
         'astronaut' : 'man in space',
         'space' : 'an empty cosmos',
         'absolutism' : 'truth exists independently of human perception',
         'astrophysics' : 'physics of stars and space bodies',
         'axiom' : 'statement accepted as true without proof',
         'celestial' : 'relating to sky or deep space',
         'cosmology' : 'study of the universe\'s\' origin',
         'epistemology' : 'philosophical study of human knowledge',
         'essence' : 'core identity or fundamental nature',
         'existentialism' : 'philosophy emphasizing individual human freedom',
         'galaxy' : 'massive system of bound stars',
         'metaphysics' : 'study of nature of reality',
         'quantum' : 'smallest unit of physical energy',
         'spacetime' : 'fusion of space and time',
         'universe' : 'all existing matter and space',
         'wormhole' : 'hypothetical cosmic shortcut through spacetime'
}

if user_input in word:
    print(f'{user_input} : {word[user_input]}')

else:
    print('word not found')
    choice = input('Would you like to add it ? yes/no : ')
    if choice == 'yes':
        # word = {}
        # add = (f'{user_input}')
        # meaning = input('Enter the meaning : ')
        # word[add] = meaning
        # print(word)
        user_add = input('Enter the meaning : ')
        print(f'{user_add}')
        word[user_input] = user_add # to add a new key : value pair in dictionary
        print('word added successfully')
        print(word)

    else:
        print('ok')