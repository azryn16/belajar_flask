# file : p07-routing-3.py
# contoh app routing dengan FLASK

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Halo</h2><p>Selamat datang di Pengembangan Aplikasi Web dengan Flask</p>"

@app.route('/profil')
def profil():
    return "<h2>Profil</h2><p>Aplikasi Web ini dibuat oleh <b>Chanief Budi Setiawan</b></p>"

@app.route('/salam/<nama>')
def salam(nama):
    return "<h2>Selamat Datang</h2><p>Selamat datang di Aplikasi ini, <b>"+str(nama)+"</b>.</p>"

@app.route('/prodi/<nama_prodi>')
def prodi(nama_prodi):
    return "<h2>Program Studi</b><p>Program Studi yang Anda pilih adalah <b>"+str(nama_prodi)+"</b>.</p>"