# Control de cadena de frio - lotes de reactivos
lote ={
    "codigo": "RD-471",
    "producto": "Reactivo Glucosa",
    "temperatura": 12.0,
    "cantidad": 25
}

print(lote["codigo"])
print(lote["temperatura"])
print(lote)

lotes = [
    {"codigo": "RD-471", "producto": "Glucosa", "temperatura": 12.0},
    {"codigo": "RD-472", "producto": "Colesterol", "temperatura": 4.5},
    {"codigo": "RD-473", "producto": "Urea", "temperatura": 6.8},
    {"codigo": "RD-474", "producto": "Hemoglobina", "temperatura": 9.2},
]

for lote in lotes:
    print(lote["codigo"], "-", lote["producto"], "-", lote["temperatura"])

def revisar_lote(lote, limite):
    if lote["temperatura"] > limite:
        return "BLOQUEADO"
    else:
        return "OK"

def revisar_bodega(lotes, limite):
    if len(lotes) == 0:
        print("No hay lotes registrados")
        return

    bloqueados = 0 
    for lote in lotes:
        estado = revisar_lote(lote, limite)
        print(lote["codigo"], "-", lote["producto"], "-", lote["temperatura"], "->", estado)
        if estado == "BLOQUEADO":
            bloqueados = bloqueados + 1

    print("---")
    print("Lotes revisados:", len(lotes))
    print("Bloqueados:", bloqueados)


revisar_bodega(lotes, 8)
