#3. Crea un programa que devuelva una lista con todos los elementos únicos de otra lista.
def elementosUnicos(lista):
    lista_unicos = []
    for elemento in lista:
        if elemento not in lista_unicos:
            lista_unicos.append(elemento)
    return lista_unicos

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
lista_unica = elementosUnicos(lista)
print("Lista original: ", lista)
print("Lista con elementos únicos: ", lista_unica)