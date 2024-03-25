from itertools import permutations

# Calculador de todas las posibles programaciones
# def calculador_dtlpp(n):
#     numbers = list(range(n))  # Generar lista de números del 0 al n-1
#     permutations_list = list(permutations(numbers))  # Generar todas las permutaciones posibles
#     return [list(perm) for perm in permutations_list]  # Convertir las tuplas de permutaciones en listas

def calculador_dtlpp(n):
    # O(1)
    # Lista de listas con n elementos, donde cada lista (de adentro) tiene un elemento y cada elemento es un numero entre 0 y n-1
    indices = [[i] for i in range(n)]

    # O(k) | k = len(lista)
    # Esta funcion determina si un elemento pertenece a una lista
    def identificador_de_elemento(elemento, lista):
        verdaderos_y_falsos = [(elemento == e) for e in lista]

        for booleano in verdaderos_y_falsos:
            if booleano:
                return True
        return False

    # O(k^(k+1)) | k = len(contador)
    # Esta funcion genera todas las posibles combinaciones de los elementos de una lista de k elementos, donde cada combinacion tiene k posiciones, las posiciones de los elementos hacen distintas las combinaciones y no se repiten los elementos en una combinacion
    def combinador_de_elementos(lista_parcial, contador):
        if contador == 0:
            return lista_parcial
        else:
            nuevo_vector_parcial = [i + j for i in lista_parcial for j in indices if (identificador_de_elemento(j[0], i)==False)]
            return combinador_de_elementos(nuevo_vector_parcial, contador - 1)

    xd = combinador_de_elementos(indices, n-1)

    return xd





# Calculador de inicio de tiempo de riego
def calculador_didtdr(programacion, tablones):
    inicios_de_tiempos_de_riego = [0] * (len(programacion))
    turno = 0

    # O(k) | k = len(programacion)
    for tablon in programacion:
        if (turno == 0):
            inicios_de_tiempos_de_riego[tablon] = 0
        else:
            inicios_de_tiempos_de_riego[tablon] = inicios_de_tiempos_de_riego[programacion[turno-1]]+tablones[programacion[turno-1]][1]
        turno += 1

    return inicios_de_tiempos_de_riego





# Calculador de costo de riego
def calculador_dcdr(inicios_de_tiempos_de_riego, tablones):
    tablon = 0
    costo_total = 0

    # O(k) | k =len(inicios_de_tiempos_de_riego)
    for tiempo_de_inicio_de_riego  in inicios_de_tiempos_de_riego:
        if (tablones[tablon][0]-tablones[tablon][1] >= tiempo_de_inicio_de_riego):
            costo_total += tablones[tablon][0] - (tiempo_de_inicio_de_riego + tablones[tablon][1])
        else:
            costo_total += tablones[tablon][2] * ((tiempo_de_inicio_de_riego + tablones[tablon][1]) - tablones[tablon][0])
        tablon += 1

    return costo_total





# Calculador de solucion optima con fuerza bruta
def roFB(n, tablones):

    programaciones_posibles = calculador_dtlpp(n)
    programacion_optima = programaciones_posibles[0]
    costo_optimo = calculador_dcdr(calculador_didtdr(programacion_optima, tablones), tablones)

    for programacion in programaciones_posibles:
        posible_costo_optimo = calculador_dcdr(calculador_didtdr(programacion, tablones), tablones)

        # print(">>>", costo_optimo, "-", posible_costo_optimo)

        if (posible_costo_optimo < costo_optimo):
            # print("XDDD")
            programacion_optima = programacion
            costo_optimo = posible_costo_optimo
        
    print(costo_optimo)

    for tablon in programacion_optima:
        print(tablon)

    # programacion1 = [0, 1, 4, 2, 3]
    # x1 = calculador_didtdr(programacion1, tablones)
    # y1 = calculador_dcdr(x1, tablones)
    # programacion2 = [2, 1, 4, 3, 0]
    # x2 = calculador_didtdr(programacion2, tablones)
    # y2 = calculador_dcdr(x2, tablones)
    # print(x1, y1)
    # print(x2, y2)
