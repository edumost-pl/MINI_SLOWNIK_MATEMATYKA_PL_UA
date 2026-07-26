document.addEventListener("DOMContentLoaded", () => {
  const search = document.querySelector("#toc-search");
  const buttons = document.querySelectorAll(".cat-btn");
  const cards = document.querySelectorAll(".toc-card");
  let activeCat = "all";

  function applyFilters() {
    const q = (search?.value || "").trim().toLowerCase();
    cards.forEach((card) => {
      const cat = card.dataset.cat || "";
      const text = card.textContent.toLowerCase();
      const catOk = activeCat === "all" || cat === activeCat;
      const qOk = !q || text.includes(q);
      card.classList.toggle("hidden", !(catOk && qOk));
    });
  }

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      buttons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      activeCat = btn.dataset.cat || "all";
      applyFilters();
    });
  });

  search?.addEventListener("input", applyFilters);

  document.querySelectorAll("[data-print]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const mode = (btn.getAttribute("data-print") || "").trim();
      document.body.classList.add("is-printing");
      document.body.classList.toggle("print-compact", mode === "compact");
      window.print();
      setTimeout(() => {
        document.body.classList.remove("is-printing", "print-compact");
      }, 800);
    });
  });

  initBlockZoom();
});

function initBlockZoom() {
  const zoomables = document.querySelectorAll("article.card, section.life-strip");
  if (!zoomables.length) return;

  const overlay = document.createElement("div");
  overlay.className = "card-zoom-overlay no-print";
  overlay.setAttribute("role", "dialog");
  overlay.setAttribute("aria-modal", "true");
  overlay.innerHTML = `
    <div class="card-zoom-panel">
      <button type="button" class="card-zoom-close" aria-label="Zamknij">×</button>
      <div class="card-zoom-content"></div>
    </div>
    <p class="card-zoom-hint">Kliknij tło lub Esc, aby zamknąć</p>
  `;
  document.body.appendChild(overlay);

  const content = overlay.querySelector(".card-zoom-content");
  const closeBtn = overlay.querySelector(".card-zoom-close");
  const panel = overlay.querySelector(".card-zoom-panel");

  function openBlock(el) {
    const clone = el.cloneNode(true);
    clone.removeAttribute("tabindex");
    clone.removeAttribute("role");
    clone.removeAttribute("aria-label");
    clone.setAttribute("aria-hidden", "false");
    clone.classList.add("is-zoomed");
    content.innerHTML = "";
    content.appendChild(clone);
    overlay.classList.add("is-open");
    document.body.classList.add("card-zoom-open");
    closeBtn.focus();
  }

  function closeBlock() {
    overlay.classList.remove("is-open");
    document.body.classList.remove("card-zoom-open");
    content.innerHTML = "";
  }

  zoomables.forEach((el) => {
    el.classList.add("is-zoomable");
    el.setAttribute("tabindex", "0");
    el.setAttribute("role", "button");
    const label = el.classList.contains("life-strip")
      ? "Powiększ przykład z życia"
      : "Powiększ kartę";
    el.setAttribute("aria-label", label);
    el.addEventListener("click", () => openBlock(el));
    el.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        openBlock(el);
      }
    });
  });

  closeBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    closeBlock();
  });

  overlay.addEventListener("click", (e) => {
    if (e.target === overlay || e.target.classList.contains("card-zoom-hint")) {
      closeBlock();
    }
  });

  panel.addEventListener("click", (e) => e.stopPropagation());

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && overlay.classList.contains("is-open")) {
      closeBlock();
    }
  });
}
