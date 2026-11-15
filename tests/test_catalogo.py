from pages.inventory_page import PaginaInventario
from pages.login_page import PaginaInicioSesion


def test_catalogo_carga_productos(navegador):
    pagina_inicio_sesion = PaginaInicioSesion(navegador)
    pagina_inicio_sesion.abrir_pagina_inicio_sesion()
    pagina_inicio_sesion.iniciar_sesion("standard_user", "secret_sauce")

    pagina_inventario = PaginaInventario(navegador)
    nombres_productos = pagina_inventario.obtener_nombres_productos()

    assert navegador.title == "Swag Labs"
    assert len(nombres_productos) >= 1, "No se encontro ningun producto cargado"
    assert pagina_inventario.obtener_cantidad_productos() > 0
    assert pagina_inventario.menu_es_visible() is True
    assert pagina_inventario.desplegable_orden_es_visible() is True
