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

def es_id_valido(ruta_archivo, id):
    """
    Valida que un id sea un numero entero positivo y exista en el archivo indicado.

    Argumentos:
        id (int): Id a validar
    
    Retorna:
        bool: True si el id es valido, False si no lo es
    """
    valido = False

    if id.isdigit() and int(id) > 0:
        contenido = leer_json(ruta_archivo, [])
        for i in contenido:
            if i['id'] == id:
                valido = True
                break

    return valido