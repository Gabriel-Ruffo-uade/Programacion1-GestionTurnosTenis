from storage import leer_json, escribir_json
import os

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
        for c in clientes:
            print(f"- {c['id']}: {c['nombre']} ({c['telefono']})")

#agrega un cliente nuevo
def agregar_cliente():
    clientes = leer_json(RUTA_CLIENTES, [])
    nuevo = {
        "id": len(clientes) + 1,
        "nombre": input("Nombre del cliente: "),
        "telefono": input("Teléfono: ")
    }
    clientes.append(nuevo)
    escribir_json(RUTA_CLIENTES, clientes)
    print("Cliente agregado correctamente.")

#modifica un cliente existente
def modificar_cliente():
    clientes = leer_json(RUTA_CLIENTES, [])
    listar_clientes()
    id_mod = int(input("Ingrese el ID del cliente a modificar: "))
    for c in clientes:
        if c["id"] == id_mod:
            c["nombre"] = input(f"Nuevo nombre ({c['nombre']}): ") or c["nombre"]
            c["telefono"] = input(f"Nuevo teléfono ({c['telefono']}): ") or c["telefono"]
            escribir_json(RUTA_CLIENTES, clientes)
            print("Cliente modificado.")
            return
    print("Cliente no encontrado.")

#elimina un cliente
def eliminar_cliente():
    clientes = leer_json(RUTA_CLIENTES, [])
    listar_clientes()
    id_del = int(input("Ingrese el ID del cliente a eliminar: "))
    clientes = [c for c in clientes if c["id"] != id_del]
    escribir_json(RUTA_CLIENTES, clientes)
    print("Cliente eliminado.")