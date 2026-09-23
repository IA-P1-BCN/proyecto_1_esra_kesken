# TaxiTech Solutions — Taxímetro

## Descripción del Proyecto

Programa que sustituye a los taxímetros físicos por una solución software: calcula el importe de un trayecto en tiempo real según el estado del taxi (parado o en movimiento).

## Problema que Resuelve

Los taxímetros físicos son difíciles de mantener y actualizar. Este proyecto digitaliza el cálculo de tarifas para facilitar el mantenimiento, la actualización de precios y la futura integración con otros sistemas (facturación, historial, apps).

## Para Quién

Empresas de taxi (como el cliente ficticio de este proyecto) que necesitan modernizar su sistema de tarificación.

## Requisitos del Cliente Implementados

- [x] Cálculo de tarifa en tiempo real según estado del taxi
- [x] Tarifa en movimiento (≥ 20 km/h): 0,05 €/segundo
- [x] Tarifa parado / velocidad baja (< 20 km/h): 0,02 €/segundo
- [x] Varios trayectos seguidos sin cerrar el programa

## Cómo Usar el Programa

Al ejecutar `taximetro.py`, el programa pide comandos en un bucle. Comandos disponibles:

| Comando | Acción |
|---|---|
| `iniciar` | Inicia un nuevo trayecto (estado inicial: parado) |
| `movimiento` | Cambia el estado a "en movimiento" |
| `parado` | Cambia el estado a "parado" |
| `finalizar` | Termina el trayecto, muestra el importe total y reinicia para el siguiente trayecto |
| `salir` | Cierra el programa |

## Niveles de Implementación

Este proyecto se organiza por **niveles**, no por fases rígidas.

### Nivel Esencial ✅

- [x] Programa ejecutable desde línea de comandos (bucle `while True` + `input()`)
- [x] Cálculo de tarifa en tiempo real usando `time.time()` (segundos reales transcurridos entre cambios de estado)
- [x] Cambio de estado (parado ↔ movimiento) con la tarifa correcta aplicada a cada tramo
- [x] Finalización del trayecto con importe total mostrado
- [x] Varios trayectos seguidos sin cerrar el programa (reinicio de `total`, `estado` y `marca_tiempo` tras finalizar)

### Nivel Medio ✅

- [x] Lógica separada en funciones (`calcular_importe`)
- [x] Tarifas configurables externamente (`config/tarifas.json`)
- [x] Historial de trayectos guardado en `logs/historial.txt`
- [x] Tests automáticos con pytest (`tests/test_taximetro.py`)
- [x] Manejo de errores de entrada (evita que el programa se rompa si se usa un comando antes de `iniciar`)

### Nivel Avanzado

*(en desarrollo — implementando interfaz con Streamlit en la rama feature/streamlit-gui)*


## Tecnologías

- **Lenguaje:** Python 3.12+
- **Control de versiones:** Git / GitHub
- **Gestión de entorno y dependencias:** [uv](https://github.com/astral-sh/uv)
- **Tests:** pytest

## Decisiones Técnicas

- **Medición de tiempo con `time.time()`:** se guarda una marca de tiempo (`marca_tiempo`) cada vez que cambia el estado del taxi. Al producirse el siguiente cambio (o al finalizar), se calcula el tiempo real transcurrido desde esa marca y se aplica la tarifa correspondiente al estado **anterior** (el que estaba activo durante ese tramo).
- **f-strings para la salida:** se usa `f"...{variable:.2f}€"` para mostrar importes con dos decimales de forma legible.
- **Tarifas en `config/tarifas.json`:** en vez de tenerlas fijas en el código, para poder cambiarlas sin tocar `taximetro.py`.
- **`if __name__ == "__main__":`:** protege el bucle principal para que `taximetro.py` se pueda importar de forma segura desde los tests, sin que se ejecute el programa interactivo.

## Organización del Proyecto y Estructura de Git

*(se documentará aquí cómo se organiza el trabajo: ramas, qué representa cada rama, y cómo evolucionó el proyecto)*

- `main`: rama principal, versión estable

## Instalación y Ejecución

```bash
uv sync           # instala las dependencias (incluye pytest)
uv run taximetro.py
```

## Tests

```bash
uv run pytest -v
```

## Autora

Esra Kesken

## Estado

Proyecto en desarrollo — Factoria F5 Barcelona.
