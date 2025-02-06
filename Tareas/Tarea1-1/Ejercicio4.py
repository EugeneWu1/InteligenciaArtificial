#4. Crea un programa que almacene información sobre productos y sus precios en un
#diccionario, esta información debe ser ingresada desde teclado.

productos = {}

while True:
    producto = input('Ingrese el nombre del producto:')
    precio = float(input('Ingrese el precio del producto: '))

    productos[producto] = precio
    continuar = input('Desear continuar? Si/No \n')

    if continuar.lower() == 'no':
        break

print(f'Productos registrados: {productos}')