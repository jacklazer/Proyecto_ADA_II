import heapq

def roV(n, tablones):
    tablones_ordenados = sorted(tablones, key=lambda x: x[2], reverse=True)

    inicio_riego = [0] * n  
    tiempo_actual = 0  
    cola_prioridad = []  

    for i, tablon in enumerate(tablones_ordenados):
        inicio_riego[i] = tiempo_actual
        tiempo_actual += tablon[1]  
        heapq.heappush(cola_prioridad, (inicio_riego[i], tablon))

    costo_total = 0
    while cola_prioridad:
        inicio, tablon = heapq.heappop(cola_prioridad)
        costo_total += max(0, tablon[2] * (inicio + tablon[1] - tablon[0]))

    print("Número de Tablones:", n)
    print("Costo Total de Riesgo:", costo_total)

    return inicio_riego, costo_total