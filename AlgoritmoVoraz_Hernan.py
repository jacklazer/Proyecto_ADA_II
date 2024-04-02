def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    n = int(lineas[0].strip())
    tablones = []
    for linea in lineas[1:]:
        ts, tr, p = map(int, linea.strip().split(','))
        tablones.append((ts, tr, p))
    return n, tablones

def roV(nombre_archivo):
    n, tablones = leer_archivo(nombre_archivo)

    # Ordenar los tablones según su prioridad de manera descendente
    tablones_ordenados = sorted(tablones, key=lambda x: x[2], reverse=True)

    # Inicializar variables
    inicio_riego = [0] * n  # Tiempo de inicio de riego para cada tablón
    tiempo_riego = 0  # Tiempo de riego actual

    # Iterar sobre los tablones ordenados
    for i in range(n):
        tablon = tablones_ordenados[i]

        # Calcular el tiempo de inicio de riego del tablón
        inicio_riego[tablones.index(tablon)] = tiempo_riego
        tiempo_riego += tablon[1]  # Sumar el tiempo de riego del tablón actual

    # Calcular el costo total de riego
    costo_total = sum((tablon[0] - inicio_riego[i] - tablon[1]) if (tablon[0] - inicio_riego[i] - tablon[1]) > 0 else tablon[2] * ((inicio_riego[i] + tablon[1]) - tablon[0]) for i, tablon in enumerate(tablones))

    # Imprimir resultados
    print("N. Tablones:", n)
    print("Valor Solución(costo de riesgo):", costo_total)

    return inicio_riego, costo_total

print(roV("Prueba30.txt"))