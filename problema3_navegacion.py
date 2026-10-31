# Problema 3: Navegación de vehículo autónomo (simulación educativa)
# No se conecta a vehículos reales ni sustituye software de conducción.


def leer_sensores():
    # Datos simulados de proximidad (metros) y cámara.
    return {"distancia": 4, "camara": "obstaculo", "trafico": "alto"}


def calcular_ruta_optima(rutas):
    # Escoge la ruta con menos minutos estimados.
    nombre = min(rutas, key=rutas.get)
    print("Ruta recomendada:", nombre, "Tiempo:", rutas[nombre], "minutos")
    return nombre


def detectar_obstaculo(datos):
    # Detecta una alerta por cercanía o por la cámara.
    return datos["distancia"] < 5 or datos["camara"] == "obstaculo"


def evitar_obstaculo(hay_obstaculo):
    # Solo muestra una acción simulada.
    if hay_obstaculo:
        print("Alerta: detener simulación y recalcular ruta")
    else:
        print("Camino despejado")


def ajustar_velocidad(trafico, obstaculo):
    # Velocidad sugerida únicamente para la simulación.
    if obstaculo:
        velocidad = 0
    elif trafico == "alto":
        velocidad = 20
    elif trafico == "medio":
        velocidad = 40
    else:
        velocidad = 60
    print("Velocidad simulada:", velocidad, "km/h")


def main():
    datos = leer_sensores()
    rutas = {"ruta A": 20, "ruta B": 16, "ruta C": 25}
    calcular_ruta_optima(rutas)
    obstaculo = detectar_obstaculo(datos)
    evitar_obstaculo(obstaculo)
    ajustar_velocidad(datos["trafico"], obstaculo)


if __name__ == "__main__":
    main()
