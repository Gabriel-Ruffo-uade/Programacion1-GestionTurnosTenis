import json
import os

#funcion para leer el archivo donde se guarda la informacion (en este caso JSON)
def leer_json(ruta, default=None):
    if not os.path.exists(ruta):
        return default if default is not None else []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Si el archivo está vacío
        return default if default is not None else []

#funcion para escribir en un archivo (usamos JSON)
def escribir_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)