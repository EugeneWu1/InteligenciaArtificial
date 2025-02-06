#1. Crea un programa que sume todos los números de una lista (sin usar el método
#nativo de Python “sum”).

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

suma = 0

for i in lista_numeros:
    suma += i

print(suma)