from selenium.webdriver.common.by import By

from pages.base_page import PaginaBase


class PaginaCarrito(PaginaBase):
    NOMBRES_PRODUCTOS_CARRITO = (By.CSS_SELECTOR, "div[data-test='inventory-item-name']")

    def obtener_nombres_productos_carrito(self):
        nombres = []
        for elemento in self.controlador.find_elements(*self.NOMBRES_PRODUCTOS_CARRITO):
            nombres.append(elemento.text)
        return nombres
