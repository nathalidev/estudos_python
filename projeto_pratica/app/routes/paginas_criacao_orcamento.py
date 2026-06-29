from flask import render_template, request #função do flask para renderização de pagina do front
from flask import jsonify # função para retorno de dados em json pro front usar
from flask import redirect, url_for #joga o usuário pra url em questão
from app import app

from datetime import datetime

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/criar-orcamento")
def criar_orcamento():
    return render_template("criar_orcamento.html")

@app.route('/orcamento', methods=["GET", "POST"])
def orcamento():
    nome_sua_empresa = request.form.get("sua_empresa")
    email_sua_empresa = request.form.get("email")
    site_sua_empresa = request.form.get("seu_site")
    telefone_sua_empresa = request.form.get("telefone_sua_empresa")

    nome_cliente = request.form.get("nome_cliente")
    telefone_cliente = request.form.get("telefone_cliente")
    email_cliente = request.form.get("email_cliente")

    inserir_validade = request.form.get("inserir_validade")
    data_validade_ingles = request.form.get("data_validade")
    data_validade = datetime.strptime(data_validade_ingles, "%Y-%m-%d").strftime("%d/%m/%Y") if data_validade_ingles else None

    nome_servico_item = request.form.get("servico_item")
    quantidade_item = int(request.form.get("quantidade"))
    valor_unitario = float(request.form.get("valor"))
    valor_desconto = float(request.form.get("desconto"))

    observacoes_adicionais = request.form.get("observacoes")
    prazo_entrega_ingles = request.form.get("prazo")
    prazo_entrega = datetime.strptime(prazo_entrega_ingles, "%Y-%m-%d").strftime("%d/%m/%Y") if prazo_entrega_ingles else None
    condicoes_pagamento = request.form.get("condicoes_pagamento")
    data_hoje = datetime.now().strftime("%d/%m/%Y")
    subtotal = quantidade_item * valor_unitario
    total = subtotal - valor_desconto

    context = {
        "nome_sua_empresa": nome_sua_empresa,
        "email_sua_empresa": email_sua_empresa,
        "site_sua_empresa": site_sua_empresa,
        "telefone_sua_empresa": telefone_sua_empresa,
        "data_hoje": data_hoje,

        "nome_cliente": nome_cliente,
        "telefone_cliente": telefone_cliente,
        "email_cliente": email_cliente,

        "inserir_validade": inserir_validade,
        "data_validade": data_validade,

        "nome_servico_item": nome_servico_item,
        "quantidade_item": quantidade_item,
        "valor_unitario": valor_unitario,
        "valor_desconto": valor_desconto,

        "observacoes_adicionais": observacoes_adicionais,
        "prazo_entrega": prazo_entrega,
        "condicoes_pagamento": condicoes_pagamento,
        "subtotal": subtotal,
        "total": total
    }

    return render_template('components/orcamento.html', **context)