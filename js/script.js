function toggleImages(className) {
    let images = document.querySelectorAll(className);
    let index = 0;

    if (images.length === 0) {
        console.warn("No se encontraron imágenes con la clase: " + className);
        return;
    }

    setInterval(() => {
        images.forEach(img => img.classList.remove("active"));
        images[index].classList.add("active");
        index = (index + 1) % images.length;
    }, 3000); 
}

document.addEventListener("DOMContentLoaded", () => {
    toggleImages(".filtro-img");
    toggleImages(".ruedas-img");
    toggleImages(".fundas-img");
    toggleImages(".mangueras-img");
});
