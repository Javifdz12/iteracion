cadena = input('Introduce una frase')

# Introducimos el caracter por el que queremos separar nuestra cadena
separador = input('¿Cual es nuestro separador?')

# Separamos la cadena en una lista
cadena_separada = cadena.split(separador)

# Imprimimos en forma de tabla
print('nº\tCadena\n')
for i in range(len(cadena_separada)):
    print(f'{i+1})\t{cadena_separada[i]}')