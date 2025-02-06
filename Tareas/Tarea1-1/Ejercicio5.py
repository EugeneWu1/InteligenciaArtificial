#5. Dado el siguiente diccionario:
#data = {
# 'Ciudad': ['Nueva York', 'Los Ángeles', 'Nueva York', 'Chicago'],
# 'Ventas': [100, 150, 200, 50]
#}
#Agrupe los datos por ciudad y mostrar la suma por ciudades


data = {
    'Ciudad' : ['Nueva York', 'Los Ángeles', 'Nueva York', 'Chicago'],
    'Ventas' : [100, 150, 200, 50]
}


print(f'Ciudades: {data['Ciudad']}, Suma por ciudades: {sum(data['Ventas'])}')