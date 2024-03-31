# Proyecto_ADA_II
# Calculando el plan de riego óptimo de una finca


## Integrantes
Grupo 9:
- Juan Sebastian Cifuentes Vallejo
- Hernan David Cisneros Vargas
- Jhon Alexander Valencia Hilamo
- Kevin Alejandro Velez Agudelo

## Profesores
- Juan Francisco Díaz Frias
- Jesús Alexander Aranda
- Monitor. Mauricio Muñoz

## Descripcion de archivos entregables

### Algoritmo_con_fuerza_bruta.py



### Algoritmo_Dinamico.py


### Algoritmo_voraz.py


### Lector.py

En este archivo se encuentra el script encargado de generar, al ejecutar la aplicacion por consola, la interfaz de usuario, permitiendo la eleccion y posterior ejecucion del algoritmo elegido, sobre una bateria de pruebas predefenidas en una serie de archivos .txt 

Los resultados de la ejecucion del algoritmo elegido por el usuario, representan la solución a cada una de las pruebas que se le entreguen. 
El script permite mostrar dichas soluciones en consola, pero ademas, usando la variable `soluciones_strse`, se generará un nuevo archivo `.txt` en donde se escribirán y se guardarán las soluciones de cada una de las pruebas, para el algoritmo que se haya elegido.
Se generará el correspondiente archivo de texto con soluciones cada vez que se ejecute la aplicación y se elija un algoritmo que no se haya elegido previamente.

Para llevar acabo todo lo anterior, `Lector.py` importa los módulos `glob` de la biblioteca estándar de Python, los cuales proporcionan una forma de buscar archivos y directorios que coincidan con un patrón especificado utilizando reglas de coincidencia de nombres similares a las utilizadas en la línea de comandos de Unix. 
Con esto, se crea la variable `archivos_txt`, que utiliza la función `glob.glob()`, para encontrar todos los archivos con extensión `.txt` en el directorio actual, devolviendo una lista de rutas de archivos o directorios que coinciden con ese patrón en el sistema de archivos.

De igual manera, se importan los modulos `Algoritmo_Fuerza_Bruta` `Algoritmo_Dinamico` y `Algoritmo_voraz`, correspondientes a los algoritmos implementados y a ser utilizados.

Se define una lista predefinida `archivos_txt_ordenados` que contiene los nombres de los archivos de texto en un orden específico. 

Luego, utilizando una estructura `if`, el usuario podrá elegir que algoritmo ejecutar, ingresando en consola un entero ( 1 para fuerza bruta, 2 para programación dinámica y 3 para programación voraz.). El entero ingresado se guardará en la variable `opcion`

Si el usuario elige la opción 1 (fuerza bruta), el script itera sobre cada archivo de la lista ordenada `archivos_txt_ordenados`.  abre cada archivo, Lee todas las líneas del archivo y las almacena en la lista lineas, Procesa cada línea del archivo (a partir de la segunda línea, ya que se omite la primera) para extraer los datos relacionados con la finca (ts, tr, y p). Estos valores se convierten en enteros y se agregan como una tupla a la lista finca. y luego llama a la función `roFB` del módulo `Algoritmo_Fuerza_Bruta` pasando la lista finca como argumento. luego, se construye una cadena `solucion_str` que contiene la información de la solución y se imprime en consola.
Por ultimo, se escribe todo el contenido de soluciones_str en `Soluciones_Fuerza_Bruta.txt`. Esto se realiza al finalizar el bucle, por lo que el archivo contendrá las soluciones de todos los archivos procesados.

Si el usuario elige la opción 2 (programación dinámica) o a opcion 3 (programación voraz), el script realiza un proceso similar al de la opción 1, pero utilizando el algoritmo de programación correspondiente (`roPD` = Algoritmo_Dinamico, `roV` = Algoritmo voraz). Las soluciones se escriben en los archivos de texto correspondientes `Soluciones_Programacion_Dinamica.txt`. y `Soluciones_Programacion_voraz.txt`.




### pruebas en formato .txt



## Instrucciones para la ejecución de la aplicación
1. Coloque los archivos de los algoritmos implementados (Algoritmo_con_fuerza_bruta.py, Algoritmo_Dinamico.py, Algoritmo_voraz.py), el archivo Lector.py y las pruebas en formato .txt (prueba1.txt a prueba30.txt) en una misma carpeta
2. Ejecute el archivo Lector.py desde la consola 

Nota: Es necesario tener instalado el interpretador de python para la ejecucion de la aplicación
