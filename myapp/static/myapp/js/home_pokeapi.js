

$(document).ready(function() {
    $('#BotonBuscar').on('click', function() {
        const pokemonName = $('#pokemonName').val().toLowerCase().trim();

        if (pokemonName === '') {
            showErrorModal('Por favor ingrese el nombre de un pokemon.');
            return;
        }


        const url =`https://pokeapi.co/api/v2/pokemon/${pokemonName}/`;

        $.ajax({
            url: url,
            method: 'GET',
            success: function(data) {
                const abilities = data.abilities;
                const abilitiesList = $('#abilitiesList');
                abilitiesList.empty(); // Limpia la lista 

                abilities.forEach(function(ability,await) {
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

            //Funcion para mostrar el nombre del pokemom
        $.ajax({
            url: url,
            method: 'GET',
            success: function(data) {
                const name = data.name;
                const pokemonDiv = $('#pokemonDiv');
                pokemonDiv.empty(); // Limpiar contenido previo

                const nameElement = $('<H2>').text(`${name}!!`);
                pokemonDiv.append(nameElement);
            },
            error: function() {
                const pokemonDiv = $('#pokemonDiv');
                pokemonDiv.empty(); // Limpiar contenido previo
                const errorElement = $('<p>').text('No se pudo encontrar el Pokémon.');
                pokemonDiv.append(errorElement);
            }

            
        });
});
    $('#BotonLimpiar').on('click', function() {

        limpiarBusqueda();
    });
        function limpiarBusqueda() {
            const imagen = 
            $('#pokemonName').val(''); // Limpiar el campo de entrada
            $('#abilitiesList').empty(); // Limpiar Habilidades
            $('#pokemonDiv').empty(); // Limpiar el contenido mostrado del nombre
            $('#pokemonImage').attr('src', '/static/myapp/images/pokemon-3418266_640.png') // Limpia y devuelve la imagen predeterminada
            .css({
                'width': '400px',
                'height': '400px',
                'object-fit': 'cover'
            });
        }

    });

// Funcion para mostrar sugerencias de Pokemon
function mostrarSugerencias(query) {
    const suggestions = allPokemon.filter(pokemon => pokemon.name.startsWith(query)).slice(0, 10);
    const suggestionsDiv = document.getElementById('suggestions');
    suggestionsDiv.innerHTML = '';
    suggestions.forEach(pokemon => {
    const div = document.createElement('div');
    div.textContent = pokemon.name;
    div.addEventListener('click', function() {
        document.getElementById('pokemonName').value = pokemon.name;
        suggestionsDiv.innerHTML = '';
    });
    suggestionsDiv.appendChild(div);
    });
    }

    function showErrorModal(message) {
        $('#errorMessage').text(message);
        $('#errorModal').modal('show');
    }

document.getElementById('pokemonName').addEventListener('input', function() {
    const query = this.value.toLowerCase();
    mostrarSugerencias(query);
});




// Función para llenar la lista de todos los Pokemon
async function obtenerTodosLosPokemon() {
    try {
        const response = await fetch('https://pokeapi.co/api/v2/pokemon?limit=1000'); // Obtener hasta 1000 Pokemon
        const data = await response.json();
        allPokemon = data.results;
    } catch (error) {
        console.error('Error al obtener la lista de Pokémon:', error);
    }
}

// Llamar a la funcion para obtener todos los Pokemon al cargar la pagina
obtenerTodosLosPokemon();