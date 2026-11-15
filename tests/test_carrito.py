from pages.cart_page import PaginaCarrito
from pages.inventory_page import PaginaInventario
from pages.login_page import PaginaInicioSesion


def test_agregar_producto_al_carrito(navegador):
    pagina_inicio_sesion = PaginaInicioSesion(navegador)
    pagina_inicio_sesion.abrir_pagina_inicio_sesion()
    pagina_inicio_sesion.iniciar_sesion("standard_user", "secret_sauce")

    pagina_inventario = PaginaInventario(navegador)
    assert pagina_inventario.obtener_valor_insignia_carrito() == 0

    pagina_inventario.agregar_producto_por_nombre("Sauce Labs Backpack")
    assert pagina_inventario.obtener_valor_insignia_carrito() == 1

    pagina_inventario.ir_al_carrito()
    assert navegador.current_url == "https://www.saucedemo.com/cart.html"

    pagina_carrito = PaginaCarrito(navegador)
    assert "Sauce Labs Backpack" in pagina_carrito.obtener_nombres_productos_carrito()
