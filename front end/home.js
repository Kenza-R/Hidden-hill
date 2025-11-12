document.addEventListener("DOMContentLoaded", () => {
  document.body.classList.add("js-enabled");

  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const headerOffset = 160;
  const sections = Array.from(document.querySelectorAll("[data-section]"));
  const navLinks = Array.from(document.querySelectorAll("[data-nav-link]"));
  const scrollTriggers = Array.from(document.querySelectorAll("[data-scroll-to]"));

  function getSectionIdFromLink(link) {
    const href = link.getAttribute("href");
    if (!href || !href.startsWith("#") || href.length <= 1) return null;
    return decodeURIComponent(href.slice(1));
  }

  function updateActiveNav() {
    if (!sections.length || !navLinks.length) return;
    const scrollPosition = window.scrollY + headerOffset;

    let currentSectionId = sections[0]?.id ?? null;

    for (const section of sections) {
      if (scrollPosition >= section.offsetTop) {
        currentSectionId = section.id;
      } else {
        break;
      }
    }

    navLinks.forEach((link) => {
      const targetId = getSectionIdFromLink(link);
      const isActive = targetId === currentSectionId;
      link.classList.toggle("is-active", isActive);
      if (isActive) {
        link.setAttribute("aria-current", "page");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  }

  let ticking = false;
  window.addEventListener(
    "scroll",
    () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          updateActiveNav();
          ticking = false;
        });
        ticking = true;
      }
    },
    { passive: true },
  );

  updateActiveNav();

  navLinks.forEach((link) => {
    const targetId = getSectionIdFromLink(link);
    if (!targetId) return;

    link.addEventListener("click", (event) => {
      const targetSection = document.getElementById(targetId);
      if (!targetSection) return;

      event.preventDefault();

      if (prefersReducedMotion) {
        targetSection.scrollIntoView();
      } else {
        window.scrollTo({
          top: targetSection.offsetTop - 100,
          behavior: "smooth",
        });
      }
    });
  });

  scrollTriggers.forEach((trigger) => {
    const targetId = trigger.getAttribute("data-scroll-to");
    if (!targetId) return;

    trigger.addEventListener("click", (event) => {
      const targetSection = document.getElementById(targetId);
      if (!targetSection) return;

      event.preventDefault();

      if (prefersReducedMotion) {
        targetSection.scrollIntoView();
      } else {
        window.scrollTo({
          top: targetSection.offsetTop - 100,
          behavior: "smooth",
        });
      }
    });
  });
});

