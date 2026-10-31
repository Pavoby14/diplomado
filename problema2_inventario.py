# Problema 2: Inventario de un almacén

def registrar_entrada(inventario, producto, cantidad):
    # Suma productos al inventario.
    if cantidad <= 0:
        print("La cantidad debe ser positiva")
        return False
    inventario[producto] = inventario.get(producto, 0) + cantidad
    return True


def registrar_salida(inventario, producto, cantidad):
    # Descuenta solo si existen suficientes productos.
    if cantidad <= 0 or inventario.get(producto, 0) < cantidad:
        print("No hay stock suficiente o la cantidad no es válida")
        return False
    inventario[producto] -= cantidad
    return True


def calcular_nivel_optimo(venta_diaria, dias_reposicion, reserva):
    # Stock recomendado para cubrir la demanda y tener reserva.
    return venta_diaria * dias_reposicion + reserva


def generar_alerta(producto, actual, nivel_optimo):
    # Indica cuánto hay que pedir, sin exceder el objetivo.
    if actual < nivel_optimo:
        print("Reabastecer", producto, "con", nivel_optimo - actual, "unidades")
    else:
        print(producto, "tiene suficiente stock")


def main():
    inventario = {"arroz": 12, "azucar": 30}
    registrar_entrada(inventario, "arroz", 8)
    registrar_salida(inventario, "azucar", 5)
    print("Inventario:", inventario)
    demanda = {"arroz": 7, "azucar": 3}
    for producto, cantidad in inventario.items():
        nivel = calcular_nivel_optimo(demanda[producto], 4, 5)
        generar_alerta(producto, cantidad, nivel)


if __name__ == "__main__":
    main()
