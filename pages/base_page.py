from datetime import datetime
from pathlib import Path

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaginaBase:
    def __init__(self, controlador):
        self.controlador = controlador
        self.wait = WebDriverWait(controlador, 10)

    def abrir(self, url: str):
        self.controlador.get(url)

    def buscar(self, by, localizador: str, tiempo_espera: int = 10) -> WebElement:
        return WebDriverWait(self.controlador, tiempo_espera).until(
            EC.presence_of_element_located((by, localizador))
        )

    def buscar_todos(self, by, localizador: str, tiempo_espera: int = 10):
        return WebDriverWait(self.controlador, tiempo_espera).until(
            EC.presence_of_all_elements_located((by, localizador))
        )

    def hacer_clic(self, by, localizador: str, tiempo_espera: int = 10):
        elemento = self.buscar(by, localizador, tiempo_espera)
        try:
            self.controlador.execute_script(
                "arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();",
                elemento,
            )
        except Exception:
            elemento.click()

    def escribir_texto(self, by, localizador: str, valor: str, tiempo_espera: int = 10):
        elemento = self.buscar(by, localizador, tiempo_espera)
        elemento.clear()
        elemento.send_keys(valor)

    def es_visible(self, by, localizador: str, tiempo_espera: int = 10) -> bool:
        try:
            elemento = self.buscar(by, localizador, tiempo_espera)
            return elemento.is_displayed()
        except Exception:
            return False

    def tomar_captura(self, nombre: str) -> Path:
        carpeta = Path("repots/screenshots")
        carpeta.mkdir(parents=True, exist_ok=True)
        ruta_archivo = carpeta / f"{nombre}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        self.controlador.save_screenshot(str(ruta_archivo))
        return ruta_archivo
