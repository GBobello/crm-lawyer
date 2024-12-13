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

function CloseModal(element) {
  const target = document.getElementById(element.attributes.getNamedItem("data-modal-target").value);

  let event = new KeyboardEvent('keydown', {
    key: 'Escape', // A tecla que você quer simular
    code: 'Escape',
    keyCode: 27, // Código da tecla
    charCode: 0,
    bubbles: true
  });

  // Dispara o evento no elemento selecionado
  target.dispatchEvent(event);
}

function SendForm(event, element) {
  event.preventDefault();
  const form = $(element);
  const url = form.attr("action");
  const method = form.attr("method");
  const data = new FormData(form.get(0));

  $.ajax({
    url: url,
    method: method,
    data: data,
    processData: false,
    contentType: false,
    success: function (response) {
      if (!response.status) {
        console.log(response.message);
        form.html(response);
      } else {
        console.log(response.message)
        location.reload();
      }
    },
    error: function (response) {
      console.log(response.message);
      alert("Erro ao tentar enviar o o formulário");
    },
  });
}

function LoadPageInModal(element) {
  const modalContentTarget = document.getElementById(element.attributes.getNamedItem("data-modal-target").value + '-content');
  // modalContentTarget.innerHTML = '<div class="transition-opacity duration-1000 opacity-0 group-hover:opacity-100 animate-bounce"><div class="m-auto h-20 w-20 border-8 border-gray-50 rounded-full border-t-[var(--main-color)] animate-spin "></div></div>';

  $.ajax({
    url: element.attributes.getNamedItem("data-url").value,
    method: "GET",
    success: function (response) {
      modalContentTarget.innerHTML = response;
      // initModals();
    },
    error: function (response) {
      console.log("Erro carregando pagina no modal" + response.message);
    },
  });
}

function ReloadList(element) {
  const block_content = document.getElementById("block-content");
  const search_input = document.getElementById("table-search");

  if (!element.attributes.getNamedItem("data-url-page")) {
    console.log("Falta definir o atributo data-url-page no elemento " + element.id);
    return;
  }

  let url = element.attributes.getNamedItem("data-url-page").value;
  if (search_input.value.trim() !== '') {
    if (url.trim() !== '') {
      url += '&search=' + search_input.value;
    } else {
      url = '?search=' + search_input.value;
    }

  }

  $.ajax({
    url: url,
    method: "GET",
    contentType: 'application/text',
    dataType: 'text',
    success: function (response) {
      console.log("Tabela recarregada por " + element.id);
      block_content.innerHTML = response;
      initModals();
      initDropdowns();
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
