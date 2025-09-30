from storage import leer_json, escribir_json
import re

# Solicta y valida datos numericos ingresados por el usuario
# Se puede urtilizar para solicitar los campos documento, telefono, edad, cliente_id, etc.
# En la proxima entrega se puede cambiar el bucle While por recursividad
def solicitar_entero(mensaje, minimo=0, maximo=None):
    """
    Solicita un número entero al usuario con validación.
    
    Argumentos:
        mensaje (str): Mensaje a mostrar al usuario
        minimo (int, optional): Valor mínimo permitido
        maximo (int, optional): Valor máximo permitido
    
    Retorna:
        int: Número entero válido ingresado por el usuario
    """

    while True:
        try:
            valor = int(input(mensaje))
            
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}")
                continue
                
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}")
                continue
                
            return valor
            
        except ValueError:
            print("Error: Debe ingresar un número entero válido")


# Solicta y valida textos ingresados por el usuario
# Se puede urtilizar para solicitar los campos nombre, apellido, direccion, etc.
# En la proxima entrega se puede cambiar el bucle While por recursividad
def solicitar_texto(mensaje, longitud_minima=0):
    """
    Solicita texto al usuario con validación de caracteres alfabéticos y signos de puntuación.
    
    Argumentos:
        mensaje (str): Mensaje a mostrar al usuario
        longitud_minima (int, optional): Longitud mínima del texto
    
    Retorna:
        str: Texto válido ingresado por el usuario
    """
    while True:
        texto = input(mensaje).strip()
        
        if len(texto) < longitud_minima:
            print(f"El valor debe tener al menos {longitud_minima} caracteres")
            continue
        
        # Valida con una expresion regular que solo contenga caracteres alfabéticos, espacios y signos de puntuación
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s.,;:!?()-]+$', texto):
            print("El valor solo puede contener letras, espacios y signos de puntuación (.,;:!?()-)")
            continue
            
        return texto


# Solicta y valida fechas y horas ingresados por el usuario
# Se puede urtilizar para solicitar el campo fecha_hora de turnos.
# En la proxima entrega se puede cambiar el bucle While por recursividad
def solicitar_fecha_hora(mensaje):
    """
    Solicita fecha y hora al usuario con validación usando regex.
    
    Argumentos:
        mensaje (str): Mensaje a mostrar al usuario
    
    Retorna:
        str: Fecha y hora en formato válido
    """
    while True:
        fecha_hora = input(mensaje).strip()
        
        if not fecha_hora:
            print("La fecha y hora no pueden estar vacías")
            continue
        
        # Valida con una expresion regular que tenga el formato YYYY-MM-DD HH:MM
        patron = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$'
        if not re.match(patron, fecha_hora):
            print("Formato inválido. Use el formato: YYYY-MM-DD HH:MM (ej. 2025-09-21 15:00)")
            continue
            
        return fecha_hora


# Agrega un nuevo registro al archivo
# Se puede urtilizar para agregar un cliente, profesor, turno, etc.
def agregar_registro(ruta_archivo, nuevo_registro):
    """
    Agrega un nuevo registro al archivo.
    
    Argumentos:
        ruta_archivo (str): Ruta del archivo JSON
        nuevo_registro (dict): Diccionario con el nuevo registro (sin 'id')
    
    Retorna:
        bool: True si se agregó correctamente
    """
    entidades = leer_json(ruta_archivo, [])
    
    # Generar ID  
    nuevo_registro['id'] = generar_id(entidades)
    
    # Agregar el nuevo registro
    entidades.append(nuevo_registro)
    escribir_json(ruta_archivo, entidades)

    return True


# Elimina un registro existente en un archivo
# Se puede urtilizar para eliminar un cliente, profesor, turno, etc.
def eliminar_registro(ruta_archivo, id):
    """
    Elimina una entidad del archivo por ID.
    
    Argumentos:
        ruta_archivo (str): Ruta del archivo JSON
        id (int): ID del registro a eliminar
    
    Retorna:
        bool: True si se eliminó correctamente, False si no se encontró u ocurrió un error
    """
    entidades = leer_json(ruta_archivo, [])

    # Filtrar y eliminar el registro
    entidades_originales = len(entidades)
    entidades = [e for e in entidades if e.get("id") != id]
    
    if len(entidades) < entidades_originales:
        escribir_json(ruta_archivo, entidades)
        return True
    else:
        return False


# Genera un ID único para un nuevo registro de la lista.
def generar_id(lista_registros):
    """
    Genera un ID único para un nuevo registro de la lista.
    
    Argumentos:
        lista (list): Lista de registros
    
    Retorna:
        int: Nuevo ID
    """
    if not lista_registros:
        return 1
    
    # Encontrar el ID máximo y sumar 1
    ids_existentes = [registro.get('id', 0) for registro in lista_registros]
    return max(ids_existentes) + 1