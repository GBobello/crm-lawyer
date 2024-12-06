function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const toggle_x = document.getElementById("toggle-x");
  const toggle_hambuguer = document.getElementById("toggle-hambuguer");
  const nav_item_name_list = document.querySelectorAll("span.nav-item-name");

  sidebar.classList.toggle("w-64");
  sidebar.classList.toggle("md:hover:w-64");
  sidebar.classList.toggle("w-20");

  toggle_x.classList.toggle("hidden");
  toggle_hambuguer.classList.toggle("hidden");

  nav_item_name_list.forEach(nav_item_name => {
    nav_item_name.classList.toggle("hidden");
  });

}
