export function initMessages() {
    const msg = document.querySelector('.messages');
    const errlist = document.querySelectorAll('.errorlist');

    setTimeout(() => {
        if (msg) msg.classList.add('hide');
    }, 6000);
    

    errlist.forEach((el, i) => {
        setTimeout(() => {
            el.scrollIntoView({ behavior: 'smooth', block: 'center' }); 
        },i * 3000);
    });

    setTimeout(() => {
        errlist.forEach(el => el.classList.add('hide'));
    }, 15000);
}