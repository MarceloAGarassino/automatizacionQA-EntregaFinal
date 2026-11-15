import time

from selenium.webdriver.common.by import By

from pages.base_page import PaginaBase


class PaginaInventario(PaginaBase):
    BOTON_MENU = (By.ID, "react-burger-menu-btn")
    DESPLEGABLE_ORDEN = (By.CSS_SELECTOR, "select[data-test='product-sort-container']")
    PRODUCTOS = (By.CLASS_NAME, "inventory_item")
    ENLACES_PRODUCTOS = (By.CSS_SELECTOR, "a[id^='item_'][id$='_title_link']")
    INSIGNIA_CARRITO = (By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']")
    ENLACE_CARRITO = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    ID_BOTON_POR_PRODUCTO = {
        "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
        "Sauce Labs Bike Light": "add-to-cart-sauce-labs-bike-light",
    }

    def menu_es_visible(self) -> bool:
        return self.es_visible(*self.BOTON_MENU)

    def desplegable_orden_es_visible(self) -> bool:
        return self.es_visible(*self.DESPLEGABLE_ORDEN)

    def obtener_cantidad_productos(self) -> int:
        return len(self.buscar_todos(*self.PRODUCTOS))

    def obtener_nombres_productos(self):
        nombres = []
        for elemento in self.buscar_todos(*self.ENLACES_PRODUCTOS):
            nombres.append(elemento.text)
        return nombres

    def agregar_producto_por_nombre(self, nombre_producto: str):
        id_boton = self.ID_BOTON_POR_PRODUCTO[nombre_producto]
        self.wait.until(lambda controlador: controlador.find_element(By.ID, id_boton).is_enabled())
        self.hacer_clic(By.ID, id_boton)

    def obtener_valor_insignia_carrito(self):
        tiempo_final = time.time() + 5
        while time.time() < tiempo_final:
            elementos = self.controlador.find_elements(*self.INSIGNIA_CARRITO)
            if elementos:
                return int(elementos[0].text)
            time.sleep(0.2)
        return 0

    def ir_al_carrito(self):
        self.hacer_clic(*self.ENLACE_CARRITO)
