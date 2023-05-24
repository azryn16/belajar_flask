# file : form-1.py
# penggunaan form dengan library flask-wtf

from flask import Flask, render_template, flash, request
from wtforms import Form, TextAreaField, validators, StringField, SubmitField

# konfigurasi aplikasi
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = StringField('Nama : ', validators=[validators.DataRequired()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    
    print (form.errors)
    if request.method == 'POST':
        name = request.form['name']
        print(name)
        
        if form.validate():
            # Ucapan selamat datang
            flash('Halo ' + name + ' ! Selamat Datang.')
        else:
            flash('Isilah semua bagian form. ')
    
    return render_template('form-1.html', form=form)
if __name__ == '__main__':
    app.run()