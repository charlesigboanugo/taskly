export function initMessages() {
    const msg = document.querySelector('.messages');

    setTimeout(() => {
        if (msg) msg.classList.add('hide');
    }, 5000);
}