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

// Funcionalidad de CARRITO.HTML

// Función de ejemplo para actualizar un ítem del carrito
// En una aplicación real, esto haría una llamada a la API del backend
function updateCartItem(itemId, newQuantity) {
    console.log(`Actualizando ítem ${itemId} a cantidad: ${newQuantity}`);
    // Aquí iría la lógica para enviar la actualización al backend
    // y luego re-renderizar los totales o el ítem específico.
}

// Simula la carga de ítems del carrito (en una aplicación real, se obtendría del backend)
const cartItems = [
    { id: 1, name: "Aventura Épica", price: 29.99, quantity: 1, imageUrl: "https://placehold.co/100x100/FF5733/FFFFFF?text=Juego1" },
    { id: 2, name: "Simulador Urbano", price: 19.99, quantity: 2, imageUrl: "https://placehold.co/100x100/33FF57/FFFFFF?text=Juego2" },
    // Puedes añadir más ítems de ejemplo aquí
];

function renderCart() {
    const container = document.getElementById('cartItemsContainer');
    const subtotalAmountSpan = document.getElementById('subtotalAmount');
    const totalAmountSpan = document.getElementById('totalAmount');
    const emptyCartMessage = document.getElementById('emptyCartMessage');

    container.innerHTML = ''; // Limpiar el contenedor antes de renderizar

    let subtotal = 0;

    if (cartItems.length === 0) {
        emptyCartMessage.classList.remove('hidden');
    } else {
        emptyCartMessage.classList.add('hidden');
        cartItems.forEach(item => {
            const itemSubtotal = item.price * item.quantity;
            subtotal += itemSubtotal;

            const itemDiv = document.createElement('div');
            itemDiv.className = 'flex items-center bg-gray-700 p-4 rounded-lg shadow-md';
            itemDiv.innerHTML = `
                <img src="${item.imageUrl}" alt="${item.name}" class="w-24 h-24 object-cover rounded-md mr-4">
                <div class="flex-grow">
                    <h3 class="text-xl font-semibold text-gray-100">${item.name}</h3>
                    <p class="text-gray-300">Precio Unitario: <span class="font-bold">$${item.price.toFixed(2)}</span></p>
                    <div class="flex items-center mt-2">
                        <label for="quantity-${item.id}" class="mr-2 text-gray-300">Cantidad:</label>
                        <input type="number" id="quantity-${item.id}" value="${item.quantity}" min="1"
                                class="w-16 p-2 rounded-md bg-gray-600 text-gray-100 border border-gray-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                                onchange="updateItemQuantity(${item.id}, this.value)">
                    </div>
                </div>
                <div class="text-right">
                    <p class="text-lg font-bold text-blue-300">Subtotal: $${itemSubtotal.toFixed(2)}</p>
                    <button onclick="removeItem(${item.id})" class="text-red-400 hover:text-red-500 transition duration-200 ease-in-out mt-2 text-sm">
                        Eliminar
                    </button>
                </div>
            `;
            container.appendChild(itemDiv);
        });
    }
    
    subtotalAmountSpan.textContent = `$${subtotal.toFixed(2)}`;
    totalAmountSpan.textContent = `$${subtotal.toFixed(2)}`; // Asumiendo envío gratis por ahora
}

function updateItemQuantity(itemId, newQuantity) {
    const itemIndex = cartItems.findIndex(item => item.id === itemId);
    if (itemIndex > -1) {
        cartItems[itemIndex].quantity = parseInt(newQuantity);
        renderCart(); // Volver a renderizar para actualizar totales y subtotales
    }
}

function removeItem(itemId) {
    const initialLength = cartItems.length;
    cartItems.splice(cartItems.findIndex(item => item.id === itemId), 1);
    if (cartItems.length < initialLength) {
        renderCart(); // Volver a renderizar si se eliminó un ítem
    }
}

// Carga el carrito cuando la página esté lista
document.addEventListener('DOMContentLoaded', renderCart);


