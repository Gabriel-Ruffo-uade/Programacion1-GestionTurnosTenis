from storage import leer_json, escribir_json
import os
from utils import solicitar_texto, solicitar_telefono, generar_id
from validaciones import es_telefono_valido
from validaciones import existe_registro_set

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
    
    #valida que no exista el telefono del cliente nuevo - para no duplicar los registros guardados.
    if existe_registro_set(RUTA_CLIENTES, "telefono", nuevo["telefono"]):
        print("Ya existe un cliente con ese teléfono. No se crea registro nuevo.")
        return

    clientes.append(nuevo)
    escribir_json(RUTA_CLIENTES, clientes)
    print("Cliente agregado correctamente.")

# modifica un cliente existente
def modificar_cliente():
    clientes = leer_json(RUTA_CLIENTES, [])
    if not clientes:
        print("No hay clientes registrados. Registre uno antes de poder modificar.")
        return

    listar_clientes()

    id_mod = None
    while id_mod is None:
        id_ingresado = input("Ingrese el ID del cliente a modificar: ").strip()

        if not id_ingresado.isdigit():
            print("ID inválido. Ingresar solo valores numéricos.")
            continue

        id_ingresado = int(id_ingresado)

        cliente_encontrado = None
        for cliente in clientes:
            if cliente["id"] == id_ingresado:
                cliente_encontrado = cliente
                break

        if not cliente_encontrado:
            print("Cliente no encontrado. Intente nuevamente.")
            continue

        id_mod = id_ingresado

    print("Dejar en blanco para no modificar.")

    nuevo_nombre = input(f"Nuevo nombre ({cliente_encontrado['nombre']}): ").strip()
    if nuevo_nombre:
        cliente_encontrado["nombre"] = nuevo_nombre

    telefono_valido = False

    while not telefono_valido:
        nuevo_telefono = input(f"Nuevo teléfono ({cliente_encontrado['telefono']}): ").strip()

        if nuevo_telefono == "":
            telefono_valido = True
            continue

        if not nuevo_telefono.isdigit() or not es_telefono_valido(nuevo_telefono):
            print("Teléfono inválido. Debe tener 10 dígitos numéricos. Intente nuevamente.")
        else:
            cliente_encontrado["telefono"] = nuevo_telefono
            telefono_valido = True

    escribir_json(RUTA_CLIENTES, clientes)
    print("Cliente modificado.")
        
def eliminar_cliente():
    clientes = leer_json(RUTA_CLIENTES, [])

    if not clientes:
        print("No hay clientes registrados. Registre uno antes de poder eliminar.")
        return
    
    listar_clientes()

    id_valido = None
    while id_valido is None:
        id_ingresado = input("Ingrese el ID del cliente a eliminar: ").strip()

        if not id_ingresado.isdigit():
            print("ID inválido. Ingrese solo valores numéricos.")
            continue

        id_ingresado = int(id_ingresado)

        cliente_encontrado = None
        for cliente in clientes:
            if cliente["id"] == id_ingresado:
                cliente_encontrado = cliente
                break

        if not cliente_encontrado:
            print("El ID ingresado no existe. Intente nuevamente.")
            continue

        id_valido = id_ingresado

    clientes = [c for c in clientes if c["id"] != id_valido]
    escribir_json(RUTA_CLIENTES, clientes)
    print("Cliente eliminado correctamente.")