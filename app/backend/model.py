GERMAN_MINSTREL_ADDRESS = "" # to input
MAX_TOKENS = 800


if GERMAN_MINSTREL_ADDRESS == "":
    GERMAN_MINSTREL_ADDRESS = input("You have not inserted the address, please insert the api address now [write 'local' if you are using the colab notebook]: ")
if GERMAN_MINSTREL_ADDRESS == "":
    raise NotImplementedError("Please remember to insert a non-empty address")

import requests


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
            raise TypeError("POST request is being sent to invalid 'local' url.")
        response = requests.post(self.url, headers=self.headers, json=data, verify=False)
        return response.json()['choices'][0]['text']

class LocalGermanMinstrel(Model):
    def __call__(self, prompt) -> str:
        raise NotImplementedError("Implemented on colab")

class DummyModel(Model): # to use for testing 
    def __call__(context_prompt, user_request) -> str:
        return "Xxx xxx xxx."