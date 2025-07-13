const html = document.documentElement;
const dark_toggle = document.querySelector("[data-toggle='theme-dark']");
const light_toggle = document.querySelector("[data-toggle='theme-light']");
    
function storeTheme(val){
    localStorage.setItem('theme', val);
}

function styleToggles(data_theme) {
    if (data_theme == "light"){
        if (light_toggle)
            light_toggle.classList.toggle("theme-active", true);
        if (dark_toggle)
            dark_toggle.classList.toggle("theme-active", false);
    }
    else if (data_theme == "dark"){
        if (dark_toggle)
            dark_toggle.classList.toggle("theme-active", true);
        if (light_toggle)
            light_toggle.classList.toggle("theme-active", false);
    }
}
function darkMode(){
    const data_theme = html.getAttribute("data-theme");
    if (data_theme == "light" || data_theme == null){
        html.setAttribute("data-theme", "dark");
        styleToggles("dark");
    }
    storeTheme("dark");
}

function lightMode(){
    const data_theme = html.getAttribute("data-theme");
    if (data_theme == "dark" || data_theme == null){
        html.setAttribute("data-theme", "light");
        styleToggles("light");
    }
    storeTheme("light");
}

export function initThemeToggle() {
    const data_theme = html.getAttribute("data-theme");

    styleToggles(data_theme);
    dark_toggle.addEventListener("click", darkMode);
    light_toggle.addEventListener("click", lightMode);
}