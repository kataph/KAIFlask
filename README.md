# Kollaborative-AI Project

Simple webapp for AI-collaborative story writing. 

The front-end interface shows the story so far, the last portion of the story produced by the model and a text area for the user to input the start of the next story portion. 

The model tested was the German minstrel model, so German story generation was tested, but one would need just to add the call the appropriate model in the model.py file to change the prompted model. The German minstrel model, was hosted on oobabooga, so it is called through the corresponding api (and the api access point must be specified in the model.py/GERMAN_MINSTREL_MODEL variable). 

![image](https://github.com/kataph/KAIFlask/assets/45362285/a6c09854-faa6-4826-bdc7-12437b5e1cd7)

# Colab use

You can also use the webapp through Google Colab (link [here](https://colab.research.google.com/drive/1KsT5z4S-QH_c5NrhT1BxLXC89a16LZVx?usp=sharing)). In that case, a Google account for using Colab is required. Moreover, you need a ngrok token (free sign up [here](https://ngrok.com/)) to be copied in the Colab notebook. 

It will take some time to load the model. 


