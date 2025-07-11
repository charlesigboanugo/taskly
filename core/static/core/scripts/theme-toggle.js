const pageBody = document.body;
const dark_toggle = document.querySelector("[data-toggle='theme-dark']");
const light_toggle = document.querySelector("[data-toggle='theme-light']");
    
function storeTheme(val){
    localStorage.setItem('theme', val);
}

function defaultTheme(){
    return localStorage.getItem('theme');
}

function darkMode(){
    const data_theme = pageBody.getAttribute("data-theme");
    if (data_theme == "light" || data_theme == null){
        pageBody.setAttribute("data-theme", "dark");
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
    const data_theme = pageBody.getAttribute("data-theme");
    if (data_theme == "dark" || data_theme == null){
        pageBody.setAttribute("data-theme", "light");
        if (dark_toggle)
            dark_toggle.classList.toggle("theme-active", false);
        if (light_toggle)
        {
            light_toggle.classList.toggle("theme-active", true);
            storeTheme("light");
        }
    }
}

export function setTheme(){
    const data_theme = defaultTheme();
    if (data_theme == null || data_theme == "dark")
        darkMode();
    else{
        lightMode();
    }
}

export function initThemeToggle() {
    setTheme();
    dark_toggle.addEventListener("click", darkMode);
    light_toggle.addEventListener("click", lightMode);
}