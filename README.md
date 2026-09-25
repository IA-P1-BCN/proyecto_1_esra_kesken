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
| `historial` | Muestra el histórico de trayectos registrados |
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
- [x] Historial de trayectos guardado en `logs/historial.txt` y visible con el comando `historial`
- [x] Tests automáticos con pytest (`tests/test_taximetro.py`)
- [x] Manejo de errores de entrada (evita que el programa se rompa si se usa un comando antes de `iniciar`)
- [x] Logs de operación con el módulo `logging` (`logs/app.log`), para diagnóstico técnico

### Nivel Avanzado ✅

- [x] Interfaz gráfica con Streamlit (`streamlit_app.py`), reutilizando `calcular_importe` de `taximetro.py`
- [x] Botones grandes y táctiles, pensados para uso en móvil/tablet
- [x] También registra los trayectos en `logs/historial.txt`, igual que la versión CLI

**Ejecución:**
```bash
uv run streamlit run streamlit_app.py
```


## Tecnologías

- **Lenguaje:** Python 3.12+
- **Control de versiones:** Git / GitHub
- **Gestión de entorno y dependencias:** [uv](https://github.com/astral-sh/uv)
- **Tests:** pytest
- **Interfaz gráfica:** Streamlit

## Decisiones Técnicas

- **Streamlit para la interfaz gráfica:** elegido en vez de Flask u otro framework porque ya tenía experiencia previa con Streamlit (bootcamp de datos), lo que permitió centrarme en la lógica del taxímetro en vez de aprender un framework nuevo desde cero.

- **Medición de tiempo con `time.time()`:** se guarda una marca de tiempo (`marca_tiempo`) cada vez que cambia el estado del taxi. Al producirse el siguiente cambio (o al finalizar), se calcula el tiempo real transcurrido desde esa marca y se aplica la tarifa correspondiente al estado **anterior** (el que estaba activo durante ese tramo).
- **f-strings para la salida:** se usa `f"...{variable:.2f}€"` para mostrar importes con dos decimales de forma legible.
- **Tarifas en `config/tarifas.json`:** en vez de tenerlas fijas en el código, para poder cambiarlas sin tocar `taximetro.py`.
- **`if __name__ == "__main__":`:** protege el bucle principal para que `taximetro.py` se pueda importar de forma segura desde los tests, sin que se ejecute el programa interactivo.

## Estructura del Proyecto

```
proyecto_1_esra_kesken/
├── taximetro.py           # Lógica principal (calcular_importe) y versión CLI
├── streamlit_app.py       # Interfaz gráfica (nivel avanzado)
├── config/
│   └── tarifas.json       # Tarifas configurables
├── logs/
│   ├── historial.txt      # Historial de trayectos (generado, no versionado)
│   └── app.log             # Logs técnicos (generado, no versionado)
├── tests/
│   └── test_taximetro.py  # Tests automáticos
├── .streamlit/
│   └── config.toml         # Tema visual (colores)
├── pyproject.toml          # Dependencias del proyecto
└── README.md
```

## Organización del Proyecto y Estructura de Git

El trabajo se organiza en un tablero Kanban (GitHub Projects: Backlog / In Progress / Done), con tareas etiquetadas por nivel (`[Medio]`, `[Avanzado]`). El nivel esencial e inicio del nivel medio se desarrollaron directamente en `main`, con commits siguiendo el formato de [conventional commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `test:`, `docs:`, `chore:`).

- `main`: rama principal, versión estable
- `feature/streamlit-gui`: desarrollo de la interfaz gráfica (nivel avanzado)

A modo de práctica del flujo de trabajo en equipo, se hizo el mismo cambio en `main` y en `feature/streamlit-gui` a propósito, provocando un conflicto de merge, que se resolvió manualmente al integrar la rama en `main`.

## Instalación y Ejecución

```bash
uv sync           # instala las dependencias (incluye pytest)
uv run taximetro.py
```

## Tests

```bash
uv run pytest -v
```

## Futuras Mejoras

- Para uso real por parte de un taxista, la interfaz debería desplegarse como una app web alojada (accesible sin terminal) o empaquetarse como app móvil/tablet.
- El cambio de estado (parado/movimiento) es manual en esta versión. En un sistema real, debería detectarse automáticamente mediante GPS o un sensor de velocidad del vehículo, sin intervención del conductor.
- Protección con contraseña (solicitada por el responsable de flota, para evitar manipulaciones) no se ha implementado por ser de prioridad baja; quedaría pendiente para una futura iteración.

## Autora

Esra Kesken

## Estado

Proyecto en desarrollo — Factoria F5 Barcelona.
