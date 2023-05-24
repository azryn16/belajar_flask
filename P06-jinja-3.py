# file : P06-jinja-3.py
# Penggunaan percabangan dengan Jinja2

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    a = -5
    return render_template("P06-jinja-3.html",a = a)