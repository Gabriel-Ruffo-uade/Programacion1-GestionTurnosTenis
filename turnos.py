from storage import leer_json, escribir_json
from clientes import listar_clientes
from profesores import listar_profesores
from utils import solicitar_fecha_hora, solicitar_id
import os
import datetime

# Obtiene el directorio donde está el archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_TURNOS = os.path.join(BASE_DIR, "data", "turnos.json")
RUTA_CLIENTES = os.path.join(BASE_DIR, "data", "clientes.json")
RUTA_PROFESORES = os.path.join(BASE_DIR, "data", "profesores.json")

#menu----------------------------------------------------------------------------------------
#arma el menu para gestionar los turnos
def menu_turnos():
    opcion = ""
    while opcion != "0":
        print("\n--- MENÚ TURNOS ---")
        print("1. Listar turnos")
        print("2. Agregar turno")
        print("3. Cancelar turno")
        print("4. Ver matriz de turnos")
        print("0. Volver\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_turnos()
        elif opcion == "2":
            agregar_turno()
        elif opcion == "3":
            cancelar_turno()        
        elif opcion == "4":
            matriz_turnos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
#fin

#funciones principales----------------------------------------------------------------------------------------
#lista los turnos guardados
def listar_turnos():
    turnos = leer_json(RUTA_TURNOS, [])

    if not turnos:
        print("No hay turnos registrados.")
    else:
        for t in turnos:
            print(f"- {t['id']}: Cliente {t['cliente_id']} con Profesor {t['profesor_id']} en {t['fecha_hora']}")
#fin

#agrega un turno nuevo
def agregar_turno():
    turnos = leer_json(RUTA_TURNOS, [])

    listar_clientes()
    cliente_id = solicitar_id("Ingrese el ID del cliente: ",RUTA_CLIENTES)

    listar_profesores()
    profesor_id = solicitar_id("Ingrese el ID del profesor: ",RUTA_PROFESORES)
    fecha_hora = solicitar_fecha_hora("Ingrese fecha y hora (ej. 2025-09-21 15:00): ")

    nuevo = {
        "id": len(turnos) + 1,
        "cliente_id": cliente_id,
        "profesor_id": profesor_id,
        "fecha_hora": fecha_hora
    }

    turnos.append(nuevo)
    escribir_json(RUTA_TURNOS, turnos)
    print("Turno registrado correctamente.")
#fin

#cancela un turno existente
def cancelar_turno():
    turnos = leer_json(RUTA_TURNOS, [])
    listar_turnos()

    id_del = int(input("Ingrese el ID del turno a cancelar: "))
    turnos = [t for t in turnos if t["id"] != id_del]
    escribir_json(RUTA_TURNOS, turnos)

    print("Turno cancelado.")
#fin

#funcion para turnos----------------------------------------------------------------------------------------
#matriz de turnos
def matriz_turnos():
    """
    Muestra una matriz 7x3 que representa la disponibilidad de turnos de los profesores.
    Los días son filas y los turnos (mañana, tarde, noche) son columnas.
    """
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    turnos = ["Mañana", "Tarde", "Noche"]

    # Crear una matriz vacia (7 filas x 3 columnas)
    matriz = [["-" for _ in range(len(turnos))] for _ in range(len(dias))]

    # Leer los turnos guardados en el JSON
    registros_turnos = leer_json(RUTA_TURNOS, [])

    # Completar la matriz en base a los turnos existentes
    for t in registros_turnos:
        profesor_id = t["profesor_id"]
        cliente_id = t["cliente_id"]
        fecha_hora = t["fecha_hora"]

        # Determinar dia y turno segun la fecha (simplificado)
        try:
            fecha = datetime.datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
            dia_semana = fecha.weekday()  # 0 = Lunes, 6 = Domingo
            hora = fecha.hour

            if hora < 12:
                col = 0  # Mañana
            elif hora < 18:
                col = 1  # Tarde
            else:
                col = 2  # Noche

            # Mostrar ID del profesor y del cliente.
            matriz[dia_semana][col] = f"Prof {profesor_id} (Cli {cliente_id})"

        except Exception as e:
            print(f"Error procesando la matriz de turnos {t['id']}: {e}")

    # Mostrar matriz formateada
    print("\n=== MATRIZ DE TURNOS ===")
    print(f"{'Día':<12} {' | '.join(turnos)}")
    print("-" * 50)
    for i, dia in enumerate(dias):#se utiliza enumerate para recorrer el objeto dia dentro de dias con el for
        print(f"{dia:<12} {' | '.join(matriz[i])}")
    print()
#fin