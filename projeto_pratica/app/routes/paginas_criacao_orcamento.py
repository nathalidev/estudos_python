from flask import render_template #função do flask para renderização de pagina do front
from flask import jsonify # função para retorno de dados em json pro front usar
from flask import redirect, url_for #joga o usuário pra url em questão
from app import app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/criar-orcamento")
def criar_orcamento():
    return render_template("criar_orcamento.html")

@app.route('/orcamento')
def orcamento():
    return render_template('components/orcamento.html')