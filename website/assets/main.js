/* Padus Solar Challenge — vanilla JS: sidebar, hero slideshow, lightbox */
(function () {
  "use strict";

  /* ---- off-canvas sidebar ---- */
  var toggle = document.querySelector(".nav-toggle");
  var scrim = document.querySelector(".scrim");
  function closeNav() { document.body.classList.remove("nav-open"); }
  if (toggle) toggle.addEventListener("click", function () { document.body.classList.toggle("nav-open"); });
  if (scrim) scrim.addEventListener("click", closeNav);
  document.querySelectorAll(".side-nav a").forEach(function (a) { a.addEventListener("click", closeNav); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeNav(); });

  /* ---- hero slideshow ---- */
  var slides = document.querySelectorAll(".hero-slides .slide");
  if (slides.length > 1) {
    var i = 0;
    setInterval(function () {
      slides[i].classList.remove("on");
      i = (i + 1) % slides.length;
      slides[i].classList.add("on");
    }, 6000);
  }

  /* ---- lightbox ---- */
  var items = Array.prototype.slice.call(document.querySelectorAll("[data-lightbox]"));
  if (items.length) {
    var lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML =
      '<button class="lb-close" aria-label="Chiudi">&times;</button>' +
      '<button class="lb-prev" aria-label="Precedente">&#8249;</button>' +
      '<button class="lb-next" aria-label="Successiva">&#8250;</button>' +
      '<img alt="">' +
      '<div class="lb-cap"></div>';
    document.body.appendChild(lb);

    var lbImg = lb.querySelector("img");
    var lbCap = lb.querySelector(".lb-cap");
    var cur = 0;

    function show(n) {
      cur = (n + items.length) % items.length;
      var el = items[cur];
      lbImg.src = el.getAttribute("data-lightbox");
      var cap = el.getAttribute("data-caption") || "";
      lbCap.textContent = cap;
      lbCap.style.display = cap ? "block" : "none";
    }
    function open(n) { show(n); lb.classList.add("on"); document.body.style.overflow = "hidden"; }
    function close() { lb.classList.remove("on"); document.body.style.overflow = ""; }

    items.forEach(function (el, n) {
      el.addEventListener("click", function (e) { e.preventDefault(); open(n); });
    });
    lb.querySelector(".lb-close").addEventListener("click", close);
    lb.querySelector(".lb-next").addEventListener("click", function () { show(cur + 1); });
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(cur - 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("on")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowRight") show(cur + 1);
      if (e.key === "ArrowLeft") show(cur - 1);
    });
  }
})();
