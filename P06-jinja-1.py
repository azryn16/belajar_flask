# file : P06-jinja-1.py
# pengolahan variabel dengan Jinja2

from flask import Flask, render_template
from models import Lingkaran

app = Flask(__name__)

@app.route('/')
def index():
    str_var = "Pengembangan Aplikasi Web"
    int_var = 20
    float_var = 29.05
    list_var = [1,2,3]
    dict_var = {'satu' : 1 , 'dua' : 2 , 'tiga' : 3}
    model = Lingkaran(30.0)
    
    # Mengirimkan nilai ke template
    return render_template("P06-jinja-1.html", str_var=str_var, int_var=int_var, float_var=float_var, list_var=list_var, dict_var=dict_var, model=model)