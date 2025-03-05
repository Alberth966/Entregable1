// Función para alternar entre las imágenes de cada sección
function toggleImages(className) {
    let images = document.querySelectorAll(className);
    let index = 0;
    
    setInterval(() => {
        images.forEach(img => img.classList.remove("active"));
        images[index].classList.add("active");
        index = (index + 1) % images.length;
    }, 3000); // Cambia la imagen cada 3 segundos
}

// Llamar la función para cada categoría
document.addEventListener("DOMContentLoaded", () => {
    toggleImages(".filtro-img");
    toggleImages(".ruedas-img");
    toggleImages(".fundas-img");
    toggleImages(".mangueras-img");
});
