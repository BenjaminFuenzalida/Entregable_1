document.addEventListener('DOMContentLoaded', function() {
  var cartButtons = document.querySelectorAll('[data-bs-toggle="offcanvas"]');

  // Manejo del evento click en los botones de "Agregar al carrito"
  cartButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      var product = button.getAttribute('data-product');
      var price = button.getAttribute('data-price');
      var offcanvasTarget = button.getAttribute('data-bs-target');
      addToCart(product, price, offcanvasTarget);
    });
  });

  // Función para agregar elementos al carrito específico del offcanvas
  function addToCart(product, price, offcanvasTarget) {
    var newItem = document.createElement('div');
    newItem.className = 'cart-item';
    
    var productName = document.createElement('span');
    productName.textContent = product;
    newItem.appendChild(productName);

    var productPrice = document.createElement('span');
    productPrice.textContent = ' - Precio: ' + price + ' USD'; // Ajustar el formato según tu necesidad
    newItem.appendChild(productPrice);

    var removeButton = document.createElement('button');
    removeButton.textContent = 'Eliminar';
    removeButton.className = 'btn btn-sm btn-danger ms-2';
    removeButton.addEventListener('click', function() {
      newItem.remove();
    });

    newItem.appendChild(removeButton);

    var offcanvasBody = document.querySelector(offcanvasTarget + ' .offcanvas-body');
    if (offcanvasBody) {
      offcanvasBody.appendChild(newItem);
    } else {
      console.error('Elemento offcanvasBody no encontrado para ' + offcanvasTarget);
    }
  }

  // Event listener para limpiar el carrito dentro de cada offcanvas
  var clearCartBtns = document.querySelectorAll('.offcanvas .btn-clear-cart');
  clearCartBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var offcanvasBody = btn.closest('.offcanvas').querySelector('.offcanvas-body');
      var cartItems = offcanvasBody.querySelectorAll('.cart-item');
      cartItems.forEach(function(item) {
        item.remove();
      });
    });
  });

});
