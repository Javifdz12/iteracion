# iteracion
ejercicio 6:

Se quiere conservar el historial de los movimientos mensuales en una cuenta corriente.

1. Modificar el tipo CUENTA definido en el capítulo «Estructuras elementales» para conservar el rastro de los movimientos en una cuenta durante un mes.

2. Establecer el saldo a final de mes de una cuenta dada.

El saldo ya no es un atributo de la cuenta. Se obtiene recorriendo el historial mensual y anual que registra el importe del saldo de la cuenta para cada mes.

3. Rehacer las definiciones anteriores.

Una tabla clientes contiene las cuentas corrientes de un conjunto de clientes.

4. Determinar los clientes para los que la media de los importes de los movimientos es superior a una suma dada.

El ejercicio siguiente se resolverá por completo en el capítulo «Edición de un número».

Ejercicio 7: Edición de un número entero





1. Escribir un algoritmo iterativo que transforme un número entero n cualquiera en su representación en una base B ≥ 2 cualquiera.

Cuando la base es superior a 36, se puede utilizar la representación de los números en base diez, pero separando cada cifra de la representación del número en base B mediante un separador convenido, por ejemplo, un punto. Eso es lo que se usa para expresar, por ejemplo, la dirección IP de un host en una red con IPv4. Así, por ejemplo, la representación en base 256 de 3000, expresada aquí en base diez, se escribirá: 11 184256 = 3000diez.

Este ejercicio está completamente resuelto en el capítulo «Edición de un número».

Ejercicio 8: Análisis de una cadena de caracteres





Sea una cadena de caracteres con distintas partes separadas por un carácter SEPARADOR específico. El ejemplo que aparece aquí debajo representa una cadena de este tipo, donde el carácter separador es dos puntos ’:’.

Este es un:ejemplo : de cadena a analizar:
Se quieren separar las distintas partes y situarlas en una tabla de cadenas de caracteres. Para el ejemplo que aparece antes, se quiere obtener la tabla siguiente:

n.°

Cadena

1

’Este es un’

2

’ejemplo ’

3

’ de cadena para analizar’











1. Escribir el módulo de software que realiza esta descomposición.

2. Utilizar este módulo en un algoritmo de búsqueda de los campos GCOS del archivo /etc/passwd de un sistema UNIX.

Se trata de construir una tabla que da todos los campos obtenidos asociados al identificador de un usuario. El algoritmo emite una alerta cuando el campo GCOS no se ha completado con la descripción del usuario.

Puede encontrar este ejercicio resuelto y la solución analizada en los elementos disponibles para descargar desde la página Información.

Ejercicio 9: Búsqueda de palabras en un diccionario





Sea una tabla de PALABRAS en español. Las palabras se guardan en una tabla llamada diccionario. Se utilizan otras dos tablas para recorrer el diccionario. Para cada palabra, una tabla llamada siguiente da el número de la celda ocupada por la palabra que le sigue en orden alfabético en el diccionario. La tabla anterior también da, para cada palabra, el número de la celda del diccionario que contiene la palabra anterior en orden alfabético. A la primera palabra de la lista ordenada le corresponde un número de celda del anterior igual a índice_min(diccionario) - 1. Igualmente, a la última palabra de la lista ordenada le corresponde un número de celda de la siguiente igual al mismo valor. La tabla que aparece debajo muestra un ejemplo de estas tres tablas.

i

diccionario

anterior

siguiente

1

avión

3

4

2

tren

4

...

3

auto

0

1

4

camión

1

2

5

...

...

...















Se ve que para ‘camión’, en la celda 4, la palabra siguiente en orden alfabético ocupa la celda 2 y la anterior ocupa la celda 1. Entonces, el orden alfabético de estas tres palabras es ‘avión’, ‘camión’ y ‘tren’.

1. Escribir el algoritmo que da la lista de las palabras guardadas empezando por una letra dada.

Así, por ejemplo, el algoritmo aplicado a la lista anterior dará (‘avión’, ‘auto’) para la letra ’a’.

También es posible definir un tipo nuevo de datos, PALABRA, formado con una cadena de caracteres para la palabra propiamente dicha y con dos números enteros para descubrir la palabra anterior y la siguiente en el diccionario. En este caso, el diccionario se convierte en una simple tabla de PALABRAS.

2. Definir el tipo PALABRA y rehacer el algoritmo anterior para utilizarlo.

3. Escribir el algoritmo que permite añadir una palabra nueva al diccionario.

4. Escribir el algoritmo de eliminación de una palabra.

Puede encontrar este ejercicio resuelto y la solución analizada en los elementos disponibles para descargar desde la página Información.

Ejercicio 10: Representar los miembros de una familia





Se ha formado una tabla familias con 1000 componentes numerados desde 1. Cada componente contiene un dato de tipo PERSONA según el siguiente diagrama:

images/06DP08.png
La asociación reflexiva en la entidad PERSONA, designada en el diagrama por «es el hijo de», significa que una instancia de PERSONA es hija (hijo) de ninguna, de una o de dos instancias de PERSONA.

1. Definir el tipo PERSONA. ¿Cómo declarar la tabla familias?

Cuando una persona registrada en la tabla no tiene padre o madre registrado, el atributo correspondiente es HUÉRFANO. Cuando una celda no está ocupada porque la persona que contenía se ha borrado, su identificador es BORRADO. Las celdas que nunca han recibido valor, cuando hay menos de 1000 personas registradas, tienen un identificador igual a VACÍO.

2. Dar la lista de todas las personas registradas con una edad de 20 a 30 años.

3. Envejecer 1 año a todas las personas registradas.

4. Establecer la lista de todos los huérfanos de menos de 15 años.

5. Hacer un algoritmo que determina la identidad del padre de ’Jaime MARTÍN’.

6. Hacer un algoritmo que establezca la lista de los hermanos y hermanas de ’Jaime MARTÍN’.

Puede encontrar la solución de este ejercicio en los complementos disponibles para descargar desde la página Información.

Ejercicio 11: mcd de dos números enteros





El algoritmo que permite determinar el máximo común divisor de dos números enteros también se estudia en el capítulo «Recursividad», durante el estudio del tipoFRACCIÓN.

1. Dar una versión iterativa del algoritmo de Euclides para el cálculo del mcd de dos números enteros.

2. Estudiar una versión iterativa que calcula el mcd haciendo solo sumas o restas.

Puede encontrar una solución completa de este ejercicio en los complementos disponibles para descargar desde la página Información.

Ejercicio 12: Cuadrados perfectos y raíz cuadrada entera





Un número entero natural es un cuadrado perfecto si es el cuadrado de un número entero. Así, 0 = 02, 1 = 12, 4 = 22, 16 = 42 son cuadrados perfectos.

1. Hacer un algoritmo que establezca la lista de los cuadrados perfectos inferiores a un límite dado. El algoritmo no debe hacer multiplicaciones.

La raíz cuadrada entera de un número entero n ≥ 0 es el único número enteror ≥ 0 definido por:

r2 ≤ n < (r + 1)2
2. Escribir el algoritmo de cálculo de la raíz cuadrada entera de un número entero.