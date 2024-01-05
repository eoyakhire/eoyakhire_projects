let currentIndex = 0;
const carousel = document.querySelector('.carousel');
const dots = document.querySelectorAll('.dot');
          
function showImage(index) {
    const translateValue = -index * 100 + '%';
    carousel.style.transform = 'translateX(' + translateValue + ')';
}

function setActiveDot(index) {
    dots.forEach(dot => dot.classList.remove('active'));
    dots[index].classList.add('active');
}

function nextImage() {
    currentIndex = (currentIndex + 1) % 3;
    showImage(currentIndex);
    setActiveDot(currentIndex);
}

function prevImage() {
    currentIndex = (currentIndex - 1 + 3) % 3;
    showImage(currentIndex);
    setActiveDot(currentIndex);
}

dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
        currentIndex = index;
        showImage(currentIndex);
        setActiveDot(currentIndex);
    });
});

setInterval(nextImage, 3000); // Auto change image every 3 seconds