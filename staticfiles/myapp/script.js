alert("JavaScript file is working");
// script.js
const form = document.querySelector("#contactForm");

form.addEventListener("submit", function(e) {
  e.preventDefault(); // page reload se bachaata hai
  alert("Thank you! We'll contact you soon.");
});