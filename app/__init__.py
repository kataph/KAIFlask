from flask import Flask, render_template, request
import os 
import app.backend.mainbu as mainbu
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + "\\app")
import backend
import random


backend.generate_files()
first_access = True

app = Flask(__name__)
@app.route("/")
def hello():
    global first_access
    
    print("first access value %s" %first_access)
    if first_access==True:
        return render_template('homepage.html', full_story=backend.get_full_story(), last_story_portion=backend.get_last_story_portion(), first_cap="Begin a new story", second_cap="Write the incipit here")
    if first_access==False:
        return render_template('homepage.html', full_story=backend.get_full_story(), last_story_portion=backend.get_last_story_portion(), first_cap="Continue the story", second_cap="How will it continue?")

@app.route('/', methods = ["POST"])
def keep_going():
    print("keep going")
    if request.method != "POST":
        raise TypeError("Wrong method")
    user_input = request.form.get("keep_going")
    backend.user_dialogue.ask_model(user_input)
    first_access=False # only this case can occur
    return render_template('homepage.html', full_story=backend.get_full_story(), last_story_portion=backend.get_last_story_portion(), first_cap="Continue the story", second_cap="How will it continue?")

@app.route('/delete_files', methods = ["POST"])
def delete_files():
    print("delete files")
    if request.method != "POST":
        raise TypeError("Wrong method")
    backend.delete_files()
    first_access=True
    
    if first_access==True:
        return render_template('homepage.html', full_story=backend.get_full_story(), last_story_portion=backend.get_last_story_portion(), first_cap="Begin a new story", second_cap="Write the incipit here")
    if first_access==False:
        return render_template('homepage.html', full_story=backend.get_full_story(), last_story_portion=backend.get_last_story_portion(), first_cap="Continue the story", second_cap="How will it continue?")

@app.route('/textbox')
def textbox():
    # the_answer = random.randint(25, 60)
    fo = open(file="last_story_portion.txt")
    the_answer = fo.read()
    return the_answer   
