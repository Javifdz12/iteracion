def mcd_euclides(n1, n2):
    while n1 % n2 != 0:
        n1, n2 = n2, n1 % n2
    return n2

n1 = int(input('Introduce un número:'))
n2 = int(input('Introduce otro número:'))

print(f'El máximo común divisor entre {n1} y {n2} es {mcd_euclides(n1, n2)}')