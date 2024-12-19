console.log("Users.js loaded")

function posLoadPageInModal() {
    console.log("Passando por posLoadPageInModal");
    initFormFields();
}

function initFormFields() {
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
}

$(document).ready(function () {
    initFormFields();
});