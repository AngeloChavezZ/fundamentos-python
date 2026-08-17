temperaturas = [4.5, 12.0, 6.2, 9.8, 3.1, 7.9]

bloqueados = 0
peor = temperaturas[0]  

for temperatura in temperaturas:
    if temperatura > 8:
        print("Bloquear - lote a", temperatura, "grados")
        bloqueados = bloqueados + 1
    else:
        print("OK - lote a", temperatura, "grados")

    if temperatura > peor:
        peor = temperatura

print("Fin de la revision")
print("Total de lotes bloqueados:", bloqueados)
print("Temperatura mas alta registrada:", peor)
