
function validarFormulario(event) {
    const firstNameInput = document.getElementById('firstName');
    const lastNameInput = document.getElementById('lastName');
    const usernameInput = document.getElementById('username');
    const emailInput = document.getElementById('email');
    const addressInput = document.getElementById('address');
    const countryInput = document.getElementById('country');
    const stateInput = document.getElementById('state');
    const zipInput = document.getElementById('zip');
    const ccNameInput = document.getElementById('cc-name');
    const ccNumberInput = document.getElementById('cc-number');
    const ccExpirationInput = document.getElementById('cc-expiration');
    const ccCvvInput = document.getElementById('cc-cvv');

    if (!validateField(firstNameInput) ||
        !validateField(lastNameInput) ||
        !validateField(usernameInput) ||
        !validateField(emailInput) ||
        !validateField(addressInput) ||
        !validateField(countryInput) ||
        !validateField(stateInput) ||
        !validateField(zipInput) ||
        !validateField(ccNameInput) ||
        !validateField(ccNumberInput) ||
        !validateField(ccExpirationInput) ||
        !validateField(ccCvvInput)) {
        event.preventDefault(); 
    }
}


function validateField(input) {
    if (input.value.trim() === '') {
        alert('Por favor, completa todos los campos obligatorios.');
        return false; 
    }
    return true; 
}


const form = document.querySelector('.needs-validation');
form.addEventListener('submit', validarFormulario);
