# Import Libraries 
from app import app
import os
# If file is called directly called, then run the app on the PORT provided defined in ENV or use '6969'.
if __name__ == "__main__":
    app.config["IS_COLAB"] = False
    app.run("0.0.0.0")