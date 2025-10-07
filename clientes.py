from storage import leer_json, escribir_json
import os
from utils import solicitar_texto, solicitar_telefono, generar_id

# Obtiene el directorio donde está el archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_CLIENTES = os.path.join(BASE_DIR, "data", "clientes.json")

#funcion que arma el menu para gestionar la informacion de los clientes (estudiantes de tenis)
def menu_clientes():
    opcion = ""
    while opcion != "0":
        print("\n--- MENÚ CLIENTES ---")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("0. Volver\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_clientes()
        elif opcion == "2":
            agregar_cliente()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

#lee la lista de clientes que hay guardada
def listar_clientes():
    clientes = leer_json(RUTA_CLIENTES, [])
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for cliente in clientes:
            print(f"- {cliente['id']}: {cliente['nombre']} Tel: {cliente['telefono']}")

#agrega un cliente nuevo
def agregar_cliente():
    clientes = leer_json(RUTA_CLIENTES, [])
    
    nuevo = {
        "id": generar_id(clientes),
        "nombre": solicitar_texto("Nombre del cliente: ", 4),
        "telefono": solicitar_telefono("Teléfono: ")
    }
    
    clientes.append(nuevo)
    escribir_json(RUTA_CLIENTES, clientes)
    print("Cliente agregado correctamente.")

#modifica un cliente existente
def modificar_cliente():
    clientes = leer_json(RUTA_CLIENTES, [])
    listar_clientes()
    
    try:
        id_mod = int(input("Ingrese el ID del cliente a modificar: "))
        for cliente in clientes:
            if cliente["id"] == id_mod:
                print("Dejar en blanco para no modificar.")
                cliente["nombre"] = input(f"Nuevo nombre ({cliente['nombre']}): ") or cliente["nombre"]
                cliente["telefono"] = input(f"Nuevo teléfono ({cliente['telefono']}): ") or cliente["telefono"]
                escribir_json(RUTA_CLIENTES, clientes)
                print("Cliente modificado.")
                return
            else:
                print("Cliente no encontrado.")
    except ValueError:
        print("ID inválido. Ingresar solo valores numéricos.")
        
def eliminar_cliente():
    clientes = leer_json(RUTA_CLIENTES, [])
    listar_clientes()
    try:
        id_del = int(input("Ingrese el ID del cliente a eliminar: "))
        clientes_originales = len(clientes)
        clientes = [cliente for cliente in clientes if cliente["id"] != id_del]
        
        if len(clientes) < clientes_originales:
            escribir_json(RUTA_CLIENTES, clientes)
            print("Cliente eliminado.")
        else:
            print("Cliente no encontrado.")
    except ValueError:
        print("ID inválido. Ingresar solo valores numéricos.")