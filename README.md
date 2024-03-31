# Kollaborative-AI Project

Simple webapp for AI-collaborative story writing. 

The front-end interface shows the story so far, the last portion of the story produced by the model and a text area for the user to input the start of the next story portion. 

The model tested was the German minstrel model, so German story generation was tested, but one would need just to add the call the appropriate model in the model.py file to change the prompted model. The German minstrel model, was hosted on oobabooga, so it is called through the corresponding api (and the api access point must be specified in the model.py/GERMAN_MINSTREL_MODEL variable). 

