from storage import leer_json

def es_texto_valido(texto):
    """
    Valida que un texto contenga solo letras y espacios.

    Argumentos:
        texto (str): Texto a validar

    Retorna:
        bool: True si el texto es valido, False si no lo es
    """
    valido = True

    for char in texto:
        if not (char.isalpha() or char.isspace()):
            valido = False
            break

    return valido

def es_fecha_hora_valida(fecha_hora):
    """
    Valida si un string cumple con el formato YYYY-MM-DD HH:MM y que la fecha y hora sean existentes.
    
    Argumentos:
        fecha_hora (str): Fecha y hora a validar

    Retorna:
        bool: True si la fecha y hora son validas, False si no lo son
    """
    valido = False

    es_largo_valido = len(fecha_hora) == 16

    if es_largo_valido:
    
        # Validamos el formato - separadores y partes numericas donde corresponden
        son_separadores_validos = fecha_hora[4] == "-" and fecha_hora[7] == "-" and fecha_hora[10] == " " and fecha_hora[13] == ":"
        
        partes_numericas = [
            fecha_hora[0:4],   # año
            fecha_hora[5:7],   # mes
            fecha_hora[8:10],  # día
            fecha_hora[11:13], # hora
            fecha_hora[14:16]  # minuto
        ]

        son_partes_numericas_validas = all(p.isdigit() for p in partes_numericas)

        if son_separadores_validos and son_partes_numericas_validas:

            # Validamos que año, mes, dia, hora y minuto sean una fecha y hora reales
            anio = int(partes_numericas[0])
            mes = int(partes_numericas[1])
            dia = int(partes_numericas[2])
            hora = int(partes_numericas[3])
            minuto = int(partes_numericas[4])

            dias_por_mes = {
                1: 31,
                #si es febrero y es bisiesto entonces hay 29 dias
                2: 29 if(anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) else 28,
                3: 31, 4: 30, 
                5: 31, 6: 30, 
                7: 31, 8: 31,
                9: 30, 10: 31, 
                11: 30, 12: 31,
            }

            if(mes <= 12 and mes >= 1) and (dia <= 31 and dia >= 1) and (hora <= 23 and hora >= 0) and (minuto <= 59 and minuto >= 0) and (dia <= dias_por_mes[mes]):
                valido = True

    return valido

def es_telefono_valido(telefono):
    """
    Valida que un telefono contenga solo numeros y un maximo de 10 digitos (Formato argentino).

    Argumentos:
        telefono (str): Telefono a validar

    Retorna:
        bool: True si el telefono es valido, False si no lo es
    """
    valido = True

    if len(telefono) != 10:
        valido = False

    else:
        for char in telefono:
            if not char.isdigit():
                valido = False
                break

    return valido

def es_id_existente(ruta_archivo, id):
    """
    Valida que un id sea un numero entero positivo y exista en el archivo indicado.

    Argumentos:
        id (int): Id a validar
    
    Retorna:
        bool: True si el id es valido, False si no lo es
    """

    if not (id.isdigit() and int(id) > 0):
        return False
    
    contenido = leer_json(ruta_archivo, [])
    
    # Crea set de IDs para búsqueda instantánea
    ids_existentes = {i['id'] for i in contenido}
    
    return int(id) in ids_existentes

def validar_turno(turno):
    if turno.lower() in ["mañana", "tarde", "noche"]:
        return True
    return False

def es_id_valido(ruta_archivo, id):
    """
    Valida que un id sea un número entero positivo y exista en el archivo indicado.

    Argumentos:
        ruta_archivo (str): Ruta del archivo JSON donde buscar
        id (int): Id a validar
    
    Retorna:
        bool: True si el id es válido, False si no lo es
    """
    if not isinstance(id, int) or id <= 0:
        return False

    datos = leer_json(ruta_archivo, [])

    return any(item["id"] == id for item in datos)

def es_nombre_valido(nombre):
    """
    Valida que el nombre no esté vacío ni sea solo espacios.
    
    Argumentos:
        nombre (str): Nombre a validar
    
    Retorna:
        bool: True si el nombre es válido, False si no
    """
    return bool(nombre and nombre.strip())

def es_horario_turno_valido(fecha_hora, rango_horario):
    """
    Valida que el horario de una fecha y hora coincida con el horario del momento del día especificado.

    Argumentos:
        fecha_hora (str): Fecha y hora en formato YYYY-MM-DD HH:MM
        rango_horario (str): Rango a validar. Debe ser "Mañana", "Tarde" o "Noche".
    
    Retorna:
        bool: True si el horario está dentro del rango válido, False si no lo está.
    
    Nota:
        Si el rango_horario es inválido, también retorna False.
    """

    horarios ={
        "mañana": [8, 12],
        "tarde": [12, 18],
        "noche": [18, 22]
    }

    hora = int(fecha_hora[11:13])

    horario = rango_horario.lower()

    valido = True
    
    if validar_turno(horario):
        if hora < horarios[horario][0] or hora >= horarios[horario][1]:
            valido = False
            print(f"El horario no coincide con el rango horario solicitado: {rango_horario} (De {horarios[horario][0]} a {horarios[horario][1]}hs).")

    else:
        print("El rango horario ingresado no es válido. Valores permitidos: Mañana, Tarde, Noche")
        valido = False

    return valido



def hay_contenido(ruta):#devuelve true si hay contenido y false si no

    if not leer_json(ruta, False): return False #leer json ya chequea si esta vacio, devolviendo el contendio del segundo parametro si lo fuera, asi que usamos esa funcionalidad.
    else: return True


def existe_registro_set(ruta_archivo, campo, valor):
    """
    Valida si existe un registro duplicado - usando conjuntos (set).
    Argumentos:
        ruta_archivo (str): Ruta del archivo JSON
        campo (str): Campo a evaluar (ej: 'telefono', 'nombre', 'fecha_hora')
        valor (str/int): Valor a validar
    Retorna:
        bool: True si ya existe, False si no existe
    """
    registros = leer_json(ruta_archivo, [])
    valores_existentes = { str(r.get(campo)).lower() for r in registros if campo in r }

    return str(valor).lower() in valores_existentes


def existe_turno_duplicado_set(ruta_archivo, profesor_id, fecha_hora):
    '''
    Docstring for existe_turno_duplicado_set
    
    :param ruta_archivo: Ruta donde se encuentra el archivo para buscar el id del profesor
    :param profesor_id: Identificador unico del profesor
    :param fecha_hora: Fecha a ser validada, si se encuentra o no
    '''
    turnos = leer_json(ruta_archivo, [])
    combinaciones = { (t["profesor_id"], t["fecha_hora"]) for t in turnos }
    return (profesor_id, fecha_hora) in combinaciones