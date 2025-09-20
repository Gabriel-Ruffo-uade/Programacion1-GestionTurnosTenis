from clientes import menu_clientes
from profesores import menu_profesores
from turnos import menu_turnos

def mostrar_menu_principal():
    opcion = ""
    while opcion != "0":
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestionar clientes")
        print("2. Gestionar profesores")
        print("3. Gestionar turnos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_profesores()
        elif opcion == "3":
            menu_turnos()
        elif opcion == "0":
            print("Saliendo de la aplicación...")
        else:
            print("Opción inválida, intente nuevamente.")