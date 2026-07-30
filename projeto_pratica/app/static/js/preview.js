document.addEventListener('DOMContentLoaded', () => {
    console.log("Arquivo JS carregado!");

    // Pega a data atual
    const hoje = new Date();

    // Formata para o padrão brasileiro (dd/mm/yyyy)
    const dia = String(hoje.getDate()).padStart(2, "0");
    const mes = String(hoje.getMonth() + 1).padStart(2, "0"); // mês começa em 0
    const ano = hoje.getFullYear();

    const dataFormatada = `${dia}/${mes}/${ano}`;

  // Atualiza o conteúdo do elemento
  
  const suaEmpresa = document.getElementById("sua_empresa");
  const email = document.getElementById("email");
  const seuSite = document.getElementById("seu_site");
  const telefoneSuaEmpresa = document.getElementById("telefone_sua_empresa");
  
  // Campos do cliente
  const nomeCliente = document.getElementById("nome_cliente");
  const telefoneCliente = document.getElementById("telefone_cliente");
  const emailCliente = document.getElementById("email_cliente");
  
  // Validade
  const inserirValidade = document.getElementById("inserir_validade");
  const campoValidade = document.getElementById("campo-validade");
  const dataValidade = document.getElementById("data_validade");
  dataValidade.min = hoje;
  dataValidade.max = "9999-12-31";
  
  // Itens
  const servicoItem = document.getElementById("servico_item");
    const quantidade = document.getElementById("quantidade");
    const valor = document.getElementById("valor");
    const desconto = document.getElementById("desconto");

    // Observações
    const observacoes = document.getElementById("observacoes");

    // Prazo
    const prazo = document.getElementById("prazo");

    // Condições de pagamento
    const condicoesPagamento = document.getElementById("condicoes_pagamento");

    // Preview
    const meuPreview = document.getElementById("meu-preview");

    const regex = /^[A-Za-zÀ-ÿ\s]+$/;

    function exibirValidade(){
        const campoValidade = document.getElementById('campo-validade');
        const opcoesValidade = document.querySelectorAll('input[name="validade"]');

        opcoesValidade.forEach(radio => {
            radio.addEventListener('change', function() {
            if (this.value === "sim") {
                campoValidade.style.display = "block"; // mostra o campo
            } else {
                campoValidade.style.display = "none";  // esconde o campo
            }
            });
        });
    }

    function pegarValorExibir(campoDoInput, campoDoOrcamento) {
        const campoEmpresa = document.getElementById(campoDoInput);
        const previewEmpresa = document.getElementById(campoDoOrcamento);
        previewEmpresa.textContent = campoEmpresa.value;
    }

    campos = [
        ["sua_empresa", "preview_empresa"],
        ["email", "preview_email"],
        ["seu_site", "preview_site"],
        ["telefone_sua_empresa", "preview_telefone"],
        ["nome_cliente", "preview_nome_cliente"],
        ["telefone_cliente", "preview_telefone_cliente"],
        ["email_cliente", "preview_email_cliente"],
        ["data_validade", "validade"],
        ["servico_item", "preview_servico_item"],
        ["quantidade", "preview_quantidade"],
        ["valor", "preview_valor"],
        ["desconto", "preview_desconto"],
        ["observacoes", "observacoes_adicionais"],
        ["prazo", "preview_prazo"],
        ["condicoes_pagamento", "preview_condicoes_pagamento"]
    ]

    campos.forEach(([campoDoInput, campoDoOrcamento]) => {
        const input = document.getElementById(campoDoInput);
        const preview = document.getElementById(campoDoOrcamento);
        input.addEventListener("input", function() {
            pegarValorExibir(campoDoInput, campoDoOrcamento);
        });
    });

    const iframe = document.getElementById("meuIframe");

    iframe.addEventListener("load", () => {
        const doc = iframe.contentDocument;

        function ajustarAltura() {
            iframe.style.height =
                doc.documentElement.scrollHeight + "px";
        }

        ajustarAltura();
    });
});