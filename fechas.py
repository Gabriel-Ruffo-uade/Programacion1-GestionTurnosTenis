import re



#--------------------------------------------------------------------------------------------------------------



def verificar_fecha(fecha): #toma un diccionario de la forma {'año':int, 'mes':int, 'dia':int, 'hora':int, 'minutos':int} y verifica que sea una fecha real.

    fecha_valida = False
    
    
    if fecha['mes'] == 2 and fecha['año'] % 4 == 0 and fecha['año'] % 100 != 0 and fecha['dia'] <= 29: fecha_valida = True #si es febrero y año bisiesto entonces el dia tiene que ser menor a 29
        
    elif fecha['mes'] == 2 and fecha['dia'] <=28: fecha_valida = True #si es febrero y no es bisiesto entonces solo hay 28 dias en el mes

    elif (fecha['mes'] == 1 or fecha['mes'] == 3 or fecha['mes'] == 5 or fecha['mes'] == 7 or fecha['mes'] == 8 or fecha['mes'] == 10 or fecha['mes'] == 12) and fecha['dia'] <=31: fecha_valida = True  #para los fecha['mes']es con 31 dias

    elif fecha['mes'] <= 12 and fecha['dia'] <= 30: fecha_valida = True #para los meses con 30 dias


    #-------

    if fecha['hora'] <= 23 and fecha['minutos'] <= 59 and fecha_valida == True: #ahora revisar que la hora sea posible
        return True
    
    else:
        return False
#fin



def convertir_desde_string(string): #convierte un string de la forma 'aaaa-mm-dd hh:mm' a un diccionario de la forma {'año':int, 'mes':int, 'dia':int, 'hora':int, 'minutos':int}. soporta meses, dias y horas de un digito.
    if re.search(r"\d\d\d\d-\d{1,2}-\d{1,2}\s\d{1,2}:\d\d\Z",string): #comprobar que tenga el formato correcto (soporta dias,meses y horas con un solo digito)

            año = int(string[:4]) #extraer el año
            string = string[5:]
            print (string)#d



            if re.search(r"\d-\d{1,2}\s\d{1,2}:\d\d\Z",string): #si solo tiene un digito el mes
                mes = int(string[:1])
                string = string[2:]
                print (string,'ms')#d
            
            else: #si tiene dos digitos el mes
                mes = int(string[:2])
                string = string[3:]
                print (string,'md')#d
                
            print({'año':año, 'mes':mes})#d

            if re.search(r"\d\s\d{1,2}:\d\d\Z",string): #si solo tiene un digito el dia
                dia = int(string[:1])
                string = string[2:]
                print (string)#d
            
            else: #si tiene dos digitos el dia
                dia = int(string[:2])
                string = string[3:]
                print (string)#d



            if re.search(r"\d:\d\d\Z",string): #si solo tiene un digito la hora
                hora = int(string[:2])
                string = string[3:]
                print (string)#d
            
            else: #si tiene dos digitos la hora
                hora = int(string[:3])
                string = string[4:]
                print (string)#d

            

            minutos = int(string) #extraer los minutos
            print({'año':año, 'mes':mes, 'dia':dia, 'hora':hora, 'minutos':minutos})#d
            return {'año':año, 'mes':mes, 'dia':dia, 'hora':hora, 'minutos':minutos}
#fin

convertir_desde_string(input())