# Problema 5: Riego automatizado (simulación educativa)
# No se controlan válvulas reales ni se consulta una API meteorológica.

def leer_humedad(seccion):
    # Devuelve porcentajes de humedad simulados.
    sensores = {"norte": 25, "sur": 55, "centro": 35}
    return sensores.get(seccion, 40)


def consultar_clima():
    # Simula una previsión de lluvia.
    return {"lluvia": False, "probabilidad": 20}


def calcular_riego(humedad, clima, necesidad):
    # Calcula litros estimados según la sequedad y las necesidades.
    if clima["lluvia"] or clima["probabilidad"] >= 70:
        return 0
    if humedad >= necesidad:
        return 0
    return (necesidad - humedad) * 2


def controlar_valvula(seccion, litros):
    # Informa qué haría la válvula, sin activar hardware.
    if litros > 0:
        print(seccion, ": abrir válvula para", litros, "litros estimados")
    else:
        print(seccion, ": mantener válvula cerrada")
    return litros > 0


def main():
    clima = consultar_clima()
    necesidades = {"norte": 45, "sur": 50, "centro": 40}
    for seccion, necesidad in necesidades.items():
        humedad = leer_humedad(seccion)
        litros = calcular_riego(humedad, clima, necesidad)
        print("Sección:", seccion, "| Humedad:", humedad, "%")
        controlar_valvula(seccion, litros)


if __name__ == "__main__":
    main()
