let closed = document.querySelector(".menu-closed");
let opened = document.querySelector(".menu-open");
let mobileMenu = document.querySelector(".mobile-menu");
let message = document.getElementById('message');

function displayMenu() {
   closed.style.display = "none";
   opened.style.display = "block";
   mobileMenu.style.display = "block";  
}

function closeMenu() {
   closed.style.display = "block";
   opened.style.display = "none";
   mobileMenu.style.display = "none";
}

function closeMessage() {
   message.style.display = "none";
}