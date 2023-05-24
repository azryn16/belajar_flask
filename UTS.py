from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mahasiswa.db'
db = SQLAlchemy(app)

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nim = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Mahasiswa {self.name}>"

@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/mahasiswa')
def mahasiswa():
    mahasiswa_list = Mahasiswa.query.all()
    return render_template('UTS.html', mahasiswa_list=mahasiswa_list)

if __name__ == '__main__':
    app.run(debug=True)
