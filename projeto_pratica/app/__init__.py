from flask import Flask

app = Flask(__name__)

from app.routes import paginas_criacao_orcamento
