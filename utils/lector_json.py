import json
from pathlib import Path

def leer_json_productos(ruta_archivo):
    """
    Lee un archivo JSON que contiene una lista de productos y devuelve la lista de productos.

    :param ruta_archivo: Ruta al archivo JSON.
    :return: Lista de productos.
    """
    ruta = Path(ruta_archivo)
    with ruta.open('r', encoding='utf-8') as archivo:
        productos = json.load(archivo)
    
    nombres = [producto['nombre'] for producto in productos]
    return nombres

