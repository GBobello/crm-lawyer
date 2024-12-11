function EnviarNovoUser(event) {
  const form = $("#create-user-modal form");
  const url = "/usuarios/inserir/";
  const method = form.attr("method");
  const data = form.serialize();
  const DivMsgErros = document.getElementById("create-modal-user-msg");
  const listaErros = document.getElementById("create-modal-user-erroslist");

  event.preventDefault();

  $.ajax({
    url: url,
    method: method,
    data: data,
    success: function (response) {
      // Verifica se existem elementos <ul class="errorlist">
      const errorLists = $(response).find("ul.errorlist");
      if (errorLists.length > 0) {
        // Limpa area da lista de erros
        listaErros.innerHTML =
          '<h2 class="mb-2 text-lg font-semibold text-red-300">Não foi possivel criar o novo usuário:</h2>';
        //Mostra a div com os erros
        if (DivMsgErros.classList.contains("hidden")) {
          DivMsgErros.classList.remove("hidden");
        }
        // Adiciona os erros encontrados
        errorLists.each(function () {
          const errors = $(this).html(); // Captura o HTML dos erros
          listaErros.innerHTML += "<div>" + errors + "</div>";
        });
      } else {
        location.reload();
      }
    },
    error: function (response) {
      alert("Erro ao salvar o usuário.");
    },
  });
}

function EnviarEditUser(event) {
  const form = $(event.target).closest("form");
  const url = form.attr("action");
  const method = form.attr("method");
  const data = form.serialize();
  const DivMsgErros = form.getElementById("edit-modal-user-msg");
  const listaErros = form.getElementById("edit-modal-user-erroslist");
  event.preventDefault();
  $.ajax({
    url: url,
    method: method,
    data: data,
    success: function (response) {
      // Verifica se existem elementos <ul class="errorlist">
      const errorLists = $(response).find("ul.errorlist");
      if (errorLists.length > 0) {
        // Limpa area da lista de erros
        listaErros.innerHTML =
          '<h2 class="mb-2 text-lg font-semibold text-red-300">Não foi possivel editar o usuário:</h2>';
        //Mostra a div com os erros
        if (DivMsgErros.classList.contains("hidden")) {
          DivMsgErros.classList.remove("hidden");
        }
        // Adiciona os erros encontrados
        errorLists.each(function () {
          const errors = $(this).html(); // Captura o HTML dos erros
          listaErros.innerHTML += "<div>" + errors + "</div>";
        });
      } else {
        location.reload();
      }
    },
    error: function (response) {
      alert("Erro ao salvar o usuário.");
    },
  });
}

function FiltrarTabela(element) {
  let conteudo = element.value.toLowerCase();
  let tbody = document.getElementById("table-body");

  if (!tbody) {
    return;
  }

  let linhas = tbody.getElementsByTagName("tr");

  for (pos in linhas) {
    if (isNaN(pos)) {
      continue;
    }
    let conteudoLinha = linhas[pos].textContent.toLowerCase();
    linhas[pos].classList.remove("hidden");
    if (!conteudoLinha.includes(conteudo)) {
      linhas[pos].classList.add("hidden");
    }
  }
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
  const form = $(element);
  const url = form.attr("action");
  const method = form.attr("method");
  const data = form.serialize();

  event.preventDefault();

  $.ajax({
    url: url,
    method: method,
    data: data,
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