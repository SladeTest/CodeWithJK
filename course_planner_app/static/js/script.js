// Scroll-triggered animations
document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate__fadeInUp');
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.card-glass, .img-fluid').forEach(el => {
        el.classList.add('animate__animated');
        observer.observe(el);
    });
});