import heapq

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

    # Aquí están los tablones ya organizados
    tablones_ordenados = sorted(tablones, key=lambda x: x[2], reverse=True)

    # Variables principales:
    '''
        Tanto el inicio de riego para cada tablón y el tiempo de riego actual están definidas en inicio y tiempo
        Y la cola de prioridad donde se agregan los tablones mientras se calcula el tiempo se define en cola_prioridad
    '''
    inicio = [0] * n
    tiempo = 0
    cola_prioridad = []

    # Primer ciclo
    '''
         Primero se asigna el tiempo de inicio de riego del tablón actual al índice correspondiente en la lista de inicio
         luego aumentamos el tiempo actual por la duración de riego del tablón actual y finalmente se agrega el par a la cola
         de prioridad
    '''
    for i, tablon in enumerate(tablones_ordenados):
        inicio[i] = tiempo
        tiempo += tablon[1]
        heapq.heappush(cola_prioridad, (inicio[i], tablon))

    # Segundo ciclo
    '''
        Inicializamos el costo en 0 para empezar y dentro del while extraemos el par (tiempo,tablón) de la cola que habíamos agregado
        en el for, luego se calcula el costo de riego para el tablón actual teniendo en cuenta su tiempo de inicio y duración de riego
        y tomando en cuenta si el riego es antes o después de la hora deseada, evitando costos negativos
    '''
    costo = 0
    while cola_prioridad:
        inicio, tablon = heapq.heappop(cola_prioridad)
        costo += max(0, tablon[2] * (inicio + tablon[1] - tablon[0]))

    # Por último mostramos los resultados
    print("Tablones:", n)
    print("Costo:", costo)

    return inicio, costo

print(roV("Prueba30.txt"))