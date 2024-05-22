(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            }
        }
    });


    // Product Quantity
    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });
    
})(jQuery);

// Conexión con API_PRODUCTOS
// GET
async function fetchProducts() {
    const response = await fetch('http://127.0.0.1:5000/listado/');
    const products = await response.json();
    const productList = document.getElementById('product-list');
    productList.innerHTML = '';
    products.forEach(product => {
        const productItem = document.createElement('div');
        productItem.innerHTML = `ID: ${product.id}, Nombre: ${product.nombre}, Precio: ${product.precio}, Stock: ${product.stock}`;
        productList.appendChild(productItem);
    });
}

// ADD
document.getElementById('addProductForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const nombre = document.getElementById('nombre').value;
    const imagen = document.getElementById('imagen').value;
    const tipo_id = document.getElementById('tipo_id').value;
    const precio = document.getElementById('precio').value;
    const stock = document.getElementById('stock').value;

    const newProduct = {
        nombre: nombre,
        imagen: imagen,
        tipo_id: parseInt(tipo_id),
        precio: parseInt(precio),
        stock: parseInt(stock)
    };

    const response = await fetch('http://127.0.0.1:5000/addProduct/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newProduct)
    });

    if (response.ok) {
        alert('Producto agregado correctamente');
        fetchProducts();
    } else {
        alert('Error al agregar el producto');
    }
});

// UPDATE
document.getElementById('updateProductForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const id = document.getElementById('update-id').value;
    const nombre = document.getElementById('update-nombre').value;
    const imagen = document.getElementById('update-imagen').value;
    const tipo_id = document.getElementById('update-tipo_id').value;
    const precio = document.getElementById('update-precio').value;
    const stock = document.getElementById('update-stock').value;

    const updatedProduct = {
        id: parseInt(id),
        nombre: nombre,
        imagen: imagen,
        tipo_id: parseInt(tipo_id),
        precio: parseInt(precio),
        stock: parseInt(stock)
    };

    const response = await fetch('http://127.0.0.1:5000/updateProd/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedProduct)
    });

    if (response.ok) {
        alert('Producto actualizado correctamente');
        fetchProducts();
    } else {
        alert('Error al actualizar el producto');
    }
});

// DELETE
document.getElementById('deleteProductForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const id = document.getElementById('delete-id').value;

    const response = await fetch(`http://127.0.0.1:5000/delete/${id}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        alert('Producto eliminado correctamente');
        fetchProducts();
    } else {
        alert('Error al eliminar el producto');
    }
});

fetchProducts();