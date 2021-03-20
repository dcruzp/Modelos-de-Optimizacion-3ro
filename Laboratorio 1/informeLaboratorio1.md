# Laboratorio 1: Modelos continuos y su solución Numérica

Utilizando librerías implementadas en el lenguaje de programación de su preferencia para la resolución de problemas matemáticos y científicos,por ejemplo(python-scipy,matlab,Julia)resuelva los modelos de optimización descritos a continuación:


## Ejercicio 1. *Problemas de CP*


#### Respuesta  Ejercicio 1 de CP 1

##### Varibale de descisión:

- $x_i$ : Cantidad de ha dedicadas al cultivo $i \in \{Tomates, Lechugas, Acelgas\}_3$.

##### P\'arametros:

- $b_i$ : Cantidad de $ha$ para la que rinde una ton de semillas del cultivo $i$.

- $c_i$ : Precio de una $ton$ del cultivo $i$.

- $d_i$ : Cantidad de hombres-d\'ias necesarios para una $ha$ del cultivo $i$.

- $e_i$ : Cantidad de $ton$ del rendimiento promedio del una $ha$ del cutlivo $i$.

##### Modelo:
$$ max \sum_{i = 1}^3 (c_i e_i x_i - c_i \frac {x_i}{b_i} - 5 d_i x_i )$$

$$ \sum_{i=1}^3 x_i \leq 1200$$

$$ \sum_{i=1}^3 d_i x_i \leq 450$$

$$ x_i \geq 0\ \forall i = 1, 2, 3$$

##### Código

@import "Ejercicio1\Ej1CP1.py"  {class="line-numbers" }


#### Respuesta  Ejercicio 2 de CP 1

##### Varibale de decisión:
- $x_{ij}$ : Cantidad de $ton$ del articulos $i \in \{A, B, C\}_3$ en la bodega $j \in \{Proa,\ Popa,\ Centro\}_3$.

##### Parámetros:
- $c_i$ : Ganancia de una *ton* del artículo $i$.
-  $b_j$ : Capacidad de la bodega $j$.
-  $d_i$ : Cantidad de *ton* disponible del artículo $i$.


##### Modelo:
$$ max \sum_{i = 1}^3 \sum_{j = 1}^3 c_j x_{ij} $$

$$ \sum_{i=1}^3 x_{ij} \leq b_j\ \forall j = 1, 2, 3$$

$$ \sum_{j=1}^3 x_{ij} \leq d_i\ \forall i = 1, 2, 3$$

$$ \frac{\sum_{i=1}^3 x_{is}} {b_s} - \frac {\sum_{i=1}^3 x_{it}} {b_t} = 0\ \forall s,t \in \{Proa, Popa, Centro\}_3 \land s \not= t $$

$$ x_{ij} \geq 0\ \forall i = 1, 2, 3 \land j = 1, 2, 3$$

##### Código

@import "Ejercicio1\Ej2CP1.py"  {class="line-numbers" }

#### Respuesta  Ejercicio 3 de CP 1 


##### Varibale de decisión:

- $x_{ij}$ : Cantidad de $hl$ de la mezcla $j \in \{Mezcla\ I,\ Mezcla\ II, Aceite,\ Secador,\ Solvente\}_5$ en el producto $i \in \{Producto\ I,\ Producto\ II\}_2$.


##### Parámetros:

- $c_j$ : Costo de la mezcla $j$.
- $a_{jk}$ : Composición en \% de la sustancia $k \in \{Aceite,Secador,\ Solvente\}_3$. en la materia prima $j$
- $b_{ik}$ : Composición requerida de la sustancia $k$ en el producto $i$.
- $d_j$ : Cantidad de $hl$ disponible para la mezcla $j$.
- $D_i$ : Demanda de $hl$ del producto $i$.


##### Modelo:
$$ min \{ \sum_{i = 1}^2 \sum_{j = 1}^5 c_j x_{ij} -  \sum_{j=1}^5 c_j d_j\}$$

$$ \sum_{j=1}^5 x_{ij} a_{jk} = \sum_{j=1}^5 x_{ij} b_{jk}\ \forall i=1, 2 \land k = 1, 2, 3 $$

$$ \sum_{i=1}^2 x_{ij} \leq d_j\ \forall j = 1, 2, ..., 5$$

$$ \sum_{j = 1}^5 x_{ij} = D_i\  \forall i=1, 2$$

$$ x_{ij} \geq 0\ \forall i = 1,2 \land j = 1, 2, ..., 5$$

##### Código 

@import "Ejercicio1\Ej3CP1.py" {class="line-numbers" }


## Ejercicio 2. Función de Rosenbrock (caso irrestricto)

Sea la función en $n$ variables:

$$min \sum_{i=1} 100 \left(x_{i-1}- x_{i}^{2} \right)^{2} + \left(1-x_{i}\right)^{2}$$

Encontrar su valor mínimo para  $n =2,3,4,5$  

##### Código

@import "Ejercicio2\FunciondeRosenbrock(caso_irrestricto).py" {class="line-numbers" }


## Ejercicio 3. Función de Rosenbrock (con restricciones)


##### Modelo:
$$min \hspace{0.2cm} 100(x_{i+1} - x_i^2)^2 + (1 - x_i)^2$$

$$ x_{0} + 2x_{1} \leq 1 $$

$$ x_{0}^{2} + x_{1} \leq 1 $$

$$ x_{0} - x_{1} \leq 4 $$

##### Código 

@import "Ejercicio3\FunciondeRosenbrock(con_restricciones).py" {class="line-numbers" }