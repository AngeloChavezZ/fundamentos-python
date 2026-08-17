numeros = ["100", "99", "9"]

if len(numeros) == 0:
    print("La lista esta vacia - No hay maximo")
else:
    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero

    print(mayor)