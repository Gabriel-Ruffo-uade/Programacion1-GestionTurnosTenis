import json
import os

def leer_json(ruta, default=None):
    if not os.path.exists(ruta):
        return default if default is not None else []
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def escribir_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)