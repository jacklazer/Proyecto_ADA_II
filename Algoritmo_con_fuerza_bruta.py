from itertools import permutations

# Calculador de todas las posibles programaciones
def calculador_dtlpp(n):
    numbers = list(range(n))  # Generar lista de números del 0 al n-1
    permutations_list = list(permutations(numbers))  # Generar todas las permutaciones posibles
    return [list(perm) for perm in permutations_list]  # Convertir las tuplas de permutaciones en listas


# Calculador de dolucion optima con fuerza bruta
def roFB(n, Ts):
    print(calculador_dtlpp(n))
