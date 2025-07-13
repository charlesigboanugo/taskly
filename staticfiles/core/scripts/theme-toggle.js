const html = document.documentElement;
const dark_toggle = document.querySelector("[data-toggle='theme-dark']");
const light_toggle = document.querySelector("[data-toggle='theme-light']");
    
function storeTheme(val){
    localStorage.setItem('theme', val);
}

function darkMode(){
    const data_theme = html.getAttribute("data-theme");
    if (data_theme == "light" || data_theme == null){
     html.setAttribute("data-theme", "dark");
        if (light_toggle)
            light_toggle.classList.toggle("theme-active", false);
        if (dark_toggle)
        {
            dark_toggle.classList.toggle("theme-active", true);
            storeTheme("dark");
        }
    }
}

function lightMode(){
    const data_theme = html.getAttribute("data-theme");
    if (data_theme == "dark" || data_theme == null){
     html.setAttribute("data-theme", "light");
        if (dark_toggle)
            dark_toggle.classList.toggle("theme-active", false);
        if (light_toggle)
        {
            light_toggle.classList.toggle("theme-active", true);
            storeTheme("light");
        }
    }
}

export function initThemeToggle() {
    dark_toggle.addEventListener("click", darkMode);
    light_toggle.addEventListener("click", lightMode);
}