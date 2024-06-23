$(document).ready(function(){
    let objetoRegister = {
        nombre: '',
        correo: '',
        telefono: '',
        contraseña: ''
    }

    let btnSubmit = $("#button");

    // Eventos
    $('#CORREO').on('input', validarCorreo);
    $('#NOMBRE').on('input', validarNombre);
    $('#TELEFONO').on('input', validarTelefono);
    $('#CONTRASEÑA').on('input', validarContraseña); 

    $("#button").on("click", function (e){
        e.preventDefault();

        // Validar formulario 
        if (comprobarFormulario()) {
            // Mensaje con los datos ingresados
            let mensaje = "Datos ingresados\n";
            alert(mensaje);

            // Redirigir a home
            window.location.href = "home.html";
        } 
    });

    function validarCorreo(e){
        if(e.target.id == "CORREO" && !validarEmail(e.target.value)){
            mostrarAlerta('El email no es valido', e.target.parentElement)
            objetoRegister['correo'] = ''
            return false;
        }
        limpiarAlerta(e.target.parentElement)
        objetoRegister['correo'] = e.target.value.trim().toLowerCase()
        return true;
    }

    function validarNombre(e){
        if(e.target.id == "NOMBRE" && (!esCaracter(e.target.value) || e.target.value == "")){
            mostrarAlerta('Nombre no valido', e.target.parentElement)
            objetoRegister['nombre'] = ''
            return false;
        }
        limpiarAlerta(e.target.parentElement)
        objetoRegister['nombre'] = e.target.value.trim().toLowerCase()
        return true;
    }

    function validarTelefono(e){
        if(e.target.id == "TELEFONO" && (!esNumerico(e.target.value) || e.target.value.length < 8)){
            mostrarAlerta('El telefono no es valido', e.target.parentElement)
            objetoRegister['telefono'] = ''
            return false;
        }
        limpiarAlerta(e.target.parentElement)
        objetoRegister['telefono'] = e.target.value.trim()
        return true;
    }

    function validarContraseña(e){
        if(e.target.id == "CONTRASEÑA" && !validarFortalezaContraseña(e.target.value)){
            mostrarAlerta('La contraseña no es válida', e.target.parentElement)
            objetoRegister['contraseña'] = ''
            return false;
        }
        limpiarAlerta(e.target.parentElement)
        objetoRegister['contraseña'] = e.target.value
        return true;
    }

    function validarFortalezaContraseña(contraseña){
        // Fortalecer de la contraseña
        const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        return regex.test(contraseña);
    }

    function esNumerico(referencia){
        const regex = /^[0-9]+$/;
        return regex.test(referencia);
    }

    function esCaracter(referencia){
        const regex = /^[A-Za-z]+$/;
        return regex.test(referencia);
    }

    function mostrarAlerta(mensaje, referencia){
        limpiarAlerta(referencia);
        const error = document.createElement('P');
        error.textContent = mensaje;
        error.classList.add('alerta');

        
        referencia.appendChild(error);
    }

    function limpiarAlerta(referencia){
        const alerta = referencia.querySelector('.alerta');
        if(alerta){
            alerta.remove();
        }
    }

    function validarEmail(email){
        const regex = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
        return regex.test(email);
    }

    function comprobarFormulario(){
        // Verifica si todos los campos están completos
        return Object.values(objetoRegister).every(value => value !== '');
    }
});
