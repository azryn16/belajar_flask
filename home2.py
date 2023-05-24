# file : home2.py
# contoh halaman web dengan Flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')