import json
with open("02_dictionary.json", "r") as file:
    word = json.load(file) # read everything from 02_dictionary.json and convert it into a python dictionary called word.
                    # json.load() -> read the JSON file
                    # json.dump() -> save to JSON file
    print(word)

    
# with open("02_dictionary.json", "w") as file:
#     json.dump(word, file)


user_input = input('Enter a word : ').strip().lower()

if user_input in word:
    print(f'{user_input} : {word[user_input]}')

else:
    print('Word not found.')
    ask_user = input('Would you like to add a meaning (yes/no) : ').strip().lower()
    if ask_user == 'yes':
        user_meaning = input('Enter meaning : ').strip().lower()
        print(f'{user_input} : {user_meaning}')
        word[user_input] = [user_meaning]
        # print(word)
    
sorted_word = dict(sorted(word.items()))
print(sorted_word)

with open("02_dictionary.json", "w") as file:
    json.dump(word, file)

    # if ask_user == 'yes':
    #     print('Word added successfully !')
    # else:
    #     print('OK')


#sorted_word = dict(sorted(word.items()))
#print(sorted_word)
print(len(word))




# TOOK USER INPUT
# USED A PYTHON DICTIONARY
# SEARCHED FOR WORDS
# ADDED NEW WORDS
# READ DATA FROM A JSON FILE (json.load)
# SAVED THE DATA PERMANENTLY(json.dump)


