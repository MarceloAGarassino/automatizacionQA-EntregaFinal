from pathlib import Path

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.logger_config import obtener_registro

logger = obtener_registro(__name__)


@pytest.fixture(scope="function")
def navegador():
    opciones = Options()
    opciones.add_argument("--headless=new")
    opciones.add_argument("--window-size=1440,1200")
    opciones.add_argument("--disable-gpu")
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")
    opciones.add_argument("--log-level=3")

    controlador = webdriver.Chrome(options=opciones)
    controlador.implicitly_wait(5)
    logger.info("Chrome iniciado")
    try:
        yield controlador
    finally:
        controlador.quit()
        logger.info("Chrome cerrado")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()
    if reporte.when == "call" and reporte.failed:
        controlador = item.funcargs.get("navegador")
        if controlador is not None:
            carpeta = Path("repots/screenshots")
            carpeta.mkdir(parents=True, exist_ok=True)
            ruta_captura = carpeta / f"{item.name}.png"
            try:
                controlador.save_screenshot(str(ruta_captura))
            except Exception:
                ruta_captura = None

            if ruta_captura is not None:
                reporte.extra = getattr(reporte, "extra", [])
                reporte.extra.append(pytest_html.extras.png(str(ruta_captura)))
