# file : p07-routing-1.py
# contoh app routing dengan FLASK

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Halo</h2><p>Selamat datang di Pengembangan Aplikasi Web dengan Flask</p>"

@app.route('/profil')
def profil():
    return "<h2>Profil</h2><p>Aplikasi Web ini dibuat oleh <b>Chanief Budi Setiawan</b></p>"