from itertools import permutations
"""
     Lee los datos de entrada desde un archivo y los devuelve como una tupla.
    
     Argumentos:
     nombre_archivo (str): Nombre del archivo de entrada.
    
     Retorna:
     n (int): Número de tablones.
     tablones (list): Lista de tuplas (ts, tr, p) que representan el tiempo de siembra, el tiempo de riego y la penalización para cada tablón.
     Complejidad: O(n), donde n es el número de tablones
"""
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        n = int(lineas[0].strip())
        tablones = []
        for linea in lineas[1:]:
            ts, tr, p = map(int, linea.strip().split(','))
            tablones.append((ts, tr, p))
        return n, tablones

"""
    Función recursiva que calcula el costo mínimo y la programación óptima de riego para un estado dado.
    
    Argumentos:
    state (tuple): Tupla de índices de tablones que quedan por regar.
    tablones (list): Lista de tuplas (ts, tr, p) que representan los tablones.
    dp (dict): Diccionario para almacenar los resultados ya calculados (memoización).
    
    Retorna:
    min_cost (float): Costo mínimo para regar los tablones en el estado dado.
    optimal_order (list): Lista de índices que representa la programación óptima de riego.
    Complejidad: O(n * 2^n), donde n es el número de tablones
"""
def cost(state, tablones, dp):
    if not state:
        return 0, []

    if state in dp:
        return dp[state]

    min_cost = float('inf')
    optimal_order = []
    
    for i in range(len(state)):
        remaining_state = tuple(sorted(set(state) - {state[i]}))
        temp_cost, temp_order = cost(remaining_state, tablones, dp)
        
        sub_cost = tablones[state[i]][0] - sum(tablones[j][1] for j in remaining_state) - tablones[state[i]][1]
        cost_i = sub_cost if sub_cost > 0 else tablones[state[i]][2] * (-sub_cost)
        
        if temp_cost + cost_i < min_cost:
            min_cost = temp_cost + cost_i
            optimal_order = [state[i]] + temp_order
    
    dp[state] = (min_cost, optimal_order)
    return min_cost, optimal_order

"""
    Función principal que resuelve el problema de optimización del riego de tablones.
    
    Argumentos:
    nombre_archivo (str): Nombre del archivo de entrada.
    
    Retorna:
    min_cost (float): Costo mínimo para regar todos los tablones.
    optimal_order (list): Lista de índices que representa la programación óptima de riego.

    # Código para leer los datos de entrada
    # Llamada a la función cost con el estado inicial
    # Complejidad: O(n * 2^n), donde n es el número de tablones
"""
def solucion_optima(nombre_archivo):
    n, tablones = leer_archivo(nombre_archivo)
    initial_state = tuple(range(n))
    dp = {}
    min_cost, optimal_order = cost(initial_state, tablones, dp)
    return min_cost, optimal_order

def roPD(finca):
    n = len(finca)
    initial_state = tuple(range(n))
    dp = {}
    min_cost, optimal_order = cost(initial_state, finca, dp)

    # O(1)
    print(min_cost)

    # O(n) | n = len(optimal_order)
    for tablon in reversed(optimal_order):
        print(tablon)





# resultado = solucion_optima('prueba4.txt')
# print(f"Tiempo óptimo de riego: {resultado[0]}")
# print(f"Programación óptima de riego: {resultado[1]}")





# print("========")

# import Algoritmo_Fuerza_Bruta
# finca_ = leer_archivo('prueba4.txt')

# tiempos_de_riego = Algoritmo_Fuerza_Bruta.calculador_didtdr(resultado[1], finca_[1])
# verificacion_de_costo = Algoritmo_Fuerza_Bruta.calculador_dcdr(tiempos_de_riego, finca_[1])
# print(tiempos_de_riego, verificacion_de_costo)

# print("========")

# resultado_revertido = resultado[1][::-1]
# tiempos_de_riego2 = Algoritmo_Fuerza_Bruta.calculador_didtdr(resultado_revertido, finca_[1])
# verificacion_de_costo2 = Algoritmo_Fuerza_Bruta.calculador_dcdr(tiempos_de_riego2, finca_[1])
# print(tiempos_de_riego2, verificacion_de_costo2)

# print("========")

# # resultado2 = solucion_optima('pruebaX.txt')
# # print(f"Tiempo óptimo de riego: {resultado2[0]}")
# # print(f"Programación óptima de riego: {resultado2[1]}")
