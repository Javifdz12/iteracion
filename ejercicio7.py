#Ejerccio 7:
def cambio_de_base(numero, base):
    '''Cambio de base para bases no superiores a 36'''
    if numero > 0:
        digito = numero % base
        numero //= base

        # Utilizamos la recursividad para disminuir el número hasta 0.
        # En este momento habremos acabado de imprimir el número
        cambio_de_base(numero, base)

        if digito < 10:
            # end = '' se utiliza para que los digitos se impriman en una misma linea
            # por defecto haría un salto de línea
            print(f'{digito}', end = '')

        else:
            # No se puede poner un digito con dos cifras, por lo que necesitamos letras para su representación
            # En nuestro caso partimos de la base 10 y la letra 'A' (Que tiene un valor numérico de 65)
            # El 55 parte de el valor de la primera letra A menos nuestro digito más grande que es 10
            print(f'{chr(digito + 55)}', end = '')

def cambio_de_base_grande(numero, base):
        digito1 = numero // base
        digito2 = numero % base
        print(f'{digito1} . {digito2}')

b = 1

# Obligamos a que la base sea mayor que 2
while b < 2:
    n = int(input("Ingrese número en base 10: "))
    b = int(input("Ingrese base: "))
    if b < 2:
        print('Listillo la base tiene que ser 2 o mayor')
        continue

    else:

        # Partimos de 10 dígitos numéricos (contando el cero como uno de ellos) y 26 caracteres (sin incluir la ñ) en el abecedario castellano
        # Es por ello que la representación de la base la damos siempre con una cantidad máxima de 36 ( = 10 + 26)
        if b >= 2 and b <= 36:
            cambio_de_base(n, b)

        # Cuando es mayor a 36 utilizamos el método del enunciado
        else:
            cambio_de_base_grande(n, b)

