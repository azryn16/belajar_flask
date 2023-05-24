# file : P08-model.py
# contoh app routing dengan variable pada Flask

from flask import Flask
from models import ContohModel

app = Flask(__name__)

@app.route('/')
def home():
    #membuat contoh objek dari kelas ContohModel
    modelku = ContohModel()
    
    #mengambil nilai dari model tsb
    return modelku.CetakTeks()