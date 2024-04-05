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

Para ello, se implementó las siguientes 4 funciones:

```python
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        n = int(lineas[0].strip())
        tablones = []
        for linea in lineas[1:]:
            ts, tr, p = map(int, linea.strip().split(','))
            tablones.append((ts, tr, p))
        return n, tablones
```

La función `leer_archivo()` tiene la tarea de leer los datos de entrada desde un archivo y devolver el numero `n` de tablones, que se encuentra en la primer linea del archivo de texto, y una lista de tuplas `tablones` correspondientes a los tablones con su respectivo tiempo de supervivencia, tiempo de riego y prioridad.

```python

def cost(state, tablones, dp):
    if not state:
        return 0, []

    if state in dp:
        return dp[state]
...
```

La función `cost()` se trata de una función recursiva que calcula el costo mínimo y la programación óptima de riego para un estado dado.
para ello, toma una tupla de índices de tablones `state`, una lista de tuplas que representan los tablones `tablones`, y un diccionario para almacenar los resultados ya calculados `dp` como argumentos, utilizando la tecnica de memoization y evitando los recalculos.
En cada iteración se elimina un tablón y se calcula el costo de regar el tablón actual en función de los tablones ya regados, actualizando el costo mínimo y la programación óptima si se encuentra una solución mejor.

```python
def solucion_optima(nombre_archivo):
    n, tablones = leer_archivo(nombre_archivo)
    initial_state = tuple(range(n))
    dp = {}
    min_cost, optimal_order = cost(initial_state, tablones, dp)
    return min_cost, optimal_order
```

`solucion_optima()` es la función principal y que se encarga de resolver el problema de optimización del riego de los tablones, utilizando funciones implementadas.
La función utiliza `leer_archivo()` para obtener el número de tablones y la información de los tablones desde el archivo especificado, luego inicializa el estado inicial como una tupla que contiene todos los índices de tablones y por ultimo utiliza `cost` para calcular el costo mínimo y la programación óptima de riego, retornando el costo mínimo y la programación óptima.

```python
def roPD(finca):
    n = len(finca)
    initial_state = tuple(range(n))
    dp = {}
    min_cost, optimal_order = cost(initial_state, finca, dp)

    return (optimal_order, min_cost)
```

La función `roPD `toma una lista de tablones `finca` como entrada y se encarga de devolver la programación óptima de riego y su costo asociado. para ello inicializa el estado inicial  `initial_state` y el diccionario `dp` y calcula la programación óptima de riego utilizando la función `cost`.



### Algoritmo_voraz.py

En Algoritmo_Voraz.py se encuentra implementado la propuesta de algoritmo con enfoque voraz que como grupo desarrollamos para dar solución al problema de riego óptimo. 
En nuestra propuesta de algoritmo voraz, hicimos uso del algoritmo de fuerza bruta que ya se había implementado con anterioridad, para acceder a algunas funciones que son necesarias para el cálculo del costo total de riego en el algoritmo voraz.

```python
def calculador_dcdur(tablon, tiempo_total_de_regado):
    costo = tablon[2] * (tiempo_total_de_regado - tablon[0])
    return costo
```
La función `calculador_dcdur` calcula el costo de riego de un `tablon` en función del tiempo total de riego en la finca, esto lo realiza con un cálculo simple basado en operaciones aritméticas y no depende del tamaño de la entrada, obteniendo una complejidad constante.

```python
def verificador_dpmg(a, b, finca):
    if (finca[a][2] >= finca[b][2]):
        return a
    elif (finca[b][2] > finca[a][2]):
        return b
```

La función `verificador_dpmg` verifica cuál, entre dos `tablones`, tiene una prioridad más alta, basándose en sus prioridades, esto lo hace realizando una comparación simple, obteniendo una complejidad constante.

```python
def calculador_dpo(costos_de_ultimo_riego, programacion_optima, finca, n):
    
    tablon_actual = 0
    costo_mas_costoso = 0
    tablon_mas_costoso = -1

    
    for costo_de_ultimo_riego in costos_de_ultimo_riego:
        if not(tablon_actual in programacion_optima):
            if (costo_de_ultimo_riego > costo_mas_costoso):
                costo_mas_costoso = costo_de_ultimo_riego
                tablon_mas_costoso = tablon_actual
            elif (costo_de_ultimo_riego == costo_mas_costoso):
                tablon_mas_costoso = verificador_dpmg(tablon_actual, tablon_mas_costoso, finca)
                costo_mas_costoso = costos_de_ultimo_riego[tablon_mas_costoso]
        tablon_actual += 1
    programacion_optima.append(tablon_mas_costoso)

   
    if (len(programacion_optima) == n):
        return programacion_optima
    else:
        return calculador_dpo(costos_de_ultimo_riego, programacion_optima, finca, n)
```
La función `calculador_dpo` calcula la programación óptima de riego utilizando el enfoque voraz. Su complejidad dominante está en el bucle que recorre la lista de costos de último riego, que tiene una complejidad lineal `O(n)`, donde `n` es la cantidad de `tablones` en la finca. El resto de sus componentes tienen una complejidad menos dominante, por lo tanto no se tienen en cuenta.

```python
def roV(finca):
    n = len(finca)
    tiempo_total_de_regado = 0
    costos_de_ultimo_riego = []

    for tablon in finca:
        tiempo_total_de_regado += tablon[1]

    for tablon in finca:
        costos_de_ultimo_riego.append(calculador_dcdur(tablon, tiempo_total_de_regado))

    programacion_optima_ = []

    programacion_optima = calculador_dpo(costos_de_ultimo_riego, programacion_optima_, finca, n)

    return (programacion_optima, Algoritmo_Fuerza_Bruta.calculador_dctdr(Algoritmo_Fuerza_Bruta.calculador_didtdr(programacion_optima, finca), finca))
```

La función principal es `roV`, la cual ejecuta el algoritmo voraz para resolver el problema. 
Esta función llama a las otras funciones ya mencionadas en el mismo módulo, dominando la complejidad de la función `calculador_dpo →  O(n) `

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

Nota 1: Es necesario tener instalado el interpretador de python para la ejecucion de la aplicación.
Nota 2: Las soluciones se iran imprimiendo en la consola a medida que el script las genere.
Nota 3: El archivo txt con todas las soluciones se generara al final de la ejecucion de todo el script.
Nota 4: Los archivos .txt que seran retornados con las respuestas seran:
-Soluciones_Fuerza_Bruta.txt
-Soluciones_Programacion_Dinamica.txt
-Soluciones_Programacion_Voraz.txt
