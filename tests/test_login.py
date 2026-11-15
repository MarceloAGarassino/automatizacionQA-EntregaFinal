import json
from pathlib import Path

import pytest

from pages.login_page import PaginaInicioSesion


def cargar_datos():
    ruta_datos = Path(__file__).resolve().parents[1] / "data" / "users.json"
    with ruta_datos.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


DATOS = cargar_datos()


def test_inicio_sesion_valido(navegador):
    pagina_inicio_sesion = PaginaInicioSesion(navegador)
    pagina_inicio_sesion.abrir_pagina_inicio_sesion()
    pagina_inicio_sesion.iniciar_sesion(DATOS["valid_users"][0]["username"], DATOS["valid_users"][0]["password"])

    assert navegador.current_url == "https://www.saucedemo.com/inventory.html"
    assert pagina_inicio_sesion.obtener_texto_logo() == "Swag Labs"
    assert pagina_inicio_sesion.obtener_titulo_productos() == "Products"


@pytest.mark.parametrize(
    "nombre_usuario,contrasena",
    [
        (usuario["username"], usuario["password"]) for usuario in DATOS["invalid_users"]
    ],
    ids=["locked_user", "wrong_password"],
)
def test_inicio_sesion_invalido(navegador, nombre_usuario, contrasena):
    pagina_inicio_sesion = PaginaInicioSesion(navegador)
    pagina_inicio_sesion.abrir_pagina_inicio_sesion()
    pagina_inicio_sesion.iniciar_sesion(nombre_usuario, contrasena)

    assert pagina_inicio_sesion.es_error_visible() is True
    assert "Epic sadface" in pagina_inicio_sesion.obtener_mensaje_error()
    assert navegador.current_url == "https://www.saucedemo.com/"
