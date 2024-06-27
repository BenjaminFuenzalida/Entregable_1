document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contactForm");
    const submitButton = document.getElementById("submitButton");
    const inputs = form.querySelectorAll("input[required]");

    function validateForm() {
        let isValid = true;
        inputs.forEach(input => {
            if (!input.checkValidity()) {
                isValid = false;
            }
        });
        submitButton.disabled = !isValid;
    }

    inputs.forEach(input => {
        input.addEventListener("input", function () {
            if (this.checkValidity()) {
                this.classList.remove("is-invalid");
                this.classList.add("is-valid");
            } else {
                this.classList.remove("is-valid");
                this.classList.add("is-invalid");
            }
            validateForm();
        });
    });

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        if (form.checkValidity()) {
           
            const successModal = new bootstrap.Modal(document.getElementById("successModal"));
            successModal.show();

            
            form.reset();
            submitButton.disabled = true;
            inputs.forEach(input => input.classList.remove("is-valid"));
        } else {
            
            inputs.forEach(input => {
                if (!input.checkValidity()) {
                    input.classList.add("is-invalid");
                }
            });
        }
    });
});
