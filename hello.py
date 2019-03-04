from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hola, Mundo!'

@app.route('/index.html')
def hello2():
    return 'Hola, Mundo!'


