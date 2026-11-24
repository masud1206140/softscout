// Phone menu toggle. Without JavaScript the menu simply stays open.
(function () {
  document.documentElement.classList.add("js");
  var side = document.getElementById("side");
  var btn = side && side.querySelector(".menu-btn");
  if (!btn) return;
  var label = btn.querySelector(".menu-label");
  function set(open) {
    side.classList.toggle("open", open);
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    label.textContent = open ? btn.dataset.close : btn.dataset.open;
  }
  btn.addEventListener("click", function () { set(btn.getAttribute("aria-expanded") !== "true"); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && side.classList.contains("open")) { set(false); btn.focus(); }
  });
})();
