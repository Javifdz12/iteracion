import pandas as pd

n = int(input('¿Cuantas personas son?'))
df = []
for i in range(n):
    print(f'Persona {i}')
    nombre = input('\tNombre: ').lower
    apellido = input('\tApellido: ').lower
    huerfano = input('\t¿Es huerfano? ')
    edad = int(input('\tEdad: '))
    df.append([nombre, apellido, huerfano, edad])


columnas = ['Nombre','Apellido', 'Huerfano', 'Edad']
df = pd.DataFrame(df, columns = columnas)
df.loc[df['Huerfano'].isin(['s', 'si', 'S']), 'Huerfano'] = 'SI'
# Estamos atascados en este ejercicio