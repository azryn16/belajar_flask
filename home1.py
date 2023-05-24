# file : home1.py
# contoh halaman web dengan Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Pengembangan Aplikasi Web dengan Python"