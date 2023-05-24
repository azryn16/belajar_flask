# file : tugas-form.py
# 212104001-Aaz Zazri Nugraha

from flask import Flask, render_template, flash, request
from wtforms import Form, TextAreaField, validators, StringField, SubmitField

# konfigurasi aplikasi
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# variable objek
class ReusableForm(Form):
    nim = StringField('NIM :', validators=[validators.DataRequired(), validators.Length(min=9, max=12)])
    nama = StringField('Nama :', validators=[validators.DataRequired()])
    programstudi = StringField('Program Studi :', validators=[validators.DataRequired(), validators.Length(min=3, max=35)])
    alamat = StringField('Alamat :', validators=[validators.DataRequired()])

# 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    print (form.errors)
    
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        programstudi =request.form['programstudi']
        alamat = request.form['alamat']
        print (nim + " " + nama + " " + programstudi + "" + alamat)
        
        if form.validate():
            # jika sudah mengisi form dengan lengkap
            flash('Halo ' + nama + ', ' + nim + ', ' + programstudi + ', ' + alamat + ' ! Terima kasih sudah mengisi form mahasiswa.')
        else:
            flash('Isilah semua bagian form terlebih dahulu. ')
    
    return render_template('tugas-form.html', form=form)

if __name__ == "__main__":
    app.run()
    
