import Algoritmo_Fuerza_Bruta
import Algoritmo_Dinamico
import Algoritmo_Voraz





# archivos_txt_ordenados = ['PruebaX.txt']
# archivos_txt_ordenados = ['Prueba_Ejemplo1.txt', 'Prueba_Ejemplo2.txt', 'Prueba_Ejemplo3.txt', 'Prueba_Ejemplo4.txt', 'Prueba_Ejemplo5.txt']
archivos_txt_ordenados = ['Prueba1.txt', 'Prueba2.txt', 'Prueba3.txt', 'Prueba4.txt', 'Prueba5.txt', 'Prueba6.txt', 'Prueba7.txt', 'Prueba8.txt', 'Prueba9.txt', 'Prueba10.txt', 
                           'Prueba11.txt', 'Prueba12.txt', 'Prueba13.txt', 'Prueba14.txt', 'Prueba15.txt', 'Prueba16.txt', 'Prueba17.txt', 'Prueba18.txt', 'Prueba19.txt', 'Prueba20.txt', 
                           'Prueba21.txt', 'Prueba22.txt', 'Prueba23.txt', 'Prueba24.txt', 'Prueba25.txt', 'Prueba26.txt', 'Prueba27.txt', 'Prueba28.txt', 'Prueba29.txt', 'Prueba30.txt']





print("Digite\n1: Para usar fuerza bruta\n2: Para usar programacion dinamica\n3: Para usar programacion voraz")
opcion = int(input("-> "))

print("Digite\n1: Para ejecutar varias pruebas \n2: Para ejecutar solo una prueba")
opcion2 = int(input("-> "))

if (opcion == 1):

    if (opcion2 == 1):

        print("Digite el numero de pruebas que requiere ejecutar (se empezaran a ejecutar las de menor numero de tablones):")
        opcion3 = int(input("-> "))

        soluciones_str = ""

        for nombre_archivo in archivos_txt_ordenados[:opcion3]:
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

    else:
        print("Digite el numero de la prueba que requiere ejecutar:")
        opcion3 = str(input("-> "))

        nombre_archivo = "Prueba"+opcion3+".txt"
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

        with open("Solucion_Fuerza_Bruta_"+nombre_archivo, "w") as archivo_:
            archivo_.write(solucion_str)


elif (opcion == 2):

    if (opcion2 == 1):

        print("Digite el numero de pruebas que requiere ejecutar (se empezaran a ejecutar las de menor numero de tablones):")
        opcion3 = int(input("-> "))
        
        soluciones_str = ""

        for nombre_archivo in archivos_txt_ordenados[:opcion3]:
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
        print("Digite el numero de la prueba que requiere ejecutar:")
        opcion3 = str(input("-> "))

        nombre_archivo = "Prueba"+opcion3+".txt"
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

        with open("Solucion_Programacion_Dinamica_"+nombre_archivo, "w") as archivo_:
            archivo_.write(solucion_str)


else:

    if (opcion2 == 1):

        print("Digite el numero de pruebas que requiere ejecutar (se empezaran a ejecutar las de menor numero de tablones):")
        opcion3 = int(input("-> "))
        
        soluciones_str = ""

        for nombre_archivo in archivos_txt_ordenados[:opcion3]:
            solucion_str = ""

            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                finca = []
                for linea in lineas[1:]:
                    ts, tr, p = map(int, linea.strip().split(','))
                    finca.append((ts, tr, p))

                solucion = Algoritmo_Voraz.roV(finca)

                solucion_str += "Solucion de " + nombre_archivo + ":\n"

                solucion_str += str(solucion[1]) + "\n"

                for tablon in solucion[0]:
                    solucion_str += str(tablon) + "\n"

                print(solucion_str)
                soluciones_str += solucion_str + "\n"

        with open("Soluciones_Programacion_Voraz.txt", "w") as archivo_:
            archivo_.write(soluciones_str)

    else:
        print("Digite el numero de la prueba que requiere ejecutar:")
        opcion3 = str(input("-> "))

        nombre_archivo = "Prueba"+opcion3+".txt"
        solucion_str = ""

        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            finca = []
            for linea in lineas[1:]:
                ts, tr, p = map(int, linea.strip().split(','))
                finca.append((ts, tr, p))

            solucion = Algoritmo_Voraz.roV(finca)

            solucion_str += "Solucion de " + nombre_archivo + ":\n"

            solucion_str += str(solucion[1]) + "\n"

            for tablon in solucion[0]:
                solucion_str += str(tablon) + "\n"

            print(solucion_str)

        with open("Solucion_Programacion_Voraz_"+nombre_archivo, "w") as archivo_:
            archivo_.write(solucion_str)

    