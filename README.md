# Python 2026 - Actividad 2

Resolución del ejercicio 10: Simulación de competencia de cocina y ranking.

## Estructura del proyecto

```
practica2/
├── src/
│   └── competencia.py      # Lógica del ejercicio 10
├── notebooks/
│   └── ejercicio10.ipynb   # Notebook con la ejecución del ejercicio
└── README.md
```

## Requisitos

- Python 3.8 o superior
- Jupyter Notebook

## Instalación de dependencias

El ejercicio 10 no requiere librerías externas (solo Python estándar).

Para instalar Jupyter Notebook:

```bash
pip install notebook
```

## Cómo ejecutar

### Opción 1: Desde el notebook (recomendado)

```bash
jupyter notebook notebooks/ejercicio10.ipynb
```

Una vez abierto el notebook, ejecutar todas las celdas con **Kernel > Restart & Run All**.

### Opción 2: Desde la terminal

```bash
python src/competencia.py
```

## Descripción del ejercicio 10

Se simula una competencia de cocina con:
- **5 participantes**: Valentina, Mateo, Camila, Santiago, Lucía
- **5 rondas**: Entrada, Plato principal, Postre, Cocina internacional, Final libre
- **3 jueces** por ronda, cada uno otorga un puntaje del 1 al 10

El programa imprime:
1. La tabla de posiciones luego de cada ronda (con el ganador de esa ronda)
2. Una tabla final con: puntaje total, rondas ganadas, mejor puntaje en una ronda y promedio por ronda
