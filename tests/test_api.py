import requests


URL_BASE = "https://jsonplaceholder.typicode.com"


def test_obtener_publicacion_respuesta_valida():
    respuesta = requests.get(f"{URL_BASE}/posts/1", timeout=15)
    assert respuesta.status_code == 200
    datos = respuesta.json()
    assert datos["userId"] == 1
    assert "title" in datos
    assert "body" in datos


def test_crear_publicacion_retorna_201():
    carga = {
        "title": "Automation test title",
        "body": "This is a sample body to validate posting on JSONPlaceholder.",
        "userId": 1,
    }
    respuesta = requests.post(f"{URL_BASE}/posts", json=carga, timeout=15)
    assert respuesta.status_code == 201
    creada = respuesta.json()
    assert creada["title"] == carga["title"]
    assert creada["body"] == carga["body"]
    assert creada["userId"] == carga["userId"]


def test_eliminar_publicacion_retorna_exito():
    respuesta = requests.delete(f"{URL_BASE}/posts/1", timeout=15)
    assert respuesta.status_code == 200
    assert respuesta.text in ["{}", "[]"] or respuesta.json() == {}
