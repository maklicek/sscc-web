const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".site-nav");

if (navToggle && navMenu) {
  navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("open");
  });
}
// Najdeme prvky
const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".main-nav");

// Když je tlačítko burgeru kliknuté → přepneme .open
if (navToggle && navMenu) {
  navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("open");
  });
}

