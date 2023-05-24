# file : P06-jinja-4.py
# Penggunaan perulangan dengan Jinja2

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #List untuk elemen bertipe tuple
    navigasi = [
        ('/', 'Beranda'),
        ('/profil', 'Profil'),
        ('/produk', 'Produk'),
        ('/kontak', 'Kontak'),
    ]
    return render_template("P06-jinja-4.html", navigasi = navigasi)

@app.route('/profil')
def profil():
    return "<h2>profil</h2>"

@app.route('/produk')
def produk():
    return "<h2>Produk</h2>"

@app.route('/kontak')
def kontak():
    return "<h2>Kontak</h2>"