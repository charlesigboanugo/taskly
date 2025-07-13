export function initMessages() {
    const msg = document.querySelector('.messages');
    const errlist = document.querySelectorAll('.errorlist');

    setTimeout(() => {
        if (msg) msg.classList.add('hide');
        errlist.forEach(el => el.classList.add('hide'));
    }, 6000);
}