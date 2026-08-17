def buscar_mayor(lista):
    mayor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento 
    return mayor

def revisar_lote(temperatura, limite):
    if temperatura > limite:
        return "BLOQUEADO"
    else:
        return "OK"

def resumen_del_dia(temperaturas, limite):
    if len(temperaturas) == 0:
        print("No hay lotes registrados hoy")
        return

    bloqueados = 0
    for temperatura in temperaturas:
        if revisar_lote(temperatura, limite) == "BLOQUEADO":
            bloqueados = bloqueados + 1

    print("Lotes Revisados:", len(temperaturas))
    print("Bloqueados:", bloqueados)
    print("Peor Temperatura:", buscar_mayor(temperaturas))

resumen_del_dia([4.5, 12.0, 6.2, 9.8, 3.1, 7.9], 8)
