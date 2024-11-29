const carousels = document.querySelectorAll('.carousel');

carousels.forEach((carousel) => {
    const slides = carousel.querySelector('.slides');
    const images = carousel.querySelectorAll('.slides img');
    let currentIndex = 0;

    // Cambio automático
    setInterval(() => {
        currentIndex = (currentIndex + 1) % images.length;
        slides.style.transform = `translateX(-${currentIndex * 100}%)`; // Corregido con las comillas invertidas y el operador *
    }, 5000);
});
