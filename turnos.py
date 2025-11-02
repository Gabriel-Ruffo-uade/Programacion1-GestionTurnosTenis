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
        print("5. Estadisticas de turnos")
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
        elif opcion == "5":
            estadisticas_turnos()
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
    turnos = leer_json(RUTA_TURNOS)
    clientes = leer_json(RUTA_CLIENTES)
    profesores = leer_json(RUTA_PROFESORES)

    if not turnos:
        print("\nNo hay turnos registrados.\n")
        return []

    # Crear diccionarios para buscar nombre por ID
    clientes_dict = {str(c["id"]): c["nombre"] for c in clientes}
    profesores_dict = {str(p["id"]): p["nombre"] for p in profesores}

    # --- Crear la matriz ---
    matriz = []
    for turno in turnos:
        fecha_hora = turno.get("fecha_hora", "Sin fecha")
        cliente_nombre = clientes_dict.get(str(turno["cliente_id"]), "Desconocido")
        profesor_nombre = profesores_dict.get(str(turno["profesor_id"]), "Desconocido")
        fila = [fecha_hora, cliente_nombre, profesor_nombre]  # fila de la matriz
        matriz.append(fila)

    # --- Mostrar la matriz en formato tabla ---
    print("\n" + "-" * 50)
    print(f"{'TURNO':<20} {'CLIENTE':<15} {'PROFESOR':<15}")
    print("-" * 50)

    for fila in matriz:
        print(f"{fila[0]:<20} {fila[1]:<15} {fila[2]:<15}")

    print("-" * 50)
    return matriz
#fin

#funcion para listar estadistica----------------------------------------------------------------------------------------
#Lista de turnos tomados y libres por mes
def estadisticas_turnos():
    # Total de turnos configurables por mes (1 cancha * 3 turnos * 6 dias semanales *  4 semanas del mes)
    TURNOS_MAXIMOS_MES = 72 
    turnos = leer_json(RUTA_TURNOS, [])

    if not turnos:
        print("\nNo hay turnos registrados.\n")
        return

    #Extraer la parte YYYY-MM del campo fecha_hora
    meses = sorted({ t["fecha_hora"][:7] for t in turnos })

    print("\n=== ESTADÍSTICAS DE TURNOS POR MES ===\n")

    for mes in meses:
        tomados = recursion_turnos(turnos, mes)# uso recursivo
        libres = TURNOS_MAXIMOS_MES - tomados# calculo básico        
        print(f"Mes: {mes} → Tomados: {tomados} | Libres: {libres}")

#Funcion recursiva
def recursion_turnos(turnos, mes, i=0, contador=0):
    # Caso base: fin de lista
    if i == len(turnos):
        return contador
    
    # Si el turno pertenece al mes (busca coincidencia con la palabra que comience con el mes buscado)
    if turnos[i]["fecha_hora"].startswith(mes):
        contador += 1

    # Llamada recursiva
    return recursion_turnos(turnos, mes, i + 1, contador)  
#fin