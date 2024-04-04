import Algoritmo_Fuerza_Bruta





# Calculador de costos de ultimo riego
# O(1)
def calculador_dcdur(tablon, tiempo_total_de_regado):
    costo = tablon[2] * (tiempo_total_de_regado - tablon[0])
    return costo





# Verificador de prioridad mas grande
# O(1)
def verificador_dpmg(a, b, finca):
    if (finca[a][2] >= finca[b][2]):
        return a
    elif (finca[b][2] > finca[a][2]):
        return b





# Calculador de programacion optima
# O(n+2 + (n+2-1) + ... + 2+2 + 1+2) = O(n) | n = len(costos_de_ultimo_riego)
def calculador_dpo(costos_de_ultimo_riego, programacion_optima, finca, n):
    # O(1)
    tablon_actual = 0
    costo_mas_costoso = 0
    tablon_mas_costoso = -1

    # O(n) | n=len(costos_de_ultimo_riego)
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

    # O(1)
    if (len(programacion_optima) == n):
        return programacion_optima
    else:
        # O(n-1)
        return calculador_dpo(costos_de_ultimo_riego, programacion_optima, finca, n)





# Respuesta obtenida Voras
# O(1 + n + n + 1 + n + n) = O(n)
def roV(finca):
    # O(1)
    n = len(finca)
    tiempo_total_de_regado = 0
    costos_de_ultimo_riego = []

    # O(n)
    for tablon in finca:
        tiempo_total_de_regado += tablon[1]

    # O(n)
    for tablon in finca:
        # O(1 + 1) = O(1)
        costos_de_ultimo_riego.append(calculador_dcdur(tablon, tiempo_total_de_regado))

    # O(1)
    programacion_optima_ = []

    # O(n)
    programacion_optima = calculador_dpo(costos_de_ultimo_riego, programacion_optima_, finca, n)

    # O(n + n) = O(2n) = O(n)
    return (programacion_optima, Algoritmo_Fuerza_Bruta.calculador_dctdr(Algoritmo_Fuerza_Bruta.calculador_didtdr(programacion_optima, finca), finca))
