document.addEventListener('DOMContentLoaded', () => {
    const regex = /^[A-Za-zÀ-ÿ\s]+$/;
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