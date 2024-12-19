let currentIndex = 0;

function showSlide(index, slides) {
    slides.forEach((slide, i) => {
        slide.style.display = i === index ? "block" : "none";
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".carousel img");
    const nextButton = document.querySelector("#next");
    const prevButton = document.querySelector("#prev");

    if (slides.length > 0) {
        showSlide(currentIndex, slides);

        nextButton.addEventListener("click", () => {
            currentIndex = (currentIndex + 1) % slides.length;
            showSlide(currentIndex, slides);
        });

        prevButton.addEventListener("click", () => {
            currentIndex = (currentIndex - 1 + slides.length) % slides.length;
            showSlide(currentIndex, slides);
        });
    }
});
