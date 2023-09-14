# Libreria de Operaciones de Vectores y Matrices Complejas
Este proyecto consiste en desarrollar un programa que permita realizar operaciones de vectores y matrices complejas, tales como:
* Adición de vectores complejos.
* Inverso (aditivo) de un vector complejos.
* Multiplicación de un escalar por un vector complejo.
* Adición de matrices complejas.
* Inversa (aditiva) de una matriz compleja.
* Multiplicación de un escalar por una matriz compleja.
* Transpuesta de una matriz/vector
* Conjugada de una matriz/vector
* Adjunta (daga) de una matriz/vector
* Producto de dos matrices (de tamaños compatibles)
* Función para calcular la "acción" de una matriz sobre un vector.
* Producto interno de dos vectores
* Norma de un vector
* Distancia entre dos vectores
* Valores  y vectores propios de una matriz
* Revisar si una matriz es unitaria
* Revisar si una matriz es Hermitiana
* Producto tensor de dos matrices/vectores

## ¿Cómo obtener una copia del repositorio?
### Pre-requisitos
Antes de comenzar con la ejecución de este proyecto, es necesario asegurarse de que se tiene instalado Python en su computador, debido a que este es el lenguaje de programación utilizado para desarrollar este proyecto. 
En caso de no tenerlo siga los siguientes pasos:
1. Dirigirse a la página https://www.python.org/downloads/
2. Dar click en la opción de descarga
   ![image](https://github.com/alexandrac1420/CNYT/assets/138069735/03d02dfb-a346-4bc8-8e9c-066816e2f80e)
3. Ejecutar el programa que se descarga automáticamente.

### Instalación 
Para instalar la librería debe tener en cuenta estos pasos:
1. Abra la carpeta en donde desea guardar la librería.
2. De click derecho y seleccione la opción "Git Bash"
3. Clone el repositorio utilizando el comando 'https://github.com/alexandrac1420/Libreria_Vectores_Matrices_Complejas.git'
4. Importe el modulo de la libreria en el programa que vaya a utilizar.
   
Completado el proceso anterior podrá trabajar con la librería proporcionada.

## Modo de uso
Para utilizar esta librería es necesario conocer la estructura de entrada de las operaciones disponibles junto con la sintaxis adecuada de cada una de las operaciones.

### Representación 
El programa reconoce de entrada de numero complejo una parte real y una imaginaria representadas en tuplas. Por ejemplo, si quiero realizar alguna operación con el numero 5 + 2i, este se ingresará al programa de la siguiente manera complex(5,2).

Para ingresar un vector se debe seguir la siguiente estructura __vector = [complex(numero1), complex(numero2)]__

Para ingresar una matriz se debe ingresar las filas en el formato de los vectores __matriz = [[complex(numero1), complex(numero2)], [complex(numero3), complex(numero4)]]__, siendo la primera fila  _[complex(numero1), complex(numero2)]_ y la segunda  _[complex(numero3), complex(numero4)]_

### Sintaxis operaciones 
A continuación se presenta la sintaxis correcta para el uso de las operaciones disponibles:
* __Adición de vectores complejos__:sum_vec_complex (_vector 1, vector 2_)
* __Inverso (aditivo) de un vector complejos__:inv_vec_complex (_vector_)
* __Multiplicación de un escalar por un vector complejo__:inv_vec_complex (_escalar, vector_)
* __Adición de matrices complejas__: sum_matrix(_matriz 1, matriz 2_)
* __Inversa (aditiva) de una matriz compleja__:inv_matrix(_matriz_)
* __Multiplicación de un escalar por una matriz compleja__: mult_esca_matrix(_escalar, matriz_)
* __Transpuesta de una matriz__: trans_matrix(_matriz_)
* __Conjugada de una matriz/vector__: conj_matrix(_matriz_)
* __Adjunta (daga) de una matriz__: adj_matrix(_matriz_)
* __Producto de dos matrices (de tamaños compatibles)__: mult_matrix(_matriz 1, matriz 2_)
* __Función para calcular la "acción" de una matriz sobre un vector__: act_matrix_vec(_matriz, vector_)

Tenga en cuenta que es necesario utilizar la representacion de los numeros mencionada anteriormente.

### Ejemplo de uso 
~~~python
import vec_matrix_complex as lb

# Ejemplo de operaciones con Vectores

# Ingrese los vectores que desea operar
v1 = [complex(2,5),complex(-8,-4)]
v2 = [complex(1,-2.5), complex(-3,1.2)]

#Realice la operación
suma = lb.sum_vec_complex(v1,v2)
print("La suma del vector {} y el vector {} es el vector {}".format(v1,v2,suma))

#Ejemplo de operaciones con Matrices


# Ingrese los vectores que desea operar
m1 = [[complex(2,5),complex(-8,-4)],[complex(1,-1), complex(3,4)]]
m2 = [[complex(1,-2.5), complex(-3,1.2)],[complex(3,7.8), complex(6,9.1)]]


#Realice la operación
suma = lb.sum_matrix(m1,m2)
print("La suma de la matriz {} y la matriz {} es la matriz{}".format(m1,m2,suma))

~~~


## Construido con
* Phyton 3.11.4
  
## Autor 
__Alexandra Cortes Tovar__ 
