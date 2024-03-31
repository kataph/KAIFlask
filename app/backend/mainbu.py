MAX_TOKENS = 800
model_name='jphme/em_german_mistral_v01'


from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, TextStreamer    

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
    prompt=f"{system} USER: {instruction} ASSISTANT:"
    input_tokens=tokenizer(prompt, return_tensors="pt").to(model.device)
    output_tokens=model.generate(**input_tokens,  generation_config=generation_config, streamer=streamer)[0]
    answer=tokenizer.decode(output_tokens, skip_special_tokens=True)
    return answer

class GermanModel:
    def __init__(self) -> None:
        self.__call__ = ask_model

germanModel = GermanModel()
        