# file : P06-jinja-5.py
# Penggunaan CSS dengan Jinja2

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("P06-jinja-5.html")