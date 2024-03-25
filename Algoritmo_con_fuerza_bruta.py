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
        # Lista de booleanos donde cada elemento es True si el elemento en esa posición de 'lista' es igual a 'elemento', False en caso contrario
        verdaderos_y_falsos = [(elemento == e) for e in lista]

        # Respuesta a si el elemento se encuentra en la lista
        for booleano in verdaderos_y_falsos:
            if booleano:
                return True
        return False

    # O(k*(k+1)) | k = len(contador)
    # Esta funcion genera todas las posibles combinaciones de los elementos en una lista de enteros
    def combinador_de_elementos(lista_parcial, contador):
        if contador == 0:
            return lista_parcial  # Aquí la lista parcial ya es la final
        else:
            nuevo_vector_parcial = [i + j for i in lista_parcial for j in indices if (identificador_de_elemento(j[0], i)==False)]
            return combinador_de_elementos(nuevo_vector_parcial, contador - 1)

    xd = combinador_de_elementos(indices, n-1)

    return xd

# Calculador de inicio de tiempo de riego
def calculador_didtdr(programacion, tablones):
    inicio_de_tiempo_de_riego = [0] * (len(programacion))
    turno = 0
    for i in programacion:
        if (turno == 0):
            inicio_de_tiempo_de_riego[i] = 0
        else:
            inicio_de_tiempo_de_riego[i] = inicio_de_tiempo_de_riego[programacion[turno-1]]+tablones[programacion[turno-1]][1]
        turno += 1
    return inicio_de_tiempo_de_riego

# Calculador de solucion optima con fuerza bruta
def roFB(n, tablones):
    programacion = [0, 1, 4, 2, 3]
    x = calculador_didtdr(programacion, tablones)
    print(x)
