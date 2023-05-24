# file : angkatan.py
# tugas Pengembangan Aplikasi Web

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Halo</h2><p>Selamat datang di Pengembangan Aplikasi Web dengan Flask</p>"

@app.route('/angkatan/<int:tahun>')
def angkatan(tahun):
    if tahun == 2019:
        return "Anda harus lulus tahun ini"
    elif tahun == 2020:
        return "Bersiaplah menghadapi Tugas Akhir"
    elif tahun == 2021:
        return "Tugas-tugas kuliah akan semakin banyak"
    elif tahun == 2022:
        return "Selamat belajar dengan dosen baru"
    else:
        return "Tahun yang dimasukkan tidak valid"