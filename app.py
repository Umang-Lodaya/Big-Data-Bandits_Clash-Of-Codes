# flask_ngrok_example.py
import pickle
from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

pkl = pickle.load()
model = pkl.load_model("")

@app.route("/")
def hello():
    return "Hello World!"

app.run()