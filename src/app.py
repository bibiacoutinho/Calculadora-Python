from flask import Flask
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('calculadora.html')

@app.route('/log')
def log():
    return render_template('logs.html')

if __name__=='__main__':
    app.run(host='0.0.0.0')
