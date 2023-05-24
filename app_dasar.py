from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/home')
def home():
    return 'Welcome to my homepage!'

@app.route('/about')
def about():
    return 'This is my about page.'
