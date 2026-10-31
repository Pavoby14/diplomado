# Problema 4: Optimización básica de la producción

def monitorear_maquina(nombre, horas_uso, funcionando):
    # Revisa si la máquina está disponible y sus horas de uso.
    print("Máquina:", nombre, "| Horas:", horas_uso)
    return funcionando


def planificar_mantenimiento(nombre, horas_uso, limite):
    # Recomienda mantenimiento cuando supera el límite indicado.
    if horas_uso >= limite:
        print("Programar mantenimiento para", nombre)
    else:
        print(nombre, "todavía no necesita mantenimiento")


def analizar_rendimiento(producidas, meta):
    # Compara unidades fabricadas con la meta.
    if meta <= 0:
        return 0
    return producidas / meta * 100


def ajustar_produccion(demanda, capacidad):
    # Evita planificar más unidades que la capacidad disponible.
    programadas = min(demanda, capacidad)
    print("Unidades programadas:", programadas)
    if demanda > capacidad:
        print("Demanda pendiente:", demanda - capacidad)


def main():
    maquinas = [("M1", 110, True), ("M2", 75, False)]
    for nombre, horas, funcionando in maquinas:
        disponible = monitorear_maquina(nombre, horas, funcionando)
        planificar_mantenimiento(nombre, horas, 100)
        if not disponible:
            print(nombre, "está detenida")
    rendimiento = analizar_rendimiento(85, 100)
    print("Rendimiento:", rendimiento, "%")
    ajustar_produccion(120, 100)


if __name__ == "__main__":
    main()
