from flask import app, Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/Projetos')
def projetos():
    return render_template('Projetos.html')

@app.route('/Contatos')
def contatos():
    return render_template('Contatos.html')