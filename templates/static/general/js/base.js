function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const toggle_x = document.getElementById("toggle-x");
  const toggle_hambuguer = document.getElementById("toggle-hambuguer");

  sidebar.classList.toggle("w-64");

  toggle_x.classList.toggle("hidden");
  toggle_hambuguer.classList.toggle("hidden");

}
