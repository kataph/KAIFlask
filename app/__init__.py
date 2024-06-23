from flask import Flask, render_template, request
import os 
import sys
import app.backend.mainbu as mainbu
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + "\\app")
import app.backend as backend
import random


backend.generate_files()
first_access = True

app = Flask(__name__)
@app.route("/")
def hello():
    global first_access
    
    print("first access value %s" %first_access)
    return render_template('homepage.html', full_story=backend.get_full_story(), last_story_portion=backend.get_last_story_portion(), first_cap="Begin a new story"*first_access + "Continue the story"*( not first_access), second_cap="Write the incipit here"*first_access + "How will it continue?"*( not first_access))

@app.route('/', methods = ["POST"])
def keep_going():
    print("keep going")
    if request.method != "POST":
        raise TypeError("Wrong method")
    user_input = request.form.get("keep_going")
    alternative_model = None
    if app.config["IS_COLAB"]:
        alternative_model = mainbu.localModel
        type(alternative_model).__call__ = app.config["COLAB_CALL_FUNCTION"] ## lambda self, prompt: f"{self}-{prompt}-zzz zzz zzz" ## this will work
    backend.user_dialogue.ask_model(user_input, alternative_model = alternative_model)
    first_access=False
    return render_template('homepage.html', full_story=backend.get_full_story(), last_story_portion=backend.get_last_story_portion(), first_cap="Begin a new story"*first_access + "Continue the story"*( not first_access), second_cap="Write the incipit here"*first_access + "How will it continue?"*( not first_access))

@app.route('/delete_files', methods = ["POST"])
def delete_files():
    print("delete files")
    if request.method != "POST":
        raise TypeError("Wrong method")
    backend.delete_files()
    first_access=True
    return render_template('homepage.html', full_story=backend.get_full_story(), last_story_portion=backend.get_last_story_portion(), first_cap="Begin a new story"*first_access + "Continue the story"*( not first_access), second_cap="Write the incipit here"*first_access + "How will it continue?"*( not first_access))

@app.route('/textbox')
def textbox():
    # the_answer = random.randint(25, 60)
    fo = open(file="last_story_portion.txt")
    the_answer = fo.read()
    return the_answer 