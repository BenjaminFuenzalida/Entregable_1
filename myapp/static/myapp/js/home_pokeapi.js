$(document).ready(function() {
    $('#searchButton').on('click', function() {
        const pokemonName = $('#pokemonName').val().toLowerCase().trim();

        if (pokemonName === '') {
            showErrorModal('Por favor ingrese el nombre de un pokemon.');
            return;
        }

        const url = `https://pokeapi.co/api/v2/pokemon/${pokemonName}/`;

        $.ajax({
            url: url,
            method: 'GET',
            success: function(data) {
                const abilities = data.abilities;
                const abilitiesList = $('#abilitiesList');
                abilitiesList.empty(); // Limpia la lista 

                abilities.forEach(function(ability) {
                    const abilityName = ability.ability.name;
                    const listItem = $('<li>').text(abilityName);
                    abilitiesList.append(listItem);
                });

                // Obtiene y muestra la imagen
                const imageUrl = data.sprites.other['official-artwork'].front_default;
                $('#pokemonImage').attr('src', imageUrl);
            },
            error: function(jqXHR, textStatus, errorThrown) {
                if (jqXHR.status === 404) {
                    showErrorModal('Pokemon no encontrado. Por favor intenta de nuevo.');
                } else {
                    showErrorModal(`Error: ${textStatus}`);
                }
            }
        });
    });

    function showErrorModal(message) {
        $('#errorMessage').text(message);
        $('#errorModal').modal('show');
    }
});
