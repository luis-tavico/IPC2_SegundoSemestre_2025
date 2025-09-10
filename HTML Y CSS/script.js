document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("contact-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita que la pagina se recargue

        // Obtener los valores de los campos
        const nombre = document.getElementById("nombre").value.trim();
        const email = document.getElementById("email").value.trim();
        const mensaje = document.getElementById("mensaje").value.trim();

        // Validaciones
        if (nombre === "" || email === "" || mensaje === "") {
            alert("Por favor completa todos los campos.");
            return;
        }

        if (!validarEmail(email)) {
            alert("El correo electrónico no es valido.");
            return;
        }

        alert("¡Gracias por contactarnos, " + nombre + "! Tu mensaje ha sido enviado.");

        // Limpiar el formulario
        form.reset();
    });

    // Funcion para validar el correo con regex
    function validarEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }
});