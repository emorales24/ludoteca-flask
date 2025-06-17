// Funcionalidad INICIO.HTML

// Funcionalidad de las Flechas del Carrusel
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


// Funcionalidad de BUSCADOR.HTML
document.addEventListener('DOMContentLoaded', async () => {
    const searchParams = new URLSearchParams(window.location.search);
    const query = searchParams.get('q') || '';
    const searchResultsContainer = document.getElementById('searchResults');
    const noResultsMessage = document.getElementById('noResults');
    const searchQueryDisplay = document.getElementById('searchQueryDisplay');

    // Mostrar la query en la página
    searchQueryDisplay.textContent = query ? `Mostrando resultados para: "${query}"` : 'Por favor, introduce un término de búsqueda.';
    if (!query) {
        noResultsMessage.textContent = 'Introduce un término de búsqueda para ver resultados.';
        noResultsMessage.classList.remove('hidden');
        return;
    }

    async function fetchGames(searchQuery) {
        try {
            const response = await fetch(`/buscar?q=${encodeURIComponent(searchQuery)}`);
            const games = await response.json();

            searchResultsContainer.innerHTML = ''; // Limpiar resultados anteriores
            if (games.length > 0) {
                noResultsMessage.classList.add('hidden');
                games.forEach(game => {
                    const gameCard = document.createElement('div');
                    gameCard.className = 'bg-slate-700 rounded-lg overflow-hidden shadow-lg transform hover:scale-105 transition duration-300 ease-in-out relative';

                    let offerBadge = '';
                    let displayPrice = game.precio;
                    if (game.en_oferta && game.porcentaje_oferta > 0) {
                        const discountedPrice = game.precio * (1 - game.porcentaje_oferta / 100);
                        offerBadge = `
                            <span class="absolute top-2 right-2 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded-full">
                                -${game.porcentaje_oferta}%
                            </span>
                        `;
                        displayPrice = discountedPrice.toFixed(2);
                    }

                    gameCard.innerHTML = `
                        ${offerBadge}
                        <img src="${game.direccion_imagen || 'https://placehold.co/600x400/FFD700/000000?text=' + game.nombre}"
                             alt="${game.nombre}" class="w-full h-48 object-cover">
                        <div class="p-4">
                            <h4 class="text-xl font-semibold mb-2 text-gray-300">${game.nombre}</h4>
                            <p class="text-gray-200 font-bold text-lg">
                                Precio: $${displayPrice}
                                ${game.en_oferta && game.porcentaje_oferta > 0 ? `<span class="line-through text-gray-500 text-sm ml-2">$${game.precio.toFixed(2)}</span>` : ''}
                            </p>
                            <p class="text-gray-200 text-sm mt-2">Género: ${game.nombre_genero || 'N/A'}</p>
                            <p class="text-gray-200 text-sm">Tipo: ${game.tipo || 'N/A'}</p>
                        </div>
                    `;
                    searchResultsContainer.appendChild(gameCard);
                });
            } else {
                noResultsMessage.classList.remove('hidden');
            }
        } catch (error) {
            console.error('Error al obtener juegos:', error);
            searchResultsContainer.innerHTML = '<p class="text-red-500 text-center">Ocurrió un error al cargar los juegos. Por favor, inténtalo de nuevo más tarde.</p>';
        }
    }

    await fetchGames(query);
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

// ---------------------------------------------------------------------------