from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lupa')
def lupa():
    return render_template('lupa.html')

@app.route('/pupa')
def pupa():
    return render_template('pupa.html')

app.run(debug=True)
