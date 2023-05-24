# file : P08-model-template-nilai.py
# contoh app Flask dengan model dan template

from flask import Flask, render_template
from models import ModelBerita

app = Flask(__name__)

content = "Virus Corona telah mewabah di dunia. Jagalah kesehatan Anda."

@app.route('/')
def home():
    # membuat objek dari kelas ModelBerita
    modelku = ModelBerita()
    
    # mengisi nilai ke dalam model
    modelku.setJudul("Berita Terkini")
    modelku.setTanggal("01/03/2023")
    modelku.setIsi(content)
    
    # mengirimkan model ke view
    return render_template("berita.html", judul=modelku.cetakJudul(), tanggal=modelku.cetakTanggal(), isi=modelku.cetakIsi())