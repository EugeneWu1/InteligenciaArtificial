#2. Crea un programa el cual imprima una lista con los primeros 15 números de la
#sucesión de Fibonacci.


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    secuencia = [0, 1]
    for i in range(2, n):
        sucesion = secuencia[-1] + secuencia[-2]
        secuencia.append(sucesion)

    return secuencia

n = 15
print(fibonacci(n))