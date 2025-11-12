document.addEventListener("DOMContentLoaded", () => {
  document.body.classList.add("js-enabled");

  const filterButtons = Array.from(document.querySelectorAll("[data-filter]"));
  const projectCards = Array.from(document.querySelectorAll("[data-category]"));
  const statusLabel = document.querySelector("[data-filter-status]");
  let activeFilter = "all";

  function setActiveFilter(filterValue) {
    activeFilter = filterValue;

    filterButtons.forEach((button) => {
      const isActive = button.dataset.filter === filterValue;
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-pressed", String(isActive));
    });

    projectCards.forEach((card) => {
      const categories = card.dataset.category.split(",");
      const isMatch = filterValue === "all" || categories.includes(filterValue);
      card.classList.toggle("is-hidden", !isMatch);
      card.setAttribute("aria-hidden", String(!isMatch));
    });

    if (statusLabel) {
      if (filterValue === "all") {
        statusLabel.textContent = `Showing all ${projectCards.length} projects.`;
      } else {
        const matchCount = projectCards.filter((card) => {
          const categories = card.dataset.category.split(",");
          return categories.includes(filterValue);
        }).length;
        statusLabel.textContent = `Filtered by ${filterValue.replace(/-/g, " ")} – ${matchCount} project${matchCount === 1 ? "" : "s"} visible.`;
      }
    }
  }

  filterButtons.forEach((button) => {
    button.classList.add("filter-chip");
    button.addEventListener("click", () => {
      const filterValue = button.dataset.filter ?? "all";
      if (filterValue === activeFilter) return;
      setActiveFilter(filterValue);
    });
  });

  setActiveFilter(activeFilter);

  const mobileToggle = document.querySelector("[data-mobile-toggle]");
  const mobilePanel = document.querySelector("[data-mobile-menu]");

  if (mobileToggle && mobilePanel) {
    const toggleMenu = () => {
      const isOpen = mobilePanel.hasAttribute("data-open");
      if (isOpen) {
        mobilePanel.removeAttribute("data-open");
        mobilePanel.setAttribute("hidden", "");
        mobileToggle.setAttribute("aria-expanded", "false");
      } else {
        mobilePanel.setAttribute("data-open", "");
        mobilePanel.removeAttribute("hidden");
        mobileToggle.setAttribute("aria-expanded", "true");
        mobilePanel.querySelector("a, button")?.focus({ preventScroll: true });
      }
    };

    mobileToggle.addEventListener("click", () => {
      toggleMenu();
    });

    document.addEventListener("click", (event) => {
      if (!mobilePanel.hasAttribute("data-open")) return;
      if (mobilePanel.contains(event.target)) return;
      if (mobileToggle.contains(event.target)) return;
      toggleMenu();
    });

    window.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && mobilePanel.hasAttribute("data-open")) {
        event.preventDefault();
        toggleMenu();
        mobileToggle.focus({ preventScroll: true });
      }
    });
  }
});

