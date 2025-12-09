// Mobile navigation toggle
document.getElementById("navToggle").onclick = () => {
    document.getElementById("mainNav").classList.toggle("open");
};

// Sticky shadow for header
window.addEventListener("scroll", () => {
    const header = document.querySelector(".site-header");
    if (window.scrollY > 20) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
});
