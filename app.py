from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Responds with welcome."""
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    """Responds with welcome home."""
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    """Responds with welcome back."""
    return "welcome back"