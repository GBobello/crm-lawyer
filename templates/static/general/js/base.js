function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const toggle_x = document.getElementById("toggle-x");
  const toggle_hambuguer = document.getElementById("toggle-hambuguer");
  const nav_item_name_list = document.querySelectorAll("span.nav-item-name");
  const toggleIcons = sidebar.querySelectorAll("i.toggle-icon");
  const conteudo = document.getElementById("conteudo");

  sidebar.classList.toggle("sidebar-switch");

  if (sidebar.classList.contains("sidebar-switch")) {
    toggle_x.classList.remove("hidden");
    toggle_hambuguer.classList.add("hidden");
    //Mobile
    sidebar.classList.add("translate-x-0");
    //Pc
    sidebar.classList.add("sm:w-16");
    conteudo.classList.add("sm:ml-16");
  } else {
    toggle_x.classList.add("hidden");
    toggle_hambuguer.classList.remove("hidden");
    //Mobile
    sidebar.classList.remove("translate-x-0");
    //Pc
    sidebar.classList.remove("sm:w-16");
    conteudo.classList.remove("sm:ml-16");
  }

  nav_item_name_list.forEach(nav_item_name => {
    nav_item_name.classList.toggle("sm:hidden");
  });
  toggleIcons.forEach(toggleIcon => {
    toggleIcon.classList.toggle("sm:hidden");
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

function toggleHidden(id) {
  const element = document.getElementById(id);
  element.classList.toggle("hidden");
}


