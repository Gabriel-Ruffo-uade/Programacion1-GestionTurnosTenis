from storage import leer_json, escribir_json
from clientes import listar_clientes
from profesores import listar_profesores
import os




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
        print("0. Volver\n")



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
    print("Ingrese el ID del cliente: ")
    cliente_id = obtener_id(RUTA_CLIENTES)

    listar_profesores()
    print("Ingrese el ID del profesor: ")
    profesor_id = obtener_id(RUTA_PROFESORES)

    fecha_hora = obtener_fecha()



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





#otras funciones-------------------------------------------------------------------------------------





def obtener_id(archivo):

    while True: #repetir hasta que se inputee lo correcto

        try:
            id = int(input())

        except:
            print('Solo numeros positivos, por favor') #si la id no es un numero int() da error

        else:
            if id > 0:

                #luego revisar si existe
                contenido = leer_json(archivo, [])
                for i in contenido:
                    if i['id'] == id:
                        return id
                print('Esta id no existe, ingresar id válida por favor')
            
#fin





def obtener_fecha():

    print("Ingrese fecha y hora (ej. 2025-09-21 15:00): ")

    while True: #repetir hasta que se inputee lo correcto

        fecha = input()

  
        

        #------------------

        if verifica:

            
            

                
            print("No es una fecha valída") #si es que falla el verificar y no sale de la funcion con el return, entonces envia este mesaje y loopea
            

        else:
            print("Formato incorrecto, tiene que ser aaaa-mm-dd hh:mm")     
#fin



