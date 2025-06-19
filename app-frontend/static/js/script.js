document.addEventListener('DOMContentLoaded', function() {
    // Carrusel
    const container = document.querySelector('.overflow-x-auto');
    const leftBtn = document.querySelector('button[aria-label="Anterior"]');
    const rightBtn = document.querySelector('button[aria-label="Siguiente"]');
    if (container && leftBtn && rightBtn) {
        rightBtn.addEventListener('click', () => {
            container.scrollBy({ left: 650, behavior: 'smooth' });
        });
        leftBtn.addEventListener('click', () => {
            container.scrollBy({ left: -650, behavior: 'smooth' });
        });
    }
    // Funcionalidad PERFIL.HTML
    const editarBtn = document.getElementById('editar-btn');
    const guardarBtn = document.getElementById('guardar-btn');
    const cancelarBtn = document.getElementById('cancelar-btn');
    const inputs = document.querySelectorAll('#perfil-form input');
    if (editarBtn && guardarBtn && cancelarBtn && inputs.length > 0) {
        editarBtn.addEventListener('click', function() {
            inputs.forEach(input => input.disabled = false);
            editarBtn.classList.add('hidden');
            guardarBtn.classList.remove('hidden');
            cancelarBtn.classList.remove('hidden');
        });

        cancelarBtn.addEventListener('click', function() {
            window.location.reload();
        });
    }

    // Funcionalidad para JUEGO.HTML
    const buyButton = document.getElementById('buyButton');
    const buyPopup = document.getElementById('buyPopup');
    const cancelBuyButton = document.getElementById('cancelBuyButton');
    if (buyButton && buyPopup && cancelBuyButton) {
        buyButton.addEventListener('click', () => {
            buyPopup.classList.remove('hidden');
        });
        cancelBuyButton.addEventListener('click', () => {
            buyPopup.classList.add('hidden');
        });
    }

    // Mostrar PopUp Agregar Metodo de Pago
    const mostrarBtn = document.getElementById('boton_mostrar_popup');
    const cancelarCargaBtn = document.getElementById('boton_cancelar_carga');
    const popup = document.getElementById('popup_metodo_pago');
    if (mostrarBtn && cancelarCargaBtn && popup) {
        mostrarBtn.onclick = function() {
            popup.classList.remove('hidden');
        };
        cancelarCargaBtn.onclick = function() {
            popup.classList.add('hidden');
        };
    }
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
