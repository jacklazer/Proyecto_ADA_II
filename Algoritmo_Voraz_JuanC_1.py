import sys
import Algoritmo_Fuerza_Bruta





# Calculador de costo de riego
def calculador_dcdr(inicio_de_tiempo_de_riego, tablon):
    i = 0
    costo = 0

    if (tablon[0]-tablon[1] >= inicio_de_tiempo_de_riego):
        costo += tablon[0] - (inicio_de_tiempo_de_riego + tablon[1])
    else:
        costo += tablon[2] * ((inicio_de_tiempo_de_riego + tablon[1]) - tablon[0])
    i += 1

    return costo




# Verificador de prioridad mas grande
def verificador_dpmg(a, b, finca):
    if (finca[a][2] >= finca[b][2]):
        return a
    elif (finca[b][2] > finca[a][2]):
        return b





# Calculador de programacion optima
def calculador_dpo(finca, n, inicio_de_tiempo_de_riego, programacion_optima):
    # n = len(finca)
    costos = []

    # inicio_de_tiempo_de_riego = 0

    for tablon in finca:
        costos.append(calculador_dcdr(inicio_de_tiempo_de_riego, tablon))

    costo_menos_costoso = sys.maxsize
    tablon_menos_costoso = -1
    # tablon_actual = 0

    # print("======")
    for i in range(n):
        # print("===")
        if not(i in programacion_optima):
            # print(">", i)
            costo = costos[i]

            if (costo < costo_menos_costoso):
                # print(">>")
                # tablon_menos_costoso = tablon_actual
                tablon_menos_costoso = i
                costo_menos_costoso = costo
            elif (costo == costo_menos_costoso):
                # print(">>>")
                # tablon_menos_costoso = verificador_dpmg(tablon_menos_costoso, tablon_actual, finca)
                tablon_menos_costoso = verificador_dpmg(tablon_menos_costoso, i, finca)
                # costo_menos_costoso = finca[tablon_menos_costoso][2]
                costo_menos_costoso = costos[tablon_menos_costoso]

        # tablon_actual += 1

    inicio_de_tiempo_de_riego += finca[tablon_menos_costoso][1]

    programacion_optima.append(tablon_menos_costoso)
    # print(">", tablon_menos_costoso)

    if (len(programacion_optima) == n):
        return programacion_optima
    else:
        return calculador_dpo(finca, n, inicio_de_tiempo_de_riego, programacion_optima)

    



def roV(finca):
    n = len(finca)

    inicio_de_tiempo_de_riego =0
    programacion_optima_ = []

    programacion_optima = calculador_dpo(finca, n, inicio_de_tiempo_de_riego, programacion_optima_)

    return (programacion_optima, Algoritmo_Fuerza_Bruta.calculador_dcdr(Algoritmo_Fuerza_Bruta.calculador_didtdr(programacion_optima, finca), finca))