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

En este archivo se encuentra la implementación propuesta del algoritmo de fuerza bruta para resolver el problema de optimización de la programación de riego en una finca en cuestion. 

```python
def calculador_dtlpp(n):
    indices = [[i] for i in range(n)]
...
```
La funcion `calculador_dtlpp` se implementó para calcular todas las posibles programaciones de riego para una finca con `n` tablones. Utilizando un efoque de fuerza bruta se genera una lista de listas llamada `indices`, donde cada sublista contiene un solo índice.

Para ello, se utiliza la función auxiliar `identificador_de_elemento`, la cual incluye un bucle for, que verifica si un elemento está presente o no en una lista, y con la función recursiva `combinador_de_elementos` se combinan elementos de una lista parcial de manera que no se repitan los índices.

```python
def calculador_didtdr(programacion, finca):
    inicios_de_tiempos_de_riego = [0] * (len(programacion))
    turno = 0
...
```
La función `calculador_didtdr` esta implementada para calcular los tiempos de inicio de riego para cada tablón en una determinada programación de riego, eniendo en cuenta el tiempo de riego de los tablones anteriores.

para ello Se inicializa una lista `inicios_de_tiempos_de_riego` con una longitud igual a la cantidad de tablones en la `programación`. Esta lista contendrá los tiempos de inicio de riego calculados para cada tablón, que será el retorno de la función. Se itera sobre cada tablón en la programacion utilizando un bucle for, donde se calcula el tiempo de inicio de riego como el tiempo de inicio de riego del tablón anterior más el tiempo de riego del tablón anterior. 

Después de cada iteración, se incrementa el `turno` para pasar al siguiente tablón en la `programación`.

```python
def calculador_dctdr(inicios_de_tiempos_de_riego, finca):
    i = 0
    costo_total = 0
...
```
La función `calculador_dcdr` fue implementada para calcular el costo total de riego para una determinada programación de riego dados los tiempos de inicio de riego de los tablones y la información sobre la finca.

Para ello, y usando un bucle `for`, se itera sobre los tablones de la finca y se calcula el costo de riego para cada tablón, usando un condicional `if` que tiene en cuenta los tiempos de inicio de riego de cada uno.
Devuelve el costo total de riego para la programación dada.


```python
def roFB(finca):
    n = len(finca)
    programaciones_posibles = calculador_dtlpp(n)
```
`roFB` es la función principal, la cual esta encargada de encontrar la solución óptima utilizando la programacion con fuerza bruta. 

Para ello, primero calcula todas las posibles programaciones utilizando la función `calculador_dtlpp`.

luego, itera sobre todas las programaciones posibles y calcula el costo de riego para cada una utilizando las funciones `calculador_dcdr` y `calculador_didtdr`.

Dentro de la función `roFB`:

```python
programacion_optima = programaciones_posibles[0]
costo_optimo = calculador_dcdr(calculador_didtdr(programacion_optima, finca), finca)
```
Inicializa la primera programación como la óptima y calcula su costo.

```python
for programacion in programaciones_posibles:
    posible_costo_optimo = calculador_dcdr(calculador_didtdr(programacion, finca), finca)
    if (posible_costo_optimo < costo_optimo):
        programacion_optima = programacion
        costo_optimo = posible_costo_optimo
```
Luego, usando un bucle `for`, se itera sobre todas las posibles programaciones y se calcula el costo de cada una. Luego, utilizando una estrucutura condicional, si se encuentra una programación con un costo menor, se actualiza la programación óptima y el costo óptimo.

Por ultimo, la función retorna una tupla que contiene la programación óptima y su costo.


### Algoritmo_Dinamico.py

En este archivo se encuentra la implementación propuesta del algoritmo de programación dinamica para resolver el problema de optimización de la programación de riego en una finca en cuestion. 







### Algoritmo_voraz.py

En este archivo se encuentra la implementación propuesta del algoritmo de programación voraz para resolver el problema de optimización de la programación de riego en una finca en cuestion. 

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

Se entrega un conjunto de archivos de texto que representan una serie de pruebas con las que se van a ejecutar los algoritmos implementados una vez ejecutada la aplicación y elegido el algoritmo a utilizar. 

Estos archivos de prueba representan los argumentos de entrada para los algoritmos que se implementaron y con los cuales se generarán las soluciones a los diferentes de escenarios de prueba del problema de optimización de la programación de riego para una finca y que luego serán mostrados por consola y en archivos de texto por algoritmo.

Cada uno de los archivos de texto tendrán un formato de `n + 1` lıneas así:

```
n
ts0,tr0,p0
ts1,tr1,p1
.
.
.
ts(n-1),tr(n-1),p(n-1)
```

En donde, la primera linea representa el numero de tablones de la finca y las siguientes `n` lıneas corresponden a los `ts = tiempos de supervivencia`, `tr = tiempos de regado` y `p = prioridades` de cada uno de los `n` tablones, uno por linea.


## Instrucciones para la ejecución de la aplicación
1. Coloque los archivos de los algoritmos implementados (Algoritmo_con_fuerza_bruta.py, Algoritmo_Dinamico.py, Algoritmo_voraz.py), el archivo Lector.py y las pruebas en formato .txt (prueba1.txt a prueba30.txt) en una misma carpeta
2. Ejecute el archivo Lector.py desde la consola 

Nota 1: Es necesario tener instalado el interpretador de python para la ejecucion de la aplicación
Nota 2: Las soluciones se iran imprimiendo en la consola a medida que el script las genere
Nota 3: El archivo txt con todas las soluciones se generara al final de la ejecucion de todo el script
