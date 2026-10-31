# Ejercicios de modularidad en Python

Este proyecto contiene cinco problemas resueltos con **funciones y procedimientos**


```bash
python problema1_temperatura.py
python problema2_inventario.py
python problema3_navegacion.py
python problema4_produccion.py
python problema5_riego.py
```
## Problema 1: Temperatura

- `leer_temperatura`: obtiene una temperatura simulada según la zona.
- `calcular_temperatura_optima`: decide la temperatura objetivo según la hora, ocupación y clima exterior.
- `ajustar_clima`: indica si conviene refrigerar o calentar.
- `analizar_consumo`: suma y promedia estimaciones de consumo.

## Problema 2: Inventario

- `registrar_entrada`: añade unidades al producto.
- `registrar_salida`: descuenta unidades si hay stock suficiente.
- `calcular_nivel_optimo`: calcula la demanda durante reposición más una reserva.
- `generar_alerta`: muestra cuánto falta para llegar al nivel recomendado.

## Problema 3: Navegación

- `leer_sensores`: entrega lecturas simuladas de proximidad, cámara y tráfico.
- `calcular_ruta_optima`: elige el menor tiempo entre rutas dadas.
- `detectar_obstaculo`: verifica la lectura de distancia y cámara.
- `evitar_obstaculo`: presenta una alerta de detención y recálculo.
- `ajustar_velocidad`: determina una velocidad simulada según tráfico y obstáculos.

## Problema 4: Producción

- `monitorear_maquina`: informa horas y disponibilidad.
- `planificar_mantenimiento`: recomienda intervenir al alcanzar un límite de horas.
- `analizar_rendimiento`: calcula el porcentaje de producción frente a la meta.
- `ajustar_produccion`: programa hasta la capacidad disponible e informa la demanda pendiente.

## Problema 5: Riego

- `leer_humedad`: lee porcentajes simulados por sección.
- `consultar_clima`: devuelve una previsión ficticia de lluvia.
- `calcular_riego`: estima los litros a aplicar si falta humedad y no se espera lluvia.
- `controlar_valvula`: muestra si una válvula se abriría o permanecería cerrada.

## Nota sobre modularidad

Las funciones reciben datos como parámetros, devuelven resultados cuando corresponde y pueden reutilizarse. Los procedimientos (`ajustar_clima`, `generar_alerta`, `evitar_obstaculo`, `ajustar_velocidad`, `planificar_mantenimiento` y `ajustar_produccion`, entre otros) muestran acciones sin que el resto del programa deba repetirlas. La modularidad facilita la lectura, las pruebas y las modificaciones; por sí sola no garantiza que el programa sea más rápido.
