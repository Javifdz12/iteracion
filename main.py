from clases.ejercicio7 import cambio_de_base,cambio_de_base_grande
from clases.ejercicio8 import cadena_separada
from clases.ejercicio9 import creardiccionario,orden,lista_nueva

if __name__ == '__main__':
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
                cambio_de_base(n,b)

        # Cuando es mayor a 36 utilizamos el método del enunciado
            else:
                cambio_de_base_grande(n, b)

if __name__ == '__main__':
    cadena = input('Introduce una frase')
    separador = input('¿Cual es nuestro separador?')
    print('nº\tCadena\n')
    for i in range(len(cadena_separada)):
        print(f'{i+1})\t{cadena_separada[i]}')

if __name__ == '__main__':
    diccionario = creardiccionario()
    print('\nAsí quedaría nuestro diccionario:\n')
    tabla = orden(diccionario)
    print(orden(diccionario))

    opcion = int(input('\n\nBien hecho, ahora que desea hacer:\n\t1) Localizar palabras que contengan lo que quiero. \n\t2) Añadir nueva palabra. \n\t3) Eliminar una de las palabras. \n\t4) Crear un nuevo diccionario. \n\t5) Mostrar diccionario\nIntroduce una opción:'))
    while  0 < opcion < 6:
        if opcion == 1:
            dato = input('\n¿Que deseas buscar en el diccinario?')
            diccionario_nuevo = lista_nueva(diccionario, dato)
            if diccionario_nuevo == []:
                print('No he podido encontrar nada')
            else:
                print('Esto es lo que he encontrado\n')
                print(orden(diccionario_nuevo))

        elif opcion == 2:
            palabra = input(f'\nIntroduce una nueva palabra\n {len(diccionario)} - ')

            while palabra in diccionario:
                palabra = input('Introduce una palabra que no exista todavía por favor:\n')

            diccionario.append(palabra)
            tabla = orden(diccionario)


        elif opcion == 3:
            print(tabla)
            posicion = int(input('Posición de la palabra que desea eliminar:'))
            diccionario.pop(posicion)
            tabla = orden(diccionario)

        elif opcion == 4:
            diccionario = creardiccionario()
            tabla = orden(diccionario)

        else:
            print('\nAsí quedaría nuestro diccionario:\n')
            print(tabla)

        opcion = int(input('\n\nBien hecho, ahora que desea hacer:\n\t1) Localizar palabras que contengan lo que quiero. \n\t2) Añadir nueva palabra. \n\t3) Eliminar una de las palabras. \n\t4) Crear un nuevo diccionario. \n\t5) Mostrar diccionario\nIntroduce una opción:'))