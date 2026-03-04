# programa1.py
# Programa que incrementa un día a una fecha dada 
# Incremento simple de un día
print("Programa 1: Incrementar un día a una fecha")

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

# Incrementar un día (versión simple, sin validar meses)
dia += 1

print(f"La fecha incrementada en un día es: {dia}/{mes}/{año}")
