# file : form-2.py
# penggunaan form dengan library flask-wtf

from flask import Flask, render_template, flash, request
from wtforms import Form, TextAreaField, validators, StringField, SubmitField

# konfigurasi aplikasi
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = StringField('Nama :', validators=[validators.DataRequired()])
    email = StringField('Email :', validators=[validators.DataRequired(), validators.Length(min=6, max=35)])
    password = StringField('Password :', validators=[validators.DataRequired(), validators.Length(min=3, max=35)])
    
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    print (form.errors)
    
    if request.method == 'POST':
        name = request.form['name']
        password =request.form['password']
        email = request.form['email']
        print (name + " " + email + " " + password)
        
        if form.validate():
            # jika sudah mengisi form dengan lengkap
            flash('Halo ' + name + ' ! Terima kasih sudah mendaftar.')
        else:
            flash('Isilah semua bagian form terlebih dahulu. ')
    
    return render_template('form-2.html', form=form)

if __name__ == "__main__":
    app.run()
    
