pedidos = [12, 45, 3, 78, 20, 45]

cuantos = 0
total = 0
mayor = pedidos[0]

for pedido in pedidos:
    cuantos = cuantos + 1
    total = total + pedido
    if pedido > mayor:
        mayor = pedido

print(cuantos)
print(total)
print(mayor)