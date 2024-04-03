import heapq
import Algoritmo_Fuerza_Bruta

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    n = int(lineas[0].strip())
    finca = []
    for linea in lineas[1:]:
        ts, tr, p = map(int, linea.strip().split(','))
        finca.append((ts, tr, p))
    return n, finca

def calculador_dcdur(tablon, tiempo_total_de_regado):
    costo = tablon[2] * (tiempo_total_de_regado - tablon[0])
    return costo

def verificador_dpmg(a, b, finca):
    if (finca[a][2] >= finca[b][2]):
        return a
    elif (finca[b][2] > finca[a][2]):
        return b
def calculador_dpo(costos_de_ultimo_riego, programacion_optima, finca, n):
    tablon_actual = 0
    costo_mas_costoso = 0
    tablon_mas_costoso = -1
    for costo_de_ultimo_riego in costos_de_ultimo_riego:
        if not(tablon_actual in programacion_optima):
            if (costo_de_ultimo_riego > costo_mas_costoso):
                costo_mas_costoso = costo_de_ultimo_riego
                tablon_mas_costoso = tablon_actual
            elif (costo_de_ultimo_riego == costo_mas_costoso):
                tablon_mas_costoso = verificador_dpmg(tablon_actual, tablon_mas_costoso, finca)
                costo_mas_costoso = costos_de_ultimo_riego[tablon_mas_costoso]
        tablon_actual += 1
    programacion_optima.append(tablon_mas_costoso)
    if (len(programacion_optima) == n):
        return programacion_optima
    else:
        return calculador_dpo(costos_de_ultimo_riego, programacion_optima, finca, n)
    
def roV(nombre_archivo):
    n, finca = leer_archivo(nombre_archivo)
    tiempo_total_de_regado = sum(tablon[1] for tablon in finca)

    # Ordenar los tablones según su prioridad de manera descendente
    finca_ordenada = sorted(enumerate(finca), key=lambda x: (-x[1][2], abs(x[1][0] - tiempo_total_de_regado)), reverse=False)

    # Variables principales
    inicio = [0] * n  # Tiempo de inicio de riego para cada tablón
    tiempo = 0  # Tiempo de riego actual
    cola_prioridad = []  # Cola de prioridad para almacenar los tablones

    # Primer ciclo
    for i, tablon in finca_ordenada:
        inicio[i] = tiempo
        tiempo += tablon[1]
        heapq.heappush(cola_prioridad, (inicio[i], tablon))

    # Segundo ciclo
    costos_de_ultimo_riego = []
    while cola_prioridad:
        inicio, tablon = heapq.heappop(cola_prioridad)
        costos_de_ultimo_riego.append(calculador_dcdur(tablon, tiempo_total_de_regado))

    programacion_optima_ = []
    programacion_optima = calculador_dpo(costos_de_ultimo_riego, programacion_optima_, [tablon for i, tablon in finca_ordenada], n)

    return (programacion_optima, Algoritmo_Fuerza_Bruta.calculador_dctdr(Algoritmo_Fuerza_Bruta.calculador_didtdr(programacion_optima, [tablon for i, tablon in finca_ordenada]), [tablon for i, tablon in finca_ordenada]))

print(roV("Prueba5.txt"))