function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const toggle_x = document.getElementById("toggle-x");
  const toggle_hambuguer = document.getElementById("toggle-hambuguer");
  const nav_item_name_list = document.querySelectorAll("span.nav-item-name");

  sidebar.classList.toggle("sidebar-switch");

  if (sidebar.classList.contains("sidebar-switch")) {
    toggle_x.classList.remove("hidden");
    toggle_hambuguer.classList.add("hidden");
    //Mobile
    sidebar.classList.remove("hidden");
    //Pc
    sidebar.classList.add("md:w-20");
  } else {
    toggle_x.classList.add("hidden");
    toggle_hambuguer.classList.remove("hidden");
    //Mobile
    sidebar.classList.add("hidden");
    //Pc\
    sidebar.classList.remove("md:w-20");
  }

  nav_item_name_list.forEach(nav_item_name => {
    nav_item_name.classList.toggle("md:hidden");
  });

}
