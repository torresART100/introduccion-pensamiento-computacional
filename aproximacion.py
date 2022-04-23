objetivo = int(input('Escoge un numero: '))

epsilon = 0.01
paso = epsilon**2
respuesta = 0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:   #abs tell us about absolutes numbers. 1.9 al cuadrado es igual 3.61 -4 (4 -3.61) igual a 0.39 este numero es mayor al valor que asignamos a epsilo de  0.01 y la respuesta es decir el número 1.9 en este ejemplo es menor a 4 nuestro numero objetivo al que le estamos sacando la raiz.
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')