from flask import Flask, render_template, request     # bring the Flask tool into my program   # request -> flask, requests -> API
import json
# import sqlite3
import requests

app = Flask(__name__) # creating a flask application 'create my website' - turn this file in flask application and save it in a variable called app
print('THIS IS MY CURRENT FLASK ')
# conn = sqlite3.connect("meanings.db", check_same_thread=False)

# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS meanings
# (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     word TEXT,
#     meaning TEXT
# )
# """)

history = []

@app.route("/", methods=["GET","POST"]) #/ represents the homepage (http://127.0.0.1.5000/)
def home():

    
    # meaning = ""

    # if request.method == "POST":
    #     user_input = request.form["word"].strip().lower() # gets the value entered by the user in the form field named "word", and stores in the variable user_input

    #     with open("02_dictionary.json", "r") as file:
    #         word = json.load(file)
    #         meaning = word.get(user_input, "word not found")
    #         history.append({"word":user_input,
    #                         "meaning":meaning})
    
    return render_template("index.html")

# @app.route("/intro", methods=["GET","POST"])
# def intro():


#     meaning = ""
    
#     if request.method == "POST":
#         user_input = request.form["word"].strip().lower() # gets the value entered by the user in the form field named "word", and stores in the variable user_input

#         url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{user_input}"
#         response = requests.get(url)
#         print("status code : ",response.status_code)
#         print(response.json())
#         data = response.json()
#         # print(data[0]["meanings"][0]["definitions"][0]["definition"])
#         api_meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
    
#         with open("02_dictionary.json", "r") as file:
#                 word = json.load(file)
#                 meaning = word.get(user_input)
#                 if meaning is None:
#                     meaning = api_meaning
#                     print("JSON meaning : ", meaning)
#                     print("API meaning : ", api_meaning)
#                 history.append({"word":user_input,
#                                 "meaning":meaning})

#                 # cursor.execute("""
#                 # INSERT INTO meanings (word, meaning)
#                 # VALUES (?, ?conn.close()

#                 print('Meaning added successfully !')
        
#                 # """, (
#                 #      user_input,
#                 #      meaning,
#                 # ))

#                 # conn.commit()
#                 #
#     return render_template("intro.html", history=history, meaning=meaning)

@app.route("/intro", methods=["GET", "POST"])
def intro():

     meaning = ""

     if request.method == "POST":
          user_input = request.form["word"].strip().lower()

          with open("02_dictionary.json", "r") as file:
               words = json.load(file)
               meaning = words.get(user_input)
               if meaning is None:
                    print("json didn't find the word.")

                    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{user_input}"
                    response = requests.get(url)
                    print("status code:", response.status_code)
                    print("response :", response.text[:200])

                    if response.status_code == 200:
                         data = response.json()
                         meaning = data[0]["meanings"][0]["definitions"][0]["definition"]

                    else:
                         meaning = "Word not found"
                         history.append({
                              "word" : user_input,
                              "meaning" : meaning
                         })

     return render_template("intro.html", meaning=meaning, history=history)




if __name__ == '__main__':
     import os
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)