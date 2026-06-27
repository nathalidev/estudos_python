from flask import render_template, request #função do flask para renderização de pagina do front
from flask import jsonify # função para retorno de dados em json pro front usar
from flask import redirect, url_for #joga o usuário pra url em questão
from app import app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/criar-orcamento", methods=["GET", "POST"])
def criar_orcamento():
    return render_template("criar_orcamento.html")

@app.route('/orcamento')
def orcamento():
    nome_sua_empresa = request.form.get("sua_empresa")
    email_sua_empresa = request.form.get("email")
    site_sua_empresa = request.form.get("seu_site")
    telefone_sua_empresa = request.form.get("telefone_sua_empresa")

    nome_cliente = request.form.get("nome_cliente")
    telefone_cliente = request.form.get("telefone_cliente")
    email_cliente = request.form.get("email_cliente")

    inserir_validade = request.form.get("inserir_validade")
    data_validade = request.form.get("data_validade")

    nome_servico_item = request.form.get("servico_item")
    quantidade_item = request.form.get("quantidade")
    valor_unitario = request.form.get("valor")
    valor_desconto = request.form.get("desconto")

    observacoes_adicionais = request.form.get("observacoes")
    prazo_entrega = request.form.get("prazo")
    condicoes_pagamento = request.form.get("condicoes_pagamento")

    context = {
        "nome_sua_empresa": nome_sua_empresa,
        "email_sua_empresa": email_sua_empresa,
        "site_sua_empresa": site_sua_empresa,
        "telefone_sua_empresa": telefone_sua_empresa,

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
        "condicoes_pagamento": condicoes_pagamento
    }

    return render_template('components/orcamento.html', **context)