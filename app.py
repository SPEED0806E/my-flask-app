from flask import Flask, render_template, request, session    # bring the Flask tool into my program   # request -> flask, requests -> API
import sqlite3
import requests

print('New flask')
print('LIVE')

app = Flask(__name__) # creating a flask application 'create my website' - turn this file in flask application and save it in a variable called app

app.secret_key = "wordmean_secret_key"

conn = sqlite3.connect("meanings.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS meanings
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT,
    meaning TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

history = []

@app.route("/", methods=["GET","POST"]) #/ represents the homepage (http://127.0.0.1.5000/)
def home():
    
    return render_template("index.html", history=history)

@app.route("/intro", methods=["GET","POST"])
def intro():


    meaning = ""
    
    if request.method == "POST":
        user_input = request.form["word"].strip().lower() # gets the value entered by the user in the form field named "word", and stores in the variable user_input

        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{user_input}"

        response = requests.get(url)

        print(response.status_code)
        print(response.text)
        # print(response.json())

        if response.status_code == 200:
            data = response.json()
            meaning = data[0]["meanings"][0]["definitions"][0]["definition"]

        else:
            meaning = "Word not found"



        print(f"{user_input} : {meaning}")
    
        history.append({
             "word":user_input,
             "meaning":meaning})
        print(history)


        cursor.execute("""
        INSERT INTO meanings (word, meaning)
        VALUES (?, ?)
        """, (user_input, meaning))

        conn.commit()
                #conn.close()

        print('Meaning added successfully !')
        
        

    return render_template("intro.html", history=history, meaning=meaning)

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (?, ?)
        """, (username, password))

        conn.commit()

        print(username)
        print(password)

        print("User created successfully !")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor.execute("""
        SELECT * FROM users WHERE username = ? AND password = ?
        """, (username, password))

        user = cursor.fetchone()

        if user:
            session["user_id"] = user[0]
            session["username"] = user[1]
            print("Login successful")
            print(session)

            return "Welcome" + ' ' + session["username"]
        else:
            print("Invalid username or password")

    return render_template("login.html")



if __name__ == '__main__':
     import os
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)