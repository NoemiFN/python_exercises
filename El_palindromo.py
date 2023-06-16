##########El problema del palíndromo#################
'''Un palíndromo es una frase o palabra que de lee igual de izquierda
a derecha y viceversa.

En este desafío vamos a crear una función para identificar si una
cadena de texto es palíndromo o no.'''


def palindromo():
   text_minus = texto.lower()                   #convierte el texto a minusculas
   text_without_spaces = text_minus.replace(" ", "")   #reemplaza los espacios para facilitar la identificacion del palíndromo
   if text_without_spaces == text_without_spaces[::-1]:
      print('Tu frase o palabra es un palindromo')
   else:
      print('Tu frase o palabra NO es un palindromo')
   return

texto = input('Ingrese su frase o palabra'+'\n' )
palindromo()

while True:
   asking = input('\n'+'¿Quieres ingresar otra palabra o frase?' + '\n')
   if asking == 'Si':
     texto = input('\n'+'Ingrese su frase o palabra'+'\n')
     palindromo()
     continue
   else:
     print('\n'+ 'Gracias por participar')
   break
