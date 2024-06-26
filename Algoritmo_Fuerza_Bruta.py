




# Calculador de todas las posibles programaciones
# O( n^(n+1) + n ) = O( n^(n+1) ) | n=n
def calculador_dtlpp(n):
    # O(n)
    indices = [[i] for i in range(n)]

    # k = len(lista)
    # O(k)
    def identificador_de_elemento(elemento, lista):
        for e in lista:
            if (e == elemento):
                return True
        return False

    # k = contador | l = len(indices) | len(lista_parcial) = m
    # combinador_de_elementos realiza k llamados recursivos | Esto se puede demostrar
    # Antes de cada llamado recursivo se ejecuta un bucle doble (que llamaremos linea Z) de complejidad O( l*m ) | La linea Z se ejecuta k veces si k>=1
    # En cada x-esima ejecucion de la linea Z, m cambia
    # Si m = p en la primera ejecucion de la linea Z, entonces el valor de m esta dado por la funcion M(x) = {p si x = 1; (M(x-1)*l)-(M(x-1)*(x-1)) si x > 1} = {p si x = 1; M(x-1)*(l+1-x) si x > 1} | Esto se puede demostrar
    # Si m = l en la primera ejecucion de la linea Z, entonces el valor de m esta dado por la funcion M(x) = {l si x = 1; M(x-1)*(l+1-x) si x > 1}
    # M(1) = l
    # M(2) = l*(l+1-2) = (l^2)-l
    # M(3) = ((l^2)-l)*(l+1-3) = ((l^2)-l)*(l-2) = (l^3)-(l^2)-(2*(l^2))+(2*l) = (l^3)-(3*(l^2))+(2*l)
    # M(4) = ((l^3)-(3*(l^2))+(2*l))*(l+1-4) = ((l^3)-(3*(l^2))+(2*l))*(l-3) = (l^4)-(3*(l^3))+(2*(l^2))-(3*(l^3))+(9*(l^2))-(6*l) = (l^4)-(6*(l^3))+(11*(l^2))-(6*l)
    # ...
    # M(x) = ((l^(x-1))+...+(a*l))*(l+1-x) = (l^x)+...+(a*(l^2)) + ((l^(x-1))+...+(a*l)) - (((l^(x-1))+...+(a*l))*x)  | Esto se puede demostrar
    # No es dificil convencerse de que M(x) siempre es un polinomio de grado x si  1 =< x < l
    # Por lo tanto la complejidad de la linea Z es de O( l*(l^x) ) = O( l^(x+1) ) para un 1 =< x < l
    # Por lo tanto la complejidad de combinador_de_elementos es de O( (l^(k+1)) + (l^k) + ... + (l^3) + (l^2) ) = O( l^(k+1) ) si no se tiene en cuenta la complejidad de identificador_de_elemento
    # len(i) = q (variable)
    # El valor de q esta dado por la funcion Q(x) = x si x >= 1 | Esto se puede demostrar
    # En cada x-esima ejecucion de la linea z, q cambia e identificador_de_elemento se ejecuta Q(x) veces | identificador_de_elemento es de complejidad O(x)
    # Por lo tanto la complejidad de combinador_de_elementos es de O( (l^(k+1))*k + (l^k)*(k-1) + ... + (l^3)*2 + (l^2)*1 ) = O( (l^(k+1))*k ) si se tiene en cuenta la complejidad de identificador_de_elemento
    # Si contador = k = n-1, len(indices) = l = n, len(lista_parcial) = m = n entonces la complejidad de combinador_de_elementos es de O( (n^n)*(n-1) ) = O( (n^(n+1))-(n^n) ) = O( n^(n+1) )
    def combinador_de_elementos(lista_parcial, contador):
        if contador == 0:
            return lista_parcial
        else:
            nueva_lista_parcial = [i + j for i in lista_parcial for j in indices if (identificador_de_elemento(j[0], i)==False)] # Linea Z
            return combinador_de_elementos(nueva_lista_parcial, contador - 1)

    # O( n^(n+1) )
    programaciones_posibles = combinador_de_elementos(indices, n-1)

    return programaciones_posibles





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





# Calculador de costo total de riego
# O(n) | n = len(finca)
def calculador_dctdr(inicios_de_tiempos_de_riego, finca):
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





# Respuesta obtenida Fuerza Bruta
# O( n^(n+1) + n + (n+1!) ) = O( n^(n+1) ) | len(finca)
def roFB(finca):
    n = len(finca)
    # O( n^(n+1) )
    programaciones_posibles = calculador_dtlpp(n)
    programacion_optima = programaciones_posibles[0]
    # O(2n) = O(n) | n = len(programacion_optima) = len(finca)
    costo_optimo = calculador_dctdr(calculador_didtdr(programacion_optima, finca), finca)

    # O( n!*(n+1) ) = O( (n+1)! ) | n! = len(programaciones_posibles)
    for programacion in programaciones_posibles:
        # O(2n) = O(n) | n = len(programacion) = len(finca)
        posible_costo_optimo = calculador_dctdr(calculador_didtdr(programacion, finca), finca)

        # O(1)
        if (posible_costo_optimo < costo_optimo):
            programacion_optima = programacion
            costo_optimo = posible_costo_optimo

    return (programacion_optima, costo_optimo)
