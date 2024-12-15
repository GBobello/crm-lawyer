function FiltrarTabela(element) {
    // let conteudo = element.value.toLowerCase();
    // let tbody = document.getElementById("table-body");

    // if (!tbody) {
    //   return;
    // }

    // let linhas = tbody.getElementsByTagName("tr");

    // for (pos in linhas) {
    //   if (isNaN(pos)) {
    //     continue;
    //   }
    //   let conteudoLinha = linhas[pos].textContent.toLowerCase();
    //   linhas[pos].classList.remove("hidden");
    //   if (!conteudoLinha.includes(conteudo)) {
    //     linhas[pos].classList.add("hidden");
    //   }
    // }
}

function SendExport(element) {
    const option = $(element);
    const url = option.attr("data-url");
    const method = 'GET';

    let urlParms = '';
    urlParms = MountUrl(urlParms);
    console.log(url + urlParms);

    window.location.href = url + urlParms;
}

function MountUrl(url) {
    const search_input = document.getElementById("table-search");
    const orderby_input = document.getElementById("orderby");

    if (search_input.value.trim() !== '') {
        if (url.trim() !== '') {
            url += '&search=' + search_input.value;
        } else {
            url = '?search=' + search_input.value;
        }
    }

    if (orderby_input.value.trim() !== '') {
        if (url.trim() !== '') {
            url += '&orderby=' + orderby_input.value;
        } else {
            url = '?orderby=' + orderby_input.value;
        }
    }

    return url;
}

function ReloadList(element) {
    const block_content = document.getElementById("block-content");

    if (!element.attributes.getNamedItem("data-url-page")) {
        console.log("Falta definir o atributo data-url-page no elemento " + element.id);
        return;
    }

    let url = element.attributes.getNamedItem("data-url-page").value;
    url = MountUrl(url);

    $.ajax({
        url: url,
        method: "GET",
        contentType: 'application/text',
        dataType: 'text',
        success: function (response) {
            console.log("Tabela recarregada por " + element.id);
            block_content.innerHTML = response;
            iniReloadList();
        },
        error: function (response) {
            console.log("Erro carregando pagina no modal" + response.message);
        },
    });
}

function Search(event, element) {
    if (event.keyCode == 13) {
        ReloadList(element);
    }
}

function CheckSearchInput(event, searchInput, searchBtnClose) {
    if (searchInput.value.trim()) {
        searchBtnClose.classList.remove("hidden");
    } else if (!searchBtnClose.classList.contains('hidden')) {
        searchBtnClose.classList.add("hidden");
    }
}

function initTableSearch() {
    const searchInput = document.getElementById("table-search");
    const searchBtnClose = document.getElementById("table-search-x");
    searchInput.addEventListener("change", (e) => {
        CheckSearchInput(e, searchInput, searchBtnClose)
    });
    searchBtnClose.addEventListener("click", () => {
        searchInput.value = "";

        let event = new KeyboardEvent('keydown', {
            key: 'Return', // A tecla que você quer simular
            code: 'Return',
            keyCode: 13, // Código da tecla
            charCode: 0,
            bubbles: true
        });
        // Dispara o evento no elemento selecionado
        searchInput.dispatchEvent(event);

    });
    CheckSearchInput(null, searchInput, searchBtnClose);
}

function iniReloadList() {
    initModals();
    initDropdowns();
    initTableSearch();
}

$(document).ready(function () {
    initTableSearch();
});