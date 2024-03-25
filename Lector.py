import glob
import Algoritmo_con_fuerza_bruta

# Obtener la lista de archivos txt en el directorio actual
archivos_txt = glob.glob('*.txt')

# Ordenar la lista de archivos
archivos_txt_ordenados = ['Prueba1.txt', 'Prueba2.txt', 'Prueba3.txt', 'Prueba4.txt', 'Prueba5.txt', 'Prueba6.txt', 'Prueba7.txt', 'Prueba8.txt', 'Prueba9.txt', 'Prueba10.txt', 
                           'Prueba11.txt', 'Prueba12.txt', 'Prueba13.txt', 'Prueba14.txt', 'Prueba15.txt', 'Prueba16.txt', 'Prueba17.txt', 'Prueba18.txt', 'Prueba19.txt', 'Prueba20.txt', 
                           'Prueba21.txt', 'Prueba22.txt', 'Prueba23.txt']#, 'Prueba24.txt', 'Prueba25.txt', 'Prueba26.txt', 'Prueba27.txt', 'Prueba28.txt', 'Prueba29.txt', 'Prueba30.txt'] # [sorted(archivos_txt)]

a = 0
b = []

print("Digite\n1: Para usar fuerza bruta\n2: Para usar programacion dinamica\n3: Para usar programacion voraz")
opcion = input("-> ")

if (opcion == 1):
    for nombre_archivo in archivos_txt_ordenados:
        with open(nombre_archivo, 'r') as archivo:
            print(f"\nSolucion de {nombre_archivo}:")
            for linea in archivo:
                elementos = linea.strip().split(',')  # Divide la línea en elementos separados por comas
                # a.append(int(elementos[0]))  # Guarda el primer elemento como entero
                if len(elementos) > 1:  # Verifica si hay más elementos en la línea
                    b.append([int(e) for e in elementos[0:]])
                else:
                    a = int(elementos[0])
            Algoritmo_con_fuerza_bruta.roFB(a, b)
            # Reinicia las listas para la próxima iteración
            a = 0
            b = []
elif (opcion == 2):
    for nombre_archivo in archivos_txt_ordenados:
        with open(nombre_archivo, 'r') as archivo:
            print(f"\nSolucion de {nombre_archivo}:")
            for linea in archivo:
                elementos = linea.strip().split(',')  # Divide la línea en elementos separados por comas
                # a.append(int(elementos[0]))  # Guarda el primer elemento como entero
                if len(elementos) > 1:  # Verifica si hay más elementos en la línea
                    b.append([int(e) for e in elementos[0:]])
                else:
                    a = int(elementos[0])
            Algoritmo_con_fuerza_bruta.roFB(a, b)
            # Reinicia las listas para la próxima iteración
            a = 0
            b = []
else:
    for nombre_archivo in archivos_txt_ordenados:
        with open(nombre_archivo, 'r') as archivo:
            print(f"\nSolucion de {nombre_archivo}:")
            for linea in archivo:
                elementos = linea.strip().split(',')  # Divide la línea en elementos separados por comas
                # a.append(int(elementos[0]))  # Guarda el primer elemento como entero
                if len(elementos) > 1:  # Verifica si hay más elementos en la línea
                    b.append([int(e) for e in elementos[0:]])
                else:
                    a = int(elementos[0])
            Algoritmo_con_fuerza_bruta.roFB(a, b)
            # Reinicia las listas para la próxima iteración
            a = 0
            b = []