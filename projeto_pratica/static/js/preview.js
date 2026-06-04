document.addEventListener('DOMContentLoaded', () => {
    const hoje = new Date().toISOString().split("T")[0];
    const validadeInput = document.getElementById("validade");
    validadeInput.min = hoje;
    validadeInput.max = "9999-12-31";

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
    function pegarValorExibir() {
        const preview = document.querySelector('.preview-vazia');
        const nomeCliente = document.getElementById("nome").value.trim();
        const servicoItem = document.getElementById("servico_item").value.trim();
        const valorUnitario = document.getElementById("valor").value;
        const descricao = document.getElementById("descricao").value.trim();
        const observacoes = document.getElementById("observacoes").value.trim();
        const prazoEntrega = document.getElementById("prazo").value;

        const teste = document.getElementById("meu-preview");
        teste.textContent = `${nomeCliente}`

    }

    document.getElementById("nome").addEventListener("input", pegarValorExibir);
});