function toggleMenu() {
  document.getElementById('menu').classList.toggle('open');
}

document.querySelectorAll('#menu a').forEach(link => {
  link.addEventListener('click', () => {
    document.getElementById('menu').classList.remove('open');
  });
});

document.getElementById('year').textContent = new Date().getFullYear();
