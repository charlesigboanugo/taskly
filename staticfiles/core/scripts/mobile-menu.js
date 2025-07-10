 export function initMobilemenu() {
    const burger = document.getElementById("burger");

    burger.addEventListener("click", () => {
        const mobile_menu = document.querySelector('.mobile-menu');
        mobile_menu.classList.toggle('mobile-menu-active'); 
        if (burger.classList.contains('fa-burger')) {
            burger.classList.replace('fa-burger', 'fa-xmark');
            } else {
            burger.classList.replace('fa-xmark', 'fa-burger');
        }
    });
 }
 