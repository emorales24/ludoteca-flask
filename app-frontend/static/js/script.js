// Funcionalidad INICIO.HTML
// Flechas del Carrusel
document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.overflow-x-auto');
    const leftBtn = document.querySelector('button[aria-label="Anterior"]');
    const rightBtn = document.querySelector('button[aria-label="Siguiente"]');
    
    rightBtn.addEventListener('click', () => {
        container.scrollBy({ left: 650, behavior: 'smooth' });
    });
    
    leftBtn.addEventListener('click', () => {
        container.scrollBy({ left: -650, behavior: 'smooth' });
    });
});

// Funcionalidad ADMIN.HTML
function mostrarFormularioEditar(id, precio, porcentaje, en_oferta) {
    document.getElementById('formulario-editar').classList.remove('hidden');
    document.getElementById('editar-id').value = id;
    document.getElementById('editar-precio').value = precio;
    document.getElementById('editar-porcentaje').value = porcentaje;
    document.getElementById('editar-en-oferta').value = (en_oferta === "True" || en_oferta === "1" || en_oferta === "true") ? "True" : "False";
}
function cerrarFormularioEditar() {
    document.getElementById('formulario-editar').classList.add('hidden');
}

// Funcionalidad PERFIL.HTML
document.addEventListener('DOMContentLoaded', function() {
    const editarBtn = document.getElementById('editar-btn');
    const guardarBtn = document.getElementById('guardar-btn');
    const cancelarBtn = document.getElementById('cancelar-btn');
    const inputs = document.querySelectorAll('#perfil-form input');

    editarBtn.addEventListener('click', function() {
        inputs.forEach(input => input.disabled = false);
        editarBtn.classList.add('hidden');
        guardarBtn.classList.remove('hidden');
        cancelarBtn.classList.remove('hidden');
    });

    cancelarBtn.addEventListener('click', function() {
        // Recarga la página para restaurar los valores originales
        window.location.reload();
    });
});


// Funcionalidad para JUEGO.HTML
        const buyButton = document.getElementById('buyButton');
        const buyPopup = document.getElementById('buyPopup');
        const cancelBuyButton = document.getElementById('cancelBuyButton');

        buyButton.addEventListener('click', () => {
            buyPopup.classList.remove('hidden');
        });

        cancelBuyButton.addEventListener('click', () => {
            buyPopup.classList.add('hidden');
        });


            // Aca agregué esto para ver si se podia poner una notificacion de que se compró algo, ver a lo ultimo
            // const form = document.querySelector('form');
            // const toast = document.getElementById('toast');

            // form.addEventListener('submit', (e) => {
            //     e.preventDefault(); // Evita que se recargue la página (opcional)

            //     // Oculta popup
            //     popup.classList.add('hidden');

            //     // Muestra el toast
            //     toast.classList.remove('hidden');

            //     // Oculta el toast después de 3 segundos
            //     setTimeout(() => {
            //         toast.classList.add('hidden');
            //     }, 3000);
            // });