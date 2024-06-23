GERMAN_MINSTREL_ADDRESS = "" # to input
MAX_TOKENS = 800


if GERMAN_MINSTREL_ADDRESS == "":
    GERMAN_MINSTREL_ADDRESS = input("You have not inserted the address, please insert the api address now [write 'local' if you are using the colab notebook]: ")
if GERMAN_MINSTREL_ADDRESS == "":
    raise NotImplementedError("Please remember to insert a non-empty address")

import requests
import sys
import time


class Model:
    def __call__(context_prompt, user_request) ->  str:
        raise NotImplementedError("To implement")
    
class GermanMinstrel(Model):
    url = GERMAN_MINSTREL_ADDRESS

    headers = {
        "Content-Type": "application/json"
    }

    max_tokens = MAX_TOKENS

    def __call__(self, prompt) -> str:#context_prompt, user_request) -> str:
        data = {'prompt': prompt,
            'max_tokens': self.max_tokens,
            #'temperature': 1,
            #'top_p': 0.9,
            #'seed': 20,
        }
        if self.url == "local":
            raise TypeError("POST request is being sent to invalid 'local' url. This should not be happening.")
        response = requests.post(self.url, headers=self.headers, json=data, verify=False)
        return response.json()['choices'][0]['text']

class LocalGermanMinstrel(Model):
    def __call__(self, prompt) -> str:
        raise NotImplementedError("Implemented on colab")

    
def slow_print(input_str):
    for c in input_str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

def ask_model_test(instruction, system = ''):
    original = sys.stdout
    sys.stdout = open('last_story_portion.txt', 'w')
    slow_print("This is a slowly printed string for texting purposes")
    sys.stdout = original
    return "xxxxx yyyyyyyyyyy zzzzzzz"

class DummyModel(Model): # to use for testing 
    def __call__(self, instruction, system = ''):
        return ask_model_test(instruction, system)
