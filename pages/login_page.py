from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import PaginaBase


class PaginaInicioSesion(PaginaBase):
    URL = "https://www.saucedemo.com/"
    INPUT_USUARIO = (By.ID, "user-name")
    INPUT_CONTRASENA = (By.ID, "password")
    BOTON_INICIO_SESION = (By.ID, "login-button")
    MENSAJE_ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    LOGO_APP = (By.CLASS_NAME, "app_logo")
    TITULO_PRODUCTOS = (By.CSS_SELECTOR, "[data-test='title']")

    def abrir_pagina_inicio_sesion(self):
        self.abrir(self.URL)

    def iniciar_sesion(self, nombre_usuario: str, contrasena: str):
        self.escribir_texto(*self.INPUT_USUARIO, nombre_usuario)
        self.escribir_texto(*self.INPUT_CONTRASENA, contrasena)
        self.hacer_clic(*self.BOTON_INICIO_SESION)
        self.wait.until(EC.any_of(
            EC.url_contains("inventory.html"),
            EC.visibility_of_element_located(self.MENSAJE_ERROR),
        ))

    def obtener_mensaje_error(self) -> str:
        return self.buscar(*self.MENSAJE_ERROR).text

    def es_error_visible(self) -> bool:
        return self.es_visible(*self.MENSAJE_ERROR)

    def obtener_texto_logo(self) -> str:
        return self.buscar(*self.LOGO_APP).text

    def obtener_titulo_productos(self) -> str:
        return self.buscar(*self.TITULO_PRODUCTOS).text
