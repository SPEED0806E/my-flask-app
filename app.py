from flask import Flask, render_template, request     # bring the Flask tool into my program   # request -> flask, requests -> API
import json
app = Flask(__name__) # creating a flask application 'create my website' - turn this file in flask application and save it in a variable called app


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
    
    return render_template("index.html", history=history)

@app.route("/intro", methods=["GET","POST"])
def intro():

    meaning = ""
    
    if request.method == "POST":
        user_input = request.form["word"].strip().lower() # gets the value entered by the user in the form field named "word", and stores in the variable user_input
    
        with open("02_dictionary.json", "r") as file:
                word = json.load(file)
                meaning = word.get(user_input, "word not found")
                history.append({"word":user_input,
                                "meaning":meaning})
        
        

    return render_template("intro.html", history=history)




if __name__ == '__main__':
     import os
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)

