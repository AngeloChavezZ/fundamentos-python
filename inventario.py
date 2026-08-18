from datetime import date

hoy = date.today()
print("Hoy es:", hoy)

vence = date(2026, 9, 15)
print("Vence:", vence)

print("¿Ya venció?", vence < hoy)

dias = (vence - hoy).days
print("Dias restantes:", dias)

def revisar_caducidad(fecha_vencimiento, dias_alerta):
    hoy = date.today()
    dias = (fecha_vencimiento - hoy).days

    if dias < 0:
        return "VENCIDO"
    elif dias <= dias_alerta:
        return "POR VENCER"
    else:
        return "VIGENTE"

print(revisar_caducidad(date(2026, 7, 1), 30))
print(revisar_caducidad(date(2026, 9, 1), 30))
print(revisar_caducidad(date(2027, 3, 1), 30))

lotes = [
    {"codigo": "RD-471", "producto": "Glucosa",     "temperatura": 12.0, "vence": date(2026, 7, 1)},
    {"codigo": "RD-472", "producto": "Colesterol",  "temperatura": 4.5, "vence": date(2026, 9, 1)},
    {"codigo": "RD-473", "producto": "Urea",        "temperatura": 6.8, "vence": date(2027, 3, 1)},
    {"codigo": "RD-474", "producto": "Hemoglobina", "temperatura": 9.2, "vence": date(2026, 12, 1)},
]

for lote in lotes:
    estado_temp = "BLOQUEADO" if lote["temperatura"] > 8 else "OK"
    estado_venc = revisar_caducidad(lote["vence"], 30)
    print(lote["codigo"], "|", lote["producto"], "| temp:", estado_temp, "| caducidad:", estado_venc)

def accion_temperatura(temperatura, limite):
    if temperatura > limite:
        return "MOVER A CAMARA DE FRIO"
    else:
        return "EN RANGO"

def accion_caducidad(fecha_vencimiento, dias_alerta):
    estado = revisar_caducidad(fecha_vencimiento, dias_alerta)

    if estado == "VENCIDO":
        return "DAR DE BAJA"
    elif estado == "POR VENCER":
        return "DESPACHAR PRIMERO"
    else:
        return "SIN ACCION"


for lote in lotes:
    print(lote["codigo"], "|", lote["producto"])
    print("temperatura:", accion_temperatura(lote["temperatura"], 8))
    print("caducidad:", accion_caducidad(lote["vence"], 30))
    print()

def accion_del_lote(lote, limite, dias_alerta):
    estado = revisar_caducidad(lote["vence"], dias_alerta)

    if estado == "VENCIDO":
        return "DAR DE BAJA"

    if lote["temperatura"] > limite:
        return "MOVER A CAMARA DE FRIO"

    if estado == "POR VENCER":
        return "DESPACHAR PRIMERO"

    return "SIN ACCION"

for lote in lotes:
    print(lote["codigo"], "|", lote["producto"], "->", accion_del_lote(lote, 8, 30))