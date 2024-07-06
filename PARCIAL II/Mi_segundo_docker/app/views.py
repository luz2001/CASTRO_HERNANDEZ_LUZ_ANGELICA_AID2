from flask import render_template
from app import app 

@app.route('/') 
def raiz():
   return "Mi segundo Docker"

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/parrot')
def parrot():
    return render_template('parrot.html')
