from .mainbu import germanModel as model
# from .mainbu import dummyModel as model

import os 

# story_window_length = 800
story_window_length = 1800

def get_full_story() -> str:
    f = open("full_story.txt", "r")
    full_story = f.read()
    f.close()
    return full_story

def append_to_full_story(last_story_portion) -> None:
    f = open("full_story.txt", "a")
    f.write(last_story_portion)
    f.close()

def get_last_story_portion() -> str:
    f = open("last_story_portion.txt", "r")
    full_story = f.read()
    f.close()
    return full_story

def write_last_story_portion(last_story_portion) -> None:
    f = open("last_story_portion.txt", "w")
    f.write(last_story_portion)
    f.close()

def generate_files():
    # if os.path.isfile("last_story_portion.txt") or os.path.isfile("full_story.txt"):
    #     delete_files()
    #     print("Files deleted")
    f = open("last_story_portion.txt", "w")
    f.write("")
    f.close()
    f = open("full_story.txt", "w")
    f.write("")
    f.close()
    print("Files generated")
def delete_files():
    generate_files()


def query_user(model_answer) -> str:
    print("I queried the user")
    user_query = model_answer + "\nHow does the story continues? "
    user_input = input(user_query)
    return user_input

def ask_model(user_input) -> None:
    print("I asked the model")
    full_story = get_full_story()
    story_window = full_story[:-story_window_length]
    model_answer =  model(story_window + "\n" + user_input)
    append_to_full_story("\n" + user_input + " " + model_answer)
    write_last_story_portion(user_input + " " + model_answer)
