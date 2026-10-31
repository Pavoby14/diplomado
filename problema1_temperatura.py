# Problema 1: Control de temperatura de un edificio
# Los sensores y el consumo se simulan para practicar funciones.

def leer_temperatura(zona):
    # Simula la lectura de temperatura en cada zona.
    temperaturas = {"oficina": 27, "sala": 23, "bodega": 19}
    return temperaturas.get(zona, 22)


def calcular_temperatura_optima(hora, ocupada, exterior):
    # Si no hay personas, se usa una temperatura de ahorro.
    if not ocupada:
        return 26 if exterior >= 25 else 18
    if hora >= 8 and hora < 18:
        return 23 if exterior >= 25 else 22
    return 24 if exterior >= 25 else 21


def ajustar_clima(zona, actual, ideal):
    # Muestra qué orden enviaría al equipo de climatización.
    if actual > ideal:
        print(zona, ": encender refrigeración")
    elif actual < ideal:
        print(zona, ": encender calefacción")
    else:
        print(zona, ": temperatura correcta")


def analizar_consumo(consumos):
    # Registra el consumo simulado y calcula su promedio.
    total = sum(consumos)
    promedio = total / len(consumos) if consumos else 0
    return total, promedio


def main():
    hora = 10
    exterior = 29
    zonas = {"oficina": True, "sala": True, "bodega": False}
    consumos = []
    for zona, ocupada in zonas.items():
        actual = leer_temperatura(zona)
        ideal = calcular_temperatura_optima(hora, ocupada, exterior)
        print("Zona:", zona, "| Actual:", actual, "| Ideal:", ideal)
        ajustar_clima(zona, actual, ideal)
        # Consumo estimado en kWh, no lectura real.
        consumos.append(abs(actual - ideal) * 0.5)
    total, promedio = analizar_consumo(consumos)
    print("Consumo estimado total:", total, "kWh")
    print("Promedio por zona:", round(promedio, 2), "kWh")


if __name__ == "__main__":
    main()
