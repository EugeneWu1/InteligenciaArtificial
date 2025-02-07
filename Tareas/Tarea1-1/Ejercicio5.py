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

diccionarioSuma = {}

for i in range(len(data['Ciudad'])):
    ciudad = data['Ciudad'][i]
    ventas = data['Ventas'][i]
    if ciudad in diccionarioSuma:
        diccionarioSuma[ciudad] += ventas
    else:
        diccionarioSuma[ciudad] = ventas


print(diccionarioSuma)