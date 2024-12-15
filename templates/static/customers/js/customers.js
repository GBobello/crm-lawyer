console.log("Cliente.js loaded")

async function buscarCep() {
    const cep = document.getElementById("cep").value.replace(/\D/g, ""); // Remove caracteres não numéricos

    if (cep.length !== 8) {
        alert("CEP inválido. Certifique-se de que tem 8 dígitos.");
        return;
    }

    try {
        const response = await fetch(`https://viacep.com.br/ws/${cep}/json`);
        if (!response.ok) throw new Error("Erro ao buscar o CEP.");

        const data = await response.json();
        if (data.erro) {
            alert("CEP não encontrado.");
            return;
        }

        // Preenche os campos com os dados retornados
        document.getElementById("endereco").value = data.logradouro || "";
        document.getElementById("bairro").value = data.bairro || "";
        document.getElementById("cidade").value = data.localidade || "";
        document.getElementById("id_estado").value = data.uf || "";
    } catch (error) {
        console.error("Erro ao buscar o CEP:", error);
        alert("Erro ao buscar o CEP. Tente novamente.");
    }
}


$(document).ready(function () {
    // Máscara para Documento
    $("#documento").keyup(function () {
        var tamanho = $("#documento").val().length;

        if (tamanho <= 14) {
            $("#documento").mask("000.000.000-000");
        } else {
            $("#documento").mask("00.000.000/0000-00");
        }
    });

    // Máscara para Telefone (com ou sem DDD)
    $("#telefone").mask("(00) 00000-0000");
});