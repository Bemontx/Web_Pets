document.addEventListener("DOMContentLoaded", function() {
    const container = document.querySelector('.container');
    const redirectUrl = container.getAttribute('data-url');

    setTimeout(function() {
        document.body.classList.add('fade-out');
    }, 2500);

    setTimeout(function() {
        window.location.href = redirectUrl;
    }, 4000);
});