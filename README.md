# Proyecto Final - Automatizacion de Pruebas

Este proyecto implementa un framework de automatizacion de pruebas con Python, Selenium y Pytest para un sitio web demo (Swag Labs). Ademas incluye pruebas de API con Requests y reportes HTML con capturas de pantalla al fallar.

## Objetivo

Desarrollar un framework de automatizacion completo que combine:

- pruebas de UI con Selenium WebDriver
- pruebas de API con Requests
- Page Object Model (POM)
- parametrizacion con archivos externos (JSON)
- logging de eventos importantes
- reportes HTML detallados
- captura de screenshots en fallas

## Tecnologias usadas

- Python 3.14
- Pytest
- Selenium WebDriver
- Requests
- Pytest HTML
- GitHub Actions

## Estructura del proyecto

```text
project-root/
├── .github/workflows/ci.yml
├── data/
│   └── users.json
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── cart_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   ├── test_carrito.py
│   ├── test_catalogo.py
│   └── test_login.py
├── utils/
│   ├── __init__.py
│   └── logger_config.py
├── README.md
├── pytest.ini
├── requirements.txt
└── repots/
    └── reporte.html
```

## Instalacion

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecucion de pruebas

```bash
pytest
```

Tambien puede ejecutarse un subconjunto especifico:

```bash
pytest tests/test_login.py
pytest tests/test_api.py
```

## Interpretacion de reportes

Los reportes HTML se generan en `repots/reporte.html`. Si alguna prueba falla, el framework guarda automaticamente una captura de pantalla en la carpeta `repots/screenshots` y la adjunta al reporte.

## Repositorio

El nombre sugerido para el repositorio es:

`proyecto-final-automation-testing-[nombre-apellido]`

## Notas

- Las pruebas son independientes entre si.
- Se utiliza un archivo JSON para los datos de prueba.
- Los flujos de UI siguen el patron Page Object Model.
- La configuracion de CI/CD se encuentra en `.github/workflows/ci.yml`.
