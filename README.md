# Ejercicios de modularidad en Python

Este proyecto contiene cinco problemas resueltos con **funciones y procedimientos**. Los ejemplos usan solamente Python y datos de prueba, por lo que no requieren librerías adicionales, sensores reales ni conexión a internet.

## Cómo ejecutar

Instalar Python 3 y abrir una terminal en esta carpeta. Ejecutar cada ejercicio con:

```bash
python problema1_temperatura.py
python problema2_inventario.py
python problema3_navegacion.py
python problema4_produccion.py
python problema5_riego.py
```

En algunos sistemas el comando es `python3`.

## Problema 1: Temperatura

- `leer_temperatura`: obtiene una temperatura simulada según la zona.
- `calcular_temperatura_optima`: decide la temperatura objetivo según la hora, ocupación y clima exterior.
- `ajustar_clima`: indica si conviene refrigerar o calentar.
- `analizar_consumo`: suma y promedia estimaciones de consumo.

**Rendimiento:** cada zona se revisa una vez; separar las funciones permite cambiar sensores o reglas sin modificar todo el programa. Los kWh son estimados, no medidos.

## Problema 2: Inventario

- `registrar_entrada`: añade unidades al producto.
- `registrar_salida`: descuenta unidades si hay stock suficiente.
- `calcular_nivel_optimo`: calcula la demanda durante reposición más una reserva.
- `generar_alerta`: muestra cuánto falta para llegar al nivel recomendado.

**Rendimiento:** el diccionario permite consultar y actualizar rápidamente cada producto; las alertas revisan todos los productos una vez.

## Problema 3: Navegación

- `leer_sensores`: entrega lecturas simuladas de proximidad, cámara y tráfico.
- `calcular_ruta_optima`: elige el menor tiempo entre rutas dadas.
- `detectar_obstaculo`: verifica la lectura de distancia y cámara.
- `evitar_obstaculo`: presenta una alerta de detención y recálculo.
- `ajustar_velocidad`: determina una velocidad simulada según tráfico y obstáculos.

**Rendimiento:** elegir entre rutas dadas requiere revisarlas una vez. Es una demostración, no un sistema de navegación seguro para un automóvil real; no calcula rutas geográficas ni ejecuta maniobras.

## Problema 4: Producción

- `monitorear_maquina`: informa horas y disponibilidad.
- `planificar_mantenimiento`: recomienda intervenir al alcanzar un límite de horas.
- `analizar_rendimiento`: calcula el porcentaje de producción frente a la meta.
- `ajustar_produccion`: programa hasta la capacidad disponible e informa la demanda pendiente.

**Rendimiento:** se procesa cada máquina una vez; estas funciones evitan repetir cálculos y ayudan a identificar paradas.

## Problema 5: Riego

- `leer_humedad`: lee porcentajes simulados por sección.
- `consultar_clima`: devuelve una previsión ficticia de lluvia.
- `calcular_riego`: estima los litros a aplicar si falta humedad y no se espera lluvia.
- `controlar_valvula`: muestra si una válvula se abriría o permanecería cerrada.

**Rendimiento:** cada sección se evalúa una vez; solo las secciones que lo necesitan reciben una recomendación de riego. Las cantidades son ilustrativas y no deben aplicarse directamente a cultivos reales.

## Nota sobre modularidad

Las funciones reciben datos como parámetros, devuelven resultados cuando corresponde y pueden reutilizarse. Los procedimientos (`ajustar_clima`, `generar_alerta`, `evitar_obstaculo`, `ajustar_velocidad`, `planificar_mantenimiento` y `ajustar_produccion`, entre otros) muestran acciones sin que el resto del programa deba repetirlas. La modularidad facilita la lectura, las pruebas y las modificaciones; por sí sola no garantiza que el programa sea más rápido.

## Publicar en GitHub

1. Crear un repositorio nuevo en GitHub, por ejemplo `ejercicios-modularidad-python`.
2. Subir estos seis archivos a la raíz del repositorio (opción **Add file > Upload files**).
3. Confirmar los cambios (**Commit changes**).
4. Copiar el enlace del repositorio y entregarlo al docente.
