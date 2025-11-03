from storage import leer_json, escribir_json
from validaciones import es_texto_valido, es_fecha_hora_valida, es_telefono_valido, es_id_existente, es_horario_turno_valido

# Solicta y valida datos numericos ingresados por el usuario
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
    valido = False
    numero = 0

    while not valido:
        try:
            numero = int(input(mensaje))
            
            if minimo is not None and numero < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}")
                
            elif maximo is not None and numero > maximo:
                print(f"El valor debe ser menor o igual a {maximo}")
            else:
                valido = True
        except ValueError:
            print("Error: Debe ingresar un número entero válido")
    
    return numero

# Solicta y valida textos ingresados por el usuario
# Se puede urtilizar para solicitar los campos nombre, especialidad, etc.
def solicitar_texto(mensaje, longitud_minima=0):
    """
    Solicita texto al usuario con validación de caracteres alfabéticos y signos de puntuación.

    Argumentos:
        mensaje (str): Mensaje a mostrar al usuario
        longitud_minima (int, optional): Longitud mínima permitida
    
    Retorna:
        str: Texto válido ingresado por el usuario
    """
    valido = False
    texto = ""

    while not valido:
        texto = input(mensaje).strip()
        
        if len(texto) < longitud_minima:
            print(f"El valor debe tener al menos {longitud_minima} caracteres")

        elif not es_texto_valido(texto):
            print("El valor solo puede contener letras y espacios")
        else:
            valido = True
    
    return texto

# Solicta y valida telefonos ingresados por el usuario
def solicitar_telefono(mensaje):
    """
    Solicita un numero de telefono al usuario validando el formato argentino.

    Argumentos:
        mensaje (str): Mensaje a mostrar al usuario
    
    Retorna:
        str: Telefono válido ingresado por el usuario
    """
    valido = False
    telefono = ""
    
    while not valido:
        telefono = input(mensaje).strip()
        
        if not telefono.isdigit():
            print("El teléfono solo puede contener números")
        elif not  es_telefono_valido(telefono):
            print("Teléfono inválido. Debe tener 10 dígitos (ej. 1123456789)")
        else:
            valido = True
    
    return telefono

# Solicta y valida fechas y horas ingresados por el usuario
def solicitar_fecha_hora(mensaje, rango_horario=None):
    """
    Solicita fecha y hora al usuario validando el formato YYYY-MM-DD HH:MM.
    Opcionalmente valida que la hora esté dentro del rango del momento del día especificado.

    Argumentos:
        mensaje (str): Mensaje a mostrar al usuario
        rango_horario (str, optional): Puede ser "Mañana", "Tarde" o "Noche". Se validará que el horario ingresado coincida el rango solicitado.
    
    Retorna:
        str: Fecha y hora válida ingresada por el usuario

    """
    fecha_hora = ""

    valido = False
    while not valido:
        fecha_hora = input(mensaje).strip()

        if not fecha_hora:
            print("La fecha y hora no pueden estar vacías")

        elif not es_fecha_hora_valida(fecha_hora):
            print("Formato inválido. Use: YYYY-MM-DD HH:MM (ej. 2025-09-21 15:00)")

        elif rango_horario and not es_horario_turno_valido(fecha_hora, rango_horario):
            continue
        else:
            valido = True

    return fecha_hora

# Solicita y valida ids ingresados por el usuario
def solicitar_id(mensaje, ruta_archivo):
    """
    Solicita un id valido al usuario.

    Argumentos:
        mensaje (str): Mensaje a mostrar al usuario
        ruta_archivo (str): Ruta del archivo JSON
    
    Retorna:
        int: Id válido ingresado por el usuario
    """
    valido = False
    id = ""
    
    while not valido:
        id = input(mensaje).strip()
        
        if not es_id_existente(ruta_archivo, id):
            print("Id inválido")

        else:
            valido = True

    return id

# Busca un registro en un archivo JSON por ID
def buscar_registro_por_id(ruta_archivo, id):
    """
    Busca un registro en un archivo JSON por su ID.
    
    Argumentos:
        ruta_archivo (str): Ruta del archivo JSON
        id (int): ID del registro a buscar
    
    Retorna:
        dict: El registro encontrado, o None si no se encuentra
    """
    entidades = leer_json(ruta_archivo, [])
    
    for registro in entidades:
        if registro.get('id') == int(id):
            return registro
    
    return None

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
    eliminado = False

    entidades = leer_json(ruta_archivo, [])

    # Filtrar y eliminar el registro
    entidades_originales = len(entidades)
    entidades = [e for e in entidades if e['id'] != id]
    
    if len(entidades) < entidades_originales:
        escribir_json(ruta_archivo, entidades)
        eliminado = True
    
    return eliminado


# Genera un ID único para un nuevo registro de la lista.
def generar_id(lista_registros):
    """
    Genera un ID único para un nuevo registro de la lista.
    
    Argumentos:
        lista (list): Lista de registros
    
    Retorna:
        int: Nuevo ID
    """

    nuevo_id = 1

    if lista_registros:
        ids_existentes = []
        for r in lista_registros:
            if 'id' in r:
                ids_existentes.append(r['id'])

        if ids_existentes:
            nuevo_id = max(ids_existentes) + 1

    return nuevo_id