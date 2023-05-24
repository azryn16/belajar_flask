# file : P08-model-template.py
# contoh app Flask dengan model dan template

from flask import Flask, render_template
from models import ContohModel

app = Flask(__name__)

@app.route('/')
def home():
    # membuat objek dari kelas ContohModel
    modelku = ContohModel()
    
    # mengirimkan model ke view
    return render_template("halo.html", modelku=modelku)