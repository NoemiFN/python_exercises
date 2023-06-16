##### Letras Repetidas ####

'''Sabemos que las cadenas de texto o strings son simplemente secuencias de caracteres y podemos tratarlo
como si fuera una lista, ¿a que se refiere esto? a que podemos obtener su longitud, iterar cada componente y 
acceder a cada caracter que compone la cadena de texto.


En este desafío, hay que crear una función que reciba una cadena de texto y devuelva el caracter que aparezca
más de una vez en el texto. Los espacios vacíos no cuentan y si la palabra no tiene letras repetidas, que devuelva None'''

def repeated_word():
    text_minus = texto.lower()
    text_without_spaces = text_minus.replace(" ", "")
    char_list = list(text_without_spaces)

    repeated = []
    for letra in range(len(char_list)):
        for letra_2 in range(len(char_list)):
            if letra != letra_2:
                if char_list[letra] == char_list[letra_2] and char_list[letra] not in repeated:
                    repeated.append(char_list[letra])
    if repeated == []:
        print('El texto no tiene elementos repetidos')
    else:
        print(repeated)

    return
                
texto = input('Ingrese su frase o palabra'+ '\n' )
repeated_word()