// Funcionaliadad BUSCADOR.HTML
document.addEventListener('DOMContentLoaded', () => {
    const searchParams = new URLSearchParams(window.location.search);
    const query = searchParams.get('q'); // Obtiene el término de búsqueda de la URL
    const searchResultsContainer = document.getElementById('searchResults');
    const noResultsMessage = document.getElementById('noResults');
    const searchQueryDisplay = document.getElementById('searchQueryDisplay');
    const searchInput = document.getElementById('searchInput'); // Obtener el input de búsqueda en esta página

    // Rellenar el input de búsqueda con la query actual si existe
    if (query) {
        searchInput.value = query;
        searchQueryDisplay.textContent = `Mostrando resultados para: "${query}"`;
        fetchGames(query); // Llama a la función para obtener y mostrar los juegos
    } else {
        searchQueryDisplay.textContent = 'Por favor, introduce un término de búsqueda.';
        noResultsMessage.textContent = 'Introduce un término de búsqueda para ver resultados.';
        noResultsMessage.classList.remove('hidden');
    }

    async function fetchGames(searchQuery) {
        try {
            // Realiza la solicitud al endpoint API de tu backend
            const response = await fetch(`/api/juegos/buscar?q=${encodeURIComponent(searchQuery)}`);
            const games = await response.json(); // Parsea la respuesta JSON

            searchResultsContainer.innerHTML = ''; // Limpiar resultados anteriores
            if (games.length > 0) {
                noResultsMessage.classList.add('hidden'); // Ocultar mensaje de "no resultados"
                games.forEach(game => {
                    const gameCard = document.createElement('div');
                    gameCard.className = 'bg-white rounded-lg shadow-md overflow-hidden transform hover:scale-105 transition duration-300 ease-in-out relative';

                    let offerBadge = '';
                    let displayPrice = game.precio;
                    if (game.en_oferta && game.porcentaje_oferta > 0) {
                        // Calcula el precio con descuento
                        const discountedPrice = game.precio * (1 - game.porcentaje_oferta / 100);
                        offerBadge = `
                            <span class="absolute top-2 right-2 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded-full">
                                -${game.porcentaje_oferta}%
                            </span>
                        `;
                        displayPrice = discountedPrice.toFixed(2); // Formatear a 2 decimales
                    }

                    // Construye el HTML para cada tarjeta de juego
                    gameCard.innerHTML = `
                        ${offerBadge}
                        <img src="${game.direccion_imagen || 'https://placehold.co/600x400/CCCCCC/000000?text=Imagen+No+Disponible'}"
                                alt="${game.nombre}" class="w-full h-48 object-cover">
                        <div class="p-4">
                            <h3 class="text-xl font-semibold mb-2">${game.nombre}</h3>
                            <p class="text-gray-700 font-bold text-lg">
                                Precio: $${displayPrice}
                                ${game.en_oferta && game.porcentaje_oferta > 0 ? `<span class="line-through text-gray-500 text-sm ml-2">$${game.precio.toFixed(2)}</span>` : ''}
                            </p>
                            <p class="text-gray-600 text-sm mt-2">Género: ${game.nombre_genero || 'N/A'}</p>
                            <p class="text-gray-600 text-sm">Tipo: ${game.tipo || 'N/A'}</p>
                        </div>
                    `;
                    searchResultsContainer.appendChild(gameCard); // Añade la tarjeta al contenedor de resultados
                });
            } else {
                noResultsMessage.classList.remove('hidden'); // Muestra mensaje de "no resultados"
            }
        } catch (error) {
            console.error('Error al obtener juegos:', error);
            searchResultsContainer.innerHTML = '<p class="text-red-500 text-center">Ocurrió un error al cargar los juegos. Por favor, inténtalo de nuevo más tarde.</p>';
        }
    }
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

// Funcionalidad ADMIN.HTML
function toggleEnOferta(juegoId, enOfertaActual, btn) {
    fetch(`/admin/toggle_oferta/${juegoId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ en_oferta: !enOfertaActual })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            btn.textContent = data.nuevo_valor ? 'Sí' : 'No';
            btn.setAttribute('onclick', `toggleEnOferta('${juegoId}', ${data.nuevo_valor}, this)`);
        } else {
            alert('Error al actualizar');
        }
    });
}

function editarPorcentaje(id) {
    const celda = document.getElementById('porcentaje-' + id);
    const valorActual = celda.textContent.replace('%', '').trim();
    celda.innerHTML = `
        <input type="number" id="input-porcentaje-${id}" value="${valorActual}" min="0" max="100" class="w-16 text-black rounded px-1">
        <button onclick="guardarPorcentaje('${id}')" class="ml-2 px-2 py-1 bg-green-500 text-white rounded">OK</button>
    `;
}

function guardarPorcentaje(id) {
    const input = document.getElementById('input-porcentaje-' + id);
    const nuevoValor = input.value;
    const celda = document.getElementById('porcentaje-' + id);
    celda.textContent = nuevoValor + '%';
}