MAX_TOKENS = 800
model_name='jphme/em_german_mistral_v01'

import sys
import time


from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, TextStreamer, BitsAndBytesConfig

# model = None
model=AutoModelForCausalLM.from_pretrained(model_name, low_cpu_mem_usage=True, load_in_8bit=True)
tokenizer=AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token_id=tokenizer.eos_token_id

generation_config=GenerationConfig(max_new_tokens=500,
                                    temperature=0.4,
                                    top_p=0.95,
                                    top_k=40,
                                    repetition_penalty=1.2,
                                    bos_token_id=tokenizer.bos_token_id,
                                    eos_token_id=tokenizer.eos_token_id,
                                    do_sample=True,
                                    use_cache=True,
                                    output_attentions=False,
                                    output_hidden_states=False,
                                    output_scores=False,
                                    remove_invalid_values=True
                                    )
streamer = TextStreamer(tokenizer)

def ask_model(instruction, system='Du bist ein Romanautor, der sich auf das Schreiben pornographisch Romane spezialisiert hat, die wegen ihrer Explizitheit erneuert wurden. Sie müssen Ihre wildesten Fantasien dem Publikum erzählen..'):
    original = sys.stdout
    sys.stdout = open('last_story_portion.txt', 'w')
    
    prompt=f"{system} USER: {instruction} ASSISTANT:"
    input_tokens=tokenizer(prompt, return_tensors="pt").to(model.device)
    output_tokens=model.generate(**input_tokens,  generation_config=generation_config, streamer=streamer)[0]
    answer=tokenizer.decode(output_tokens, skip_special_tokens=True)
    
    sys.stdout = original
    
    return answer



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

class GermanModel:
    def __call__(self, instruction, system = ''):
        return ask_model(instruction, system)
    # def __call__(self, instruction, system = ''):
    #     return ask_model_test(instruction, system) # also works
    # def __init__(self) -> None:
    #     # self.__call__ = ask_model
        # self.__call__ = ask_model_test  ## doesnt work
# GermanModel.__call__ = ask_model_test  ## works

germanModel = GermanModel()
        