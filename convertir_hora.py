#### Convertir hora ####
'''Hay que crear una función que reciba una hora en el formato 12 hrs y que convierta ese input en un formato
24 hrs '''

def hour_convert():
    hour_separated = hour.split(":")                             #Al ingresar la hora, lo toma como cadena de texto entonces la separamos
    if hour[-2:].lower() == 'pm':                                #Nos ubicaremos en el tipo de hora am/pm y si es pm debe cumplirse
        if hour_separated[0] != '12':                            #esta condición, la cual nos indica si la hora es distinta de 12
            hour_separated[0] = str(int(hour_separated[0])+12)   #tomamos el valor que hay en la posicion 0 de la lista con hora separada y le sumamos 12
    else:
        if hour_separated[0] == '12':                            #Si la hora es igual a 12, 
            hour_separated[0] = '00'                             #convertimos solamente a 00 la hora
    hour_conv = ':'.join(hour_separated)                         #volvemos a unir la hora separada por :
    print(hour_conv[:-2])                                        #devuelve la hora formato 24hrs pero sin el am/pm
    return
        

hour = input('Ingrese una hora en formato 12 hrs y en número, especifique AM o PM: ' + '\n')
hour_convert()

