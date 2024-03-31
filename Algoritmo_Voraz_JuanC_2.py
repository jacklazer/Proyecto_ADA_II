import Algoritmo_Fuerza_Bruta





# Calculador de costo de ultimo riego
def calculador_dcdur(tablon, tiempo_total_de_regado):

    # costo += tablon[0] - (inicio_de_tiempo_de_riego + tablon[1])

    costo = tablon[2] * (tiempo_total_de_regado - tablon[0])

    return costo





# Verificador de prioridad mas grande
def verificador_dpmg(a, b, finca):
    if (finca[a][2] >= finca[b][2]):
        return a
    elif (finca[b][2] > finca[a][2]):
        return b





# Calculador de programacion optima
def calculador_dpo(costos_de_ultimo_riego, programacion_optima, finca, n):

    tablon_actual = 0
    costo_mas_costoso = 0
    tablon_mas_costoso = -1

    for costo_de_ultimo_riego in costos_de_ultimo_riego:
        # print("===")
        if not(tablon_actual in programacion_optima):
            # print(costo_de_ultimo_riego, "-", costo_mas_costoso)
            if (costo_de_ultimo_riego > costo_mas_costoso):
                # print(costo_de_ultimo_riego, "-", costo_mas_costoso)
                # print(tablon_actual, "-", tablon_mas_costoso)
                costo_mas_costoso = costo_de_ultimo_riego
                tablon_mas_costoso = tablon_actual
                # print(tablon_actual, "-", tablon_mas_costoso)
            elif (costo_de_ultimo_riego == costo_mas_costoso):
                # print(tablon_actual, "-", tablon_mas_costoso)
                tablon_mas_costoso = verificador_dpmg(tablon_actual, tablon_mas_costoso, finca)
                costo_mas_costoso = costos_de_ultimo_riego[tablon_mas_costoso]
                # print(tablon_actual, "-", tablon_mas_costoso)

        tablon_actual += 1

    programacion_optima.append(tablon_mas_costoso)

    if (len(programacion_optima) == n):
        return programacion_optima
    else:
        return calculador_dpo(costos_de_ultimo_riego, programacion_optima, finca, n)





def roV(finca):
    n = len(finca)

    tiempo_total_de_regado = 0

    costos_de_ultimo_riego = []

    for tablon in finca:
        tiempo_total_de_regado += tablon[1]

    for tablon in finca:
        costos_de_ultimo_riego.append(calculador_dcdur(tablon, tiempo_total_de_regado))

    programacion_optima_ = []
    programacion_optima = []
    programacion_optima = calculador_dpo(costos_de_ultimo_riego, programacion_optima_, finca, n)

    return (programacion_optima, Algoritmo_Fuerza_Bruta.calculador_dcdr(Algoritmo_Fuerza_Bruta.calculador_didtdr(programacion_optima, finca), finca))