def roV(n, tablones):
    # Función para calcular la relación entre el tiempo de supervivencia restante y el tiempo de regado
    def calcular_relacion(tablon):
        return (tablones[tablon][0] - tablones[tablon][1]) / tablones[tablon][1]

    # Inicialización de la lista de tablones no regados
    tablones_no_regados = list(range(n))

    # Inicialización de la lista de programación óptima
    programacion_optima = []

    # Mientras haya tablones no regados
    while tablones_no_regados:
        # Seleccionar el tablón con la menor relación
        tablon_seleccionado = min(tablones_no_regados, key=calcular_relacion)
        # Agregar el tablón seleccionado a la programación óptima
        programacion_optima.append(tablon_seleccionado)
        # Eliminar el tablón seleccionado de la lista de tablones no regados
        tablones_no_regados.remove(tablon_seleccionado)

    # Calcular el costo total de riego
    costo_total = sum((tablones[i][0] - (programacion_optima.index(i) * tablones[i][1])) if programacion_optima.index(i) * tablones[i][1] < tablones[i][0] else tablones[i][2] * (programacion_optima.index(i) * tablones[i][1] - tablones[i][0]) for i in programacion_optima)

    # Imprimir la solución óptima
    print("Solución óptima:")
    print("Costo total de riego:", costo_total)
    for tablon in programacion_optima:
        print(tablon)


