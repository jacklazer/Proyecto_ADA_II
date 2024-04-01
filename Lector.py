import Algoritmo_Fuerza_Bruta
import Algoritmo_Dinamico





# archivos_txt_ordenados = ['PruebaX.txt']
archivos_txt_ordenados = ['Prueba1.txt', 'Prueba2.txt', 'Prueba3.txt', 'Prueba4.txt', 'Prueba5.txt', 'Prueba6.txt', 'Prueba7.txt', 'Prueba8.txt', 'Prueba9.txt', 'Prueba10.txt']
# archivos_txt_ordenados = ['Prueba1.txt', 'Prueba2.txt', 'Prueba3.txt', 'Prueba4.txt', 'Prueba5.txt', 'Prueba6.txt', 'Prueba7.txt', 'Prueba8.txt', 'Prueba9.txt', 'Prueba10.txt', 
#                            'Prueba11.txt', 'Prueba12.txt', 'Prueba13.txt', 'Prueba14.txt', 'Prueba15.txt', 'Prueba16.txt', 'Prueba17.txt', 'Prueba18.txt', 'Prueba19.txt', 'Prueba20.txt', 
#                            'Prueba21.txt', 'Prueba22.txt', 'Prueba23.txt', 'Prueba24.txt', 'Prueba25.txt', 'Prueba26.txt', 'Prueba27.txt', 'Prueba28.txt', 'Prueba29.txt', 'Prueba30.txt']





print("Digite\n1: Para usar fuerza bruta\n2: Para usar programacion dinamica\n3: Para usar programacion voraz")
opcion = int(input("-> "))

if (opcion == 1):
    soluciones_str = ""

    for nombre_archivo in archivos_txt_ordenados:
        solucion_str = ""

        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            finca = []
            for linea in lineas[1:]:
                ts, tr, p = map(int, linea.strip().split(','))
                finca.append((ts, tr, p))

            solucion = Algoritmo_Fuerza_Bruta.roFB(finca)

            solucion_str += "Solucion de " + nombre_archivo + ":\n"

            solucion_str += str(solucion[1]) + "\n"

            for tablon in solucion[0]:
                solucion_str += str(tablon) + "\n"

            print(solucion_str)
            soluciones_str += solucion_str + "\n"

    with open("Soluciones_Fuerza_Bruta.txt", "w") as archivo_:
        archivo_.write(soluciones_str)

elif (opcion == 2):
    soluciones_str = ""

    for nombre_archivo in archivos_txt_ordenados:
        solucion_str = ""
        
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            finca = []
            for linea in lineas[1:]:
                ts, tr, p = map(int, linea.strip().split(','))
                finca.append((ts, tr, p))

            solucion = Algoritmo_Dinamico.roPD(finca)

            solucion_str += "Solucion de " + nombre_archivo + ":\n"

            solucion_str += str(solucion[1]) + "\n"

            for tablon in solucion[0]:
                solucion_str += str(tablon) + "\n"

            print(solucion_str)
            soluciones_str += solucion_str + "\n"
                
    with open("Soluciones_Programacion_Dinamica.txt", "w") as archivo_:
        archivo_.write(soluciones_str)
else:
    print("xd")
    