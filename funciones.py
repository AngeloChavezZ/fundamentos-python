def buscar_mayor (lista):
    mayor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento 
    return mayor

resultado = buscar_mayor([12, 45, 3, 78])
print(resultado)

otro = buscar_mayor([5, 2, 9])
print(otro)

temperaturas = buscar_mayor([4.5, 12.0, 6.2, 9.8])
print(temperaturas)

def sumar_todo(lista):
    suma = 0
    for elemento in lista:
        print("elemento:", elemento , " | suma:", suma)
        suma = suma + elemento
    return suma

print(sumar_todo([12, 45, 3, 78, 20, 45]))

def contar_bloqueados(temperaturas, limite):
    bloqueados = 0
    for temperatura in temperaturas:
        if temperatura > limite:
            bloqueados = bloqueados +1
    return bloqueados

print( contar_bloqueados([4.5, 12.0, 6.2, 9.8, 3.1, 7.9], 8))
print( contar_bloqueados([4.5, 12.0, 6.2, 9.8, 3.1, 7.9], 5))
print( contar_bloqueados([4.5, 12.0, 6.2, 9.8, 3.1, 7.9], 15))


def revisar_lote(temperatura, limite):
    if temperatura > limite:
        return ("BLOQUEADO")
    else:
        return "OK"

print(revisar_lote(12.0, 8))
print(revisar_lote(4.5, 8))

def revisar_todos (temperaturas, limite):
    bloqueados = 0
    for temperatura in temperaturas:
        estado = revisar_lote(temperatura, limite)
        print(temperatura, "->", estado)
        if estado == "BLOQUEADO":
            bloqueados = bloqueados + 1
    return bloqueados

total = revisar_todos([4.5, 12.0, 6.2, 9.8, 3.1, 7.9], 8)
print("Total Bloqueados:", total)
