from storage import leer_json, escribir_json
from validaciones import validar_turno, es_id_valido, es_nombre_valido
from validaciones import existe_registro_set
import os

# Obtiene el directorio donde está el archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_PROFESORES = os.path.join(BASE_DIR, "data", "profesores.json")

#funcion para mostrar las opciones de gestion para los datos de prfesor de tenis
def menu_profesores():
    opcion = ""
    while opcion != "0":
        print("\n--- MENÚ PROFESORES ---")
        print("1. Listar profesores")
        print("2. Agregar profesor")
        print("3. Modificar profesor")
        print("4. Eliminar profesor")
        print("0. Volver\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_profesores()
        elif opcion == "2":
            agregar_profesor()
        elif opcion == "3":
            modificar_profesor()
        elif opcion == "4":
            eliminar_profesor()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

#lee la informacion del archivo para acceder a los datos del profesor de tenis
def listar_profesores():
    profesores = leer_json(RUTA_PROFESORES, [])
    if not profesores:
        print("No hay profesores registrados.")
    else:
        for p in profesores:
            print(f"- {p['id']}: {p['nombre']} (Turno: {p['turno']})")

#escribe los datos de un profesor nuevo
def agregar_profesor():
    profesores = leer_json(RUTA_PROFESORES, [])

    nombre = input("Nombre del profesor: ").strip()
    while not es_nombre_valido(nombre):
        print("El nombre no puede estar vacío. Intente nuevamente.")
        nombre = input("Nombre del profesor: ").strip()

    turno = input("Turno (Mañana/Tarde/Noche): ")
    while not validar_turno(turno):
        print("Turno inválido. Por favor, seleccione entre (Mañana/Tarde/Noche).")
        turno = input("Turno (Mañana/Tarde/Noche): ")
    turno = turno.capitalize()

    nuevo = {
        "id": len(profesores) + 1,
        "nombre": nombre,
        "turno": turno
    }

    #valida que no exista el nombre del profesor en el Json
    if existe_registro_set(RUTA_PROFESORES, "nombre", nombre):
        print("Ya existe un profesor con ese nombre. No se guardan los datos ingresados.")
        return

    profesores.append(nuevo)
    escribir_json(RUTA_PROFESORES, profesores)
    print("Profesor agregado correctamente.")

#modifica los datos de un profesor existente
def modificar_profesor():
    profesores = leer_json(RUTA_PROFESORES, [])

    if not profesores:
        print("No hay profesores registrados. Registre uno antes de poder modificar.")
        return

    listar_profesores()

    id_mod = None
    while id_mod is None or not es_id_valido(RUTA_PROFESORES, id_mod):
        entrada = input("Ingrese el ID del profesor a modificar: ")
        try:
            id_mod = int(entrada)
            if not es_id_valido(RUTA_PROFESORES, id_mod):
                print("ID no válido. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número entero.")

    for p in profesores:
        if p["id"] == id_mod:
            p["nombre"] = input(f"Nuevo nombre ({p['nombre']}): ") or p["nombre"]

            turno_ingresado = input(f"Nuevo turno ({p['turno']}): ")
            if turno_ingresado:
                while not validar_turno(turno_ingresado):
                    print("Turno inválido. Por favor, seleccione entre (Mañana/Tarde/Noche).")
                    turno_ingresado = input("Nuevo turno (Mañana/Tarde/Noche): ")
                p["turno"] = turno_ingresado.capitalize()

            escribir_json(RUTA_PROFESORES, profesores)
            print("Profesor modificado.")
            return


#elimina los datos de un profesor
def eliminar_profesor():
    profesores = leer_json(RUTA_PROFESORES, [])

    if not profesores:
        print("No hay profesores registrados. Registre uno antes de poder eliminar.")
        return

    listar_profesores()

    id_del = None

    while id_del is None or not es_id_valido(RUTA_PROFESORES, id_del):
        entrada = input("Ingrese el ID del profesor a eliminar: ")
        try:
            id_del = int(entrada)
            if not es_id_valido(RUTA_PROFESORES, id_del):
                print("ID no válido o no encontrado. Intente nuevamente.")
        except ValueError:
            print("Error: Por favor ingrese un número entero.")

    profesores = [p for p in profesores if p["id"] != id_del]
    escribir_json(RUTA_PROFESORES, profesores)
    print("Profesor eliminado correctamente.")
