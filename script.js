function toggleMenu() {
  document.getElementById("menu").classList.toggle("open");
}

document.querySelectorAll("#menu a").forEach(function(link) {
  link.addEventListener("click", function() {
    document.getElementById("menu").classList.remove("open");
  });
});

document.getElementById("year").textContent = new Date().getFullYear();
