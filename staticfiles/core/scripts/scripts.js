window.onload = () => {
    setTimeout(() => {
        const msg = document.querySelector('.messages');
        if (msg) msg.classList.add('hide');
    }, 5000);

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
};