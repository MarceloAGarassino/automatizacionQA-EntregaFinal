import logging


def obtener_registro(nombre: str) -> logging.Logger:
    registro = logging.getLogger(nombre)
    if registro.handlers:
        return registro

    registro.setLevel(logging.INFO)
    manejador = logging.StreamHandler()
    manejador.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    )
    registro.addHandler(manejador)
    return registro
