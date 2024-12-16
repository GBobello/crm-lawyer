function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const toggle_x = document.getElementById("toggle-x");
  const toggle_hambuguer = document.getElementById("toggle-hambuguer");
  const nav_item_name_list = document.querySelectorAll("span.nav-item-name");
  const toggleIcons = sidebar.querySelectorAll("i.toggle-icon");
  const conteudo = document.getElementById("conteudo");

  sidebar.classList.toggle("sidebar-switch");

  if (sidebar.classList.contains("sidebar-switch")) {
    localStorage.setItem('django.crm.navSidebarIsOpen', true);

    toggle_x.classList.remove("hidden");
    toggle_hambuguer.classList.add("hidden");
    //Mobile
    sidebar.classList.add("translate-x-0");
    //Pc
    sidebar.classList.add("md:w-16");
    conteudo.classList.add("md:ml-16");
  } else {
    localStorage.setItem('django.crm.navSidebarIsOpen', false);
    toggle_x.classList.add("hidden");
    toggle_hambuguer.classList.remove("hidden");
    //Mobile
    sidebar.classList.remove("translate-x-0");
    //Pc
    sidebar.classList.remove("md:w-16");
    conteudo.classList.remove("md:ml-16");
  }

  nav_item_name_list.forEach(nav_item_name => {
    nav_item_name.classList.toggle("md:hidden");
    $(nav_item_name).parent().toggleClass("md:justify-center");
  });
  toggleIcons.forEach(toggleIcon => {
    toggleIcon.classList.toggle("md:hidden");
  });


}

function toggleSubMenu(element) {
  const submenus = element.getElementsByClassName("slide-menu")
  const toggleIcons = element.getElementsByClassName("toggle-icon")
  for (let i = 0; i < submenus.length; i++) {
    const submenu = submenus[i];
    submenu.classList.toggle("h-0");
  }
  for (let i = 0; i < toggleIcons.length; i++) {
    const icon = toggleIcons[i];
    icon.classList.toggle("rotate-180");
    icon.classList.toggle("right-5");
  }
}

$(document).ready(function () {
  const navSidebarIsOpen = localStorage.getItem('django.crm.navSidebarIsOpen');
  if (navSidebarIsOpen === 'true') {
    toggleSidebar();
  }
});

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

function LoadPageInModal(element) {
  const modalContentTarget = document.getElementById(element.attributes.getNamedItem("data-modal-target").value + '-content');
  modalContentTarget.innerHTML = '<div class="transition-opacity duration-1000 group-hover:opacity-100 animate-bounce"><div class="m-auto h-20 w-20 border-8 border-gray-50 rounded-full border-t-[var(--main-color)] animate-spin "></div></div>';

  $.ajax({
    url: element.attributes.getNamedItem("data-url").value,
    method: "GET",
    success: function (response) {
      modalContentTarget.innerHTML = response;
      posLoadPageInModal();
    },
    error: function (response) {
      console.log("Erro carregando pagina no modal" + response.message);
    },
  });
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


