from storage import leer_json, escribir_json

RUTA_CLIENTES = "data/clientes.json"

def menu_clientes():
    while True:
        print("\n--- MENÚ CLIENTES ---")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("0. Volver")

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

def listar_clientes():
    clientes = leer_json(RUTA_CLIENTES, [])
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for c in clientes:
            print(f"- {c['id']}: {c['nombre']} ({c['telefono']})")

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

def eliminar_cliente():
    clientes = leer_json(RUTA_CLIENTES, [])
    listar_clientes()
    id_del = int(input("Ingrese el ID del cliente a eliminar: "))
    clientes = [c for c in clientes if c["id"] != id_del]
    escribir_json(RUTA_CLIENTES, clientes)
    print("Cliente eliminado.")