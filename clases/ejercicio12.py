def cuadrados_perfectos(lim):
    cuadrados=[]
    for i in range(1,lim+1):
        n=1
        while n*n<=i:
            if n*n==i:
                cuadrados.append(i)
            n=n+1
    return cuadrados

cuadrados_perfectos(100)

import math
def raiz_cuadrada_entera(a):
    x = int(math.sqrt(a))
    return x

raiz_cuadrada_entera(1253)

def raiz_cuadrada_entera2(b):
    x = 0
    while x * x <= b:
        x = x + 0.1
    return int(x)

raiz_cuadrada_entera2(1250)