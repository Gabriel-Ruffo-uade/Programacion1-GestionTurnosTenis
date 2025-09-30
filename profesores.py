from storage import leer_json, escribir_json
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
            print(f"- {p['id']}: {p['nombre']} (Especialidad: {p['especialidad']})")

#escribe los datos de un profesor nuevo
def agregar_profesor():
    profesores = leer_json(RUTA_PROFESORES, [])
    nuevo = {
        "id": len(profesores) + 1,
        "nombre": input("Nombre del profesor: "),
        "especialidad": input("Especialidad: ")
    }
    profesores.append(nuevo)
    escribir_json(RUTA_PROFESORES, profesores)
    print("Profesor agregado correctamente.")

#modifica los datos de un profesor existente
def modificar_profesor():
    profesores = leer_json(RUTA_PROFESORES, [])
    listar_profesores()
    id_mod = int(input("Ingrese el ID del profesor a modificar: "))
    for p in profesores:
        if p["id"] == id_mod:
            p["nombre"] = input(f"Nuevo nombre ({p['nombre']}): ") or p["nombre"]
            p["especialidad"] = input(f"Nueva especialidad ({p['especialidad']}): ") or p["especialidad"]
            escribir_json(RUTA_PROFESORES, profesores)
            print("Profesor modificado.")
            return
    print("Profesor no encontrado.")

#elimina los datos de un profesor
def eliminar_profesor():
    profesores = leer_json(RUTA_PROFESORES, [])
    listar_profesores()
    id_del = int(input("Ingrese el ID del profesor a eliminar: "))
    profesores = [p for p in profesores if p["id"] != id_del]
    escribir_json(RUTA_PROFESORES, profesores)
    print("Profesor eliminado.")
