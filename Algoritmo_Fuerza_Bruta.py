from itertools import permutations

# Calculador de todas las posibles programaciones
# O( n^(n+1) )
def calculador_dtlpp(n):
    # O(n)
    indices = [[i] for i in range(n)]

    # k = len(lista)
    # O(k)
    def identificador_de_elemento(elemento, lista):
        verdaderos_y_falsos = [(elemento == e) for e in lista]

        for booleano in verdaderos_y_falsos:
            if booleano:
                return True
        return False

    # k = contador | l = len(indices) | len(lista_parcial) = m
    # combinador_de_elementos realiza k llamados recursivos
    # Antes de cada llamado recursivo se ejecuta un bucle doble de complejidad O( l*m ) | Este bucle doble se ejecuta k veces si k>=1
    # En cada x-esima ejecucion del bucle doble m cambia
    # Si m = l en la primera ejecucion del bucle doble entonces el valor de m esta dado por la funcion M(x) = {l si x = 1; M(x-1)*(l-1) si x > 1} | Esto se puede demostrar
    # M(1) = l, M(2) = l*(l-1) = (l^2)-l, M(3) = ((l^2)-l)*(l-1) = (l^3)-(l^2)-(l^2)+l = (l^3)-(2*(l^2))+l, ..., M(x) = (l^x)+...+l | Esto se puede demostrar
    # No es dificil convencerse de que M(x) siempre es un polinomio de grado x
    # Por lo tanto la complejidad del bucle doble es de O( l*(l^x) ) = O( l^(x+1) ) para un x >= 1
    # Por lo tanto la complejidad de combinador_de_elementos es de O( (l^(k+1)) + (l^k) + ... + (l^3) + (l^2) ) = O( l^(k+1) ) si no se tiene en cuenta la complejidad de identificador_de_elemento
    # len(i) = p (variable)
    # En cada x-esima ejecucion del bucle doble p cambia e identificador_de_elemento se ejecuta M(x) veces
    # El valor de p esta dado por la funcion P(x) = x si x >= 1 | Esto se puede demostrar
    # Por lo tanto la complejidad de combinador_de_elementos es de O( (l^(k+1))*k + (l^k)*(k-1) + ... + (l^3)*2 + (l^2)*1 ) = O( (l^(k+1))*k ) si se tiene en cuenta la complejidad de identificador_de_elemento
    # Si contador = n-1, len(indices) = n, len(lista_parcial) = n entonces la complejidad de combinador_de_elementos es de O( (n^n)*(n-1) ) = O( (n^(n+1))-(n^n) ) = O( n^(n+1) )
    def combinador_de_elementos(lista_parcial, contador):
        if contador == 0:
            return lista_parcial
        else:
            nuevo_vector_parcial = [i + j for i in lista_parcial for j in indices if (identificador_de_elemento(j[0], i)==False)]
            return combinador_de_elementos(nuevo_vector_parcial, contador - 1)

    # O( n^(n+1) )
    xd = combinador_de_elementos(indices, n-1)

    return xd





# Calculador de inicio de tiempo de riego
# O(n) | n = len(programacion)
def calculador_didtdr(programacion, finca):
    inicios_de_tiempos_de_riego = [0] * (len(programacion))
    turno = 0

    # O(n) | n = len(programacion)
    for tablon in programacion:
        if (turno == 0):
            inicios_de_tiempos_de_riego[tablon] = 0
        else:
            inicios_de_tiempos_de_riego[tablon] = inicios_de_tiempos_de_riego[programacion[turno-1]]+finca[programacion[turno-1]][1]
        turno += 1

    return inicios_de_tiempos_de_riego





# Calculador de costo de riego
# O(n) | n = len(inicios_de_tiempos_de_riego)
def calculador_dcdr(inicios_de_tiempos_de_riego, finca):
    i = 0
    costo_total = 0

    # O(n) | n = len(finca)
    for tablon in finca:
        if (tablon[0]-tablon[1] >= inicios_de_tiempos_de_riego[i]):
            costo_total += tablon[0] - (inicios_de_tiempos_de_riego[i] + tablon[1])
        else:
            costo_total += tablon[2] * ((inicios_de_tiempos_de_riego[i] + tablon[1]) - tablon[0])
        i += 1

    return costo_total





# Calculador de solucion optima con fuerza bruta
# O( n^(n+1) + n + (n!*n) + 1 + n) = O( n^(n+1) )
def roFB(finca):
    n = len(finca)
    # O( n^(n+1) )
    programaciones_posibles = calculador_dtlpp(n)
    programacion_optima = programaciones_posibles[0]
    # O(2n) = O(n) | n = len(programacion_optima) = len(finca)
    costo_optimo = calculador_dcdr(calculador_didtdr(programacion_optima, finca), finca)

    # O(n!*n) | n! = len(programaciones_posibles)
    for programacion in programaciones_posibles:
        # O(2n) = O(n) | n = len(programacion) = calculador_didtdr(programacion, finca)
        posible_costo_optimo = calculador_dcdr(calculador_didtdr(programacion, finca), finca)

        # O(1)
        if (posible_costo_optimo < costo_optimo):
            programacion_optima = programacion
            costo_optimo = posible_costo_optimo
        
    # O(1)
    print(costo_optimo)

    # O(n) | n = len(programacion_optima)
    for tablon in programacion_optima:
        print(tablon)
