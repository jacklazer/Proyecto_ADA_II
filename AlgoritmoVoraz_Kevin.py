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

def solucion_voraz(nombre_archivo):
    """
    Función que encuentra una solución aproximada al problema de optimización del riego de tablones utilizando un enfoque voraz.
    
    Argumentos:
    nombre_archivo (str): Nombre del archivo de entrada.
    
    Retorna:
    costo_total (float): Costo total de riego obtenido con la solución aproximada.
    orden_riego (list): Lista de índices que representa el orden de riego de los tablones.
    """
    # Leer los datos de entrada desde el archivo
    n, tablones = leer_archivo(nombre_archivo)
    
    # Ordenar los tablones por tiempo de siembra (ts) de forma ascendente
    tablones.sort(key=lambda x: x[0])
    
    # Inicializar variables
    orden_riego = []
    tiempo_actual = 0
    costo_total = 0
    
    # Iterar sobre los tablones ordenados
    for ts, tr, p in tablones:
        # Si el tiempo actual es menor que el tiempo de siembra (ts), avanzar el tiempo
        # Calcular el tiempo que se debe avanzar y multiplicarlo por la penalización (p)
        tiempo_avanzado = max(0, ts - tiempo_actual)
        costo_total += p * tiempo_avanzado
        
        # Actualizar el tiempo actual al tiempo de siembra (ts)
        tiempo_actual = ts
        
        # Regar el tablón
        # Calcular el costo de riego como el máximo entre 0 y la diferencia entre el tiempo de riego (tr) y el tiempo transcurrido desde el inicio del riego (tiempo_actual - ts)
        costo_total += max(0, tr - (tiempo_actual - ts))
        
        # Actualizar el tiempo actual sumando el tiempo de riego (tr)
        tiempo_actual += tr
        
        # Agregar el índice del tablón actual a la lista orden_riego
        orden_riego.append(tablones.index((ts, tr, p)))
    
    # Devolver el costo total y el orden de riego obtenido
    return costo_total, orden_riego

print(solucion_voraz("Prueba29.txt"))