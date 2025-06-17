// Funcionalidad de INICIO.HTML
document.addEventListener('DOMContentLoaded', () => {
    const carouselData = [
        {
            title: "El RPG del Año",
            description: "Sumérgete en un vasto mundo de fantasía con una historia épica y combates intensos.",
            image: "https://placehold.co/1200x675/A0522D/FFFFFF?text=RPG+Aventura" // Proporción 16:9
        },
        {
            title: "Acción Sin Límites",
            description: "Adrenalina pura en este shooter frenético con gráficos de nueva generación.",
            image: "https://placehold.co/1200x675/2F4F4F/FFFFFF?text=Accion+Frenetica"
        },
        {
            title: "Rompecabezas Mental",
            description: "Desafía tu ingenio con los rompecabezas más intrincados y originales.",
            image: "https://placehold.co/1200x675/4682B4/FFFFFF?text=Juego+Rompecabezas"
        },
        {
            title: "Simulador Urbano",
            description: "Construye y gestiona tu propia metrópolis desde cero.",
            image: "https://placehold.co/1200x675/6B8E23/FFFFFF?text=Simulador+Ciudad"
        },
            {
            title: "Deportes Extremos",
            description: "Conviértete en el campeón definitivo en el deporte que más te apasiona.",
            image: "https://placehold.co/1200x675/CD5C5C/FFFFFF?text=Deportes+Extremos"
        }
    ];

    let currentIndex = 0;
    const mainDisplay = document.getElementById('mainCarouselDisplay');
    const thumbnailsContainer = document.getElementById('carouselThumbnails');
    const upBtn = document.getElementById('carouselUpBtn');
    const downBtn = document.getElementById('carouselDownBtn');
    let autoSlideInterval;

    function renderCarousel() {
        mainDisplay.innerHTML = ''; // Limpiar el display principal
        thumbnailsContainer.innerHTML = ''; // Limpiar thumbnails

        carouselData.forEach((item, index) => {
            // Crear el ítem del carrusel principal
            const mainItem = document.createElement('div');
            mainItem.className = `carousel-item absolute inset-0 transition-opacity duration-500 ease-in-out ${index === currentIndex ? 'active opacity-100' : 'opacity-0'}`;
            mainItem.innerHTML = `
                <img src="${item.image}" alt="${item.title}" class="w-full h-full object-cover rounded-lg">
                <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent p-6 text-white rounded-b-lg">
                    <h4 class="text-3xl font-bold mb-2">${item.title}</h4>
                    <p class="text-lg">${item.description}</p>
                </div>
            `;
            mainDisplay.appendChild(mainItem);

            // Crear el thumbnail
            const thumbnail = document.createElement('div');
            thumbnail.className = `thumbnail-item rounded-md overflow-hidden w-full aspect-w-16 aspect-h-9 ${index === currentIndex ? 'active' : ''}`;
            thumbnail.innerHTML = `
                <img src="${item.image}" alt="${item.title}" class="w-full h-full object-cover rounded-md">
            `;
            thumbnail.addEventListener('click', () => showSlide(index));
            thumbnailsContainer.appendChild(thumbnail);
        });

        updateThumbnailScroll(); // Asegura que el thumbnail activo esté visible
    }

    function showSlide(index) {
        currentIndex = (index + carouselData.length) % carouselData.length; // Asegura que el índice esté dentro del rango
        renderCarousel(); // Volver a renderizar para actualizar activos
        resetAutoSlide(); // Reiniciar el temporizador al cambiar manualmente
    }

    function nextSlide() {
        showSlide(currentIndex + 1);
    }

    function prevSlide() {
        showSlide(currentIndex - 1);
    }

    function updateThumbnailScroll() {
        const activeThumbnail = thumbnailsContainer.querySelector('.thumbnail-item.active');
        if (activeThumbnail) {
            // Centrar el thumbnail activo en el contenedor de thumbnails
            thumbnailsContainer.scrollTop = activeThumbnail.offsetTop - (thumbnailsContainer.offsetHeight / 2) + (activeThumbnail.offsetHeight / 2);
        }
    }

    function startAutoSlide() {
        autoSlideInterval = setInterval(nextSlide, 5000); // Cambia cada 5 segundos
    }

    function resetAutoSlide() {
        clearInterval(autoSlideInterval);
        startAutoSlide();
    }

    // Asignar eventos a los botones de navegación
    upBtn.addEventListener('click', prevSlide);
    downBtn.addEventListener('click', nextSlide);

    // Iniciar el carrusel al cargar la página
    renderCarousel();
    startAutoSlide();
});

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