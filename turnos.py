from storage import leer_json, escribir_json
from clientes import listar_clientes
from profesores import listar_profesores

RUTA_TURNOS = "data/turnos.json"

def menu_turnos():
    while True:
        print("\n--- MENÚ TURNOS ---")
        print("1. Listar turnos")
        print("2. Agregar turno")
        print("3. Cancelar turno")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_turnos()
        elif opcion == "2":
            agregar_turno()
        elif opcion == "3":
            cancelar_turno()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def listar_turnos():
    turnos = leer_json(RUTA_TURNOS, [])
    if not turnos:
        print("No hay turnos registrados.")
    else:
        for t in turnos:
            print(f"- {t['id']}: Cliente {t['cliente_id']} con Profesor {t['profesor_id']} en {t['fecha_hora']}")

def agregar_turno():
    turnos = leer_json(RUTA_TURNOS, [])
    listar_clientes()
    cliente_id = int(input("Ingrese el ID del cliente: "))
    listar_profesores()
    profesor_id = int(input("Ingrese el ID del profesor: "))
    fecha_hora = input("Ingrese fecha y hora (ej. 2025-09-21 15:00): ")

    nuevo = {
        "id": len(turnos) + 1,
        "cliente_id": cliente_id,
        "profesor_id": profesor_id,
        "fecha_hora": fecha_hora
    }
    turnos.append(nuevo)
    escribir_json(RUTA_TURNOS, turnos)
    print("Turno registrado correctamente.")

def cancelar_turno():
    turnos = leer_json(RUTA_TURNOS, [])
    listar_turnos()
    id_del = int(input("Ingrese el ID del turno a cancelar: "))
    turnos = [t for t in turnos if t["id"] != id_del]
    escribir_json(RUTA_TURNOS, turnos)
    print("Turno cancelado.")
