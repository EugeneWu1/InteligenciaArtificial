#Ejercicio 1: Listas y bucles
#Escribe un programa que:
#Cree una lista con los números del 1 al 10.
#Recorra la lista usando un bucle for e imprima cada número multiplicado por 2.

lista1 = [1,2,3,4,5,6,7,8,9,10]

for i in lista1:
    print(i * 2)


#Ejercicio 2: Suma de elementos de una lista
#Escribe un programa que:
#Cree una lista con 5 números enteros.
#Calcule la suma de todos los elementos de la lista usando un bucle for.
#Imprima el resultado.

lista2 = [1,2,3,4,5]

suma1 = 0

for j in lista2:
    suma1+= j

print(suma1)

#Ejercicio 3: Diccionarios y búsqueda
#Escribe un programa que:
#Cree un diccionario con los siguientes pares clave-valor:
#"manzana": 3
#"banana": 5
#"naranja": 2
#Pida al usuario que ingrese una fruta.
#Verifique si la fruta está en el diccionario y, si está, imprima la cantidad disponible. Si no está, imprima "Fruta no encontrada".

frutas ={
    'manzana' : 3,
    'banana' : 5,
    'naranja' : 2
}

fruit = input('Elija una de estas frutas: ')

if fruit in frutas:
    print(f'Fruta {fruit}, cantidad: {frutas[fruit]}')
else:
    print('No hay en existencia.')


#Ejercicio 4: Filtrar números pares
#Escribe un programa que:
#Cree una lista con 10 números enteros.
#Recorra la lista y cree una nueva lista que contenga solo los números pares.
#Imprima la nueva lista.
print()
nums = [1,2,3,4,5,6,7,8,9,10]

lista = [3, 8, 12, 7, 4, 10, 15, 6, 9, 2]
pares = [num for num in lista if num % 2 == 0]
print("Números pares:", pares)

#Ejercicio 5: Conteo de palabras
#Escribe un programa que:
#Pida al usuario que ingrese una frase.
#Cuente cuántas veces aparece cada palabra en la frase (puedes usar un diccionario para almacenar los resultados).
#Imprima el diccionario con las palabras y su conteo.

print('----------------------------------------')
oracion = input('Escriba una oracion: ').split()
conteo = {}
for palabra in oracion:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print(conteo)


#Ejercicio 6: Promedio de una lista
#Escribe un programa que:
#Cree una lista con 7 números decimales.
#Calcule el promedio de los números en la lista.
#Imprima el resultado.


#Ejercicio 7: Invertir una lista
#Escribe un programa que:
#Cree una lista con 6 elementos.
#Invierta el orden de los elementos de la lista sin usar la función reverse().
#Imprima la lista invertida.


#Ejercicio 8: Diccionario de estudiantes
#Escribe un programa que:
#Cree un diccionario donde las claves sean nombres de estudiantes y los valores sean sus calificaciones (un número entre 0 y 10).
#Recorra el diccionario e imprima el nombre de cada estudiante junto con "Aprobado" si su calificación es mayor o igual a 6, o "Reprobado" si es menor.


#Ejercicio 9: Eliminar duplicados
#Escribe un programa que:
#Cree una lista con elementos repetidos.
#Elimine los elementos duplicados de la lista.
#Imprima la lista sin duplicados.


#Ejercicio 10: Tabla de multiplicar
#Escribe un programa que:
#Pida al usuario que ingrese un número.
#Genere e imprima la tabla de multiplicar de ese número del 1 al 10.

