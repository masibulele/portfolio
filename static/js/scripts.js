function toggleMenu(forceOpen) {
    const menu = document.querySelector(".menu-links");
    const button = document.querySelector(".hamburger-icon");
    const isOpen = forceOpen ?? !menu.classList.contains("open");

    menu.classList.toggle("open", isOpen);
    button.classList.toggle("open", isOpen);
    button.setAttribute("aria-expanded", String(isOpen));
    button.setAttribute("aria-label", isOpen ? "Close navigation menu" : "Open navigation menu");
}

document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
    button.addEventListener("click", () => {
        const theme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
        document.documentElement.dataset.theme = theme;
        localStorage.setItem("portfolio-theme", theme);
        updateThemeButtons(theme);
    });
});

function updateThemeButtons(theme) {
    document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
        const isDark = theme === "dark";
        button.setAttribute("aria-pressed", String(isDark));
        button.setAttribute("aria-label", `Switch to ${isDark ? "light" : "dark"} mode`);
        button.querySelector(".theme-toggle-icon").textContent = isDark ? "☀" : "☾";
        button.querySelector(".theme-toggle-label").textContent = `${isDark ? "Light" : "Dark"} mode`;
    });
}

updateThemeButtons(document.documentElement.dataset.theme);

document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        toggleMenu(false);
    }
});