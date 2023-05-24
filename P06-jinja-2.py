# file : P06-jinja-2.py
# Penggunaan operator dengan Jinja2

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    a = 20
    b = 30
    c = 20
    
    # Mengirimkan nilai ke temlate
    return render_template("P06-jinja-2.html", a=a, b=b, c=c)