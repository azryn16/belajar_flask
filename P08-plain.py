# file : P08-plain.py
# contoh app flask tanpa model dan template

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Aplikasi Flask</h2><p>Selamat datang di Pengembangan Aplikasi Web</p>"