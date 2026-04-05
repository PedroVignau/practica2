"""
Ejercicio 10: Simulación de competencia de cocina y ranking
"""
 
rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Mateo':     {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Camila':    {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Santiago':  {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
            'Lucía':     {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
        }
    },
    {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Mateo':     {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Camila':    {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
            'Santiago':  {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
            'Lucía':     {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
        }
    },
    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Mateo':     {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Camila':    {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Santiago':  {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
            'Lucía':     {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
        }
    },
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
            'Mateo':     {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
            'Camila':    {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
            'Santiago':  {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
            'Lucía':     {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
        }
    },
    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
            'Mateo':     {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
            'Camila':    {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
            'Santiago':  {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            'Lucía':     {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
        }
    },
]
 
 
def puntaje_ronda(scores_cocinero):
    """Suma los puntajes de los tres jueces para un cocinero en una ronda."""
    return sum(scores_cocinero.values())
 
 
def simular_competencia(rounds):
    """
    Simula la competencia ronda a ronda.
    Retorna el acumulado final con estadísticas por cocinero.
    """
    cocineros = list(rounds[0]['scores'].keys())
 
    # Acumuladores
    acumulado = {c: 0 for c in cocineros}
    rondas_ganadas = {c: 0 for c in cocineros}
    mejor_ronda = {c: 0 for c in cocineros}
 
    for num_ronda, ronda in enumerate(rounds, start=1):
        theme = ronda['theme']
        scores = ronda['scores']
 
        # Puntajes de esta ronda
        pts_ronda = {c: puntaje_ronda(scores[c]) for c in cocineros}
 
        # Ganador de la ronda
        ganador = max(pts_ronda, key=lambda c: pts_ronda[c])
        rondas_ganadas[ganador] += 1
 
        # Actualizar acumulados y mejor ronda
        for c in cocineros:
            acumulado[c] += pts_ronda[c]
            if pts_ronda[c] > mejor_ronda[c]:
                mejor_ronda[c] = pts_ronda[c]
 
        # Imprimir tabla de la ronda
        print(f"\nRonda {num_ronda} - {theme}:")
        print(f"  Ganador: {ganador} ({pts_ronda[ganador]} pts)")
        print(f"  {'Cocinero':<12} {'Pts ronda':>10} {'Acumulado':>10}")
        print(f"  {'-'*34}")
        tabla_ronda = sorted(cocineros, key=lambda c: acumulado[c], reverse=True)
        for c in tabla_ronda:
            print(f"  {c:<12} {pts_ronda[c]:>10} {acumulado[c]:>10}")
 
    return acumulado, rondas_ganadas, mejor_ronda, len(rounds)
 
 
def imprimir_tabla_final(acumulado, rondas_ganadas, mejor_ronda, total_rondas):
    """Imprime la tabla de posiciones final ordenada por puntaje total."""
    cocineros = sorted(acumulado, key=lambda c: acumulado[c], reverse=True)
 
    print("\n" + "=" * 62)
    print("TABLA DE POSICIONES FINAL")
    print("=" * 62)
    print(f"{'Cocinero':<12} {'Puntaje':>8} {'Rondas gan.':>12} {'Mejor ronda':>12} {'Promedio':>9}")
    print("-" * 62)
    for c in cocineros:
        promedio = acumulado[c] / total_rondas
        print(
            f"{c:<12} {acumulado[c]:>8} {rondas_ganadas[c]:>12} {mejor_ronda[c]:>12} {promedio:>9.1f}"
        )
    print("-" * 62)
 
 
def main():
    acumulado, rondas_ganadas, mejor_ronda, total_rondas = simular_competencia(rounds)
    imprimir_tabla_final(acumulado, rondas_ganadas, mejor_ronda, total_rondas)
 
 
if __name__ == "__main__":
    main()