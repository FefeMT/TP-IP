
//SPINNER PARA LAS SECCIONES

document.addEventListener('DOMContentLoaded', function () {
    // Elementos del DOM necesarios
    const spinner = document.getElementById('spinner');
    const links = document.querySelectorAll('a.nav-link');

    // Verifica si el spinner existe
    if (!spinner) {
        console.error('Spinner element not found.');
        return;
    }

    // Agrega el evento 'click' para los enlaces de navegación
    links.forEach(link => {
        link.addEventListener('click', function (event) {
            // Evita comportamiento por defecto si el link es inválido
            if (!link.href || link.href === '#') {
                return;
            }

            // Muestra el spinner antes de redirigir
            spinner.style.display = 'flex';
        });
    });

    // Asegura que el spinner desaparezca al cargar la nueva página
    window.addEventListener('load', function () {
        spinner.style.display = 'none';
    });
});

//SPINNER PARA EL BUSCADOR

document.addEventListener('DOMContentLoaded', function () {
    // Mostrar el spinner cuando se envía el formulario de búsqueda
    const searchForm = document.getElementById('searchForm');
    if (searchForm) {
        searchForm.addEventListener('submit', function (e) {
            // Mostrar el spinner al hacer submit
            document.getElementById('spinner').style.display = 'flex';
        });
    }

    function hideSpinner() {
        document.getElementById('spinner').style.display = 'none';
    }
});
