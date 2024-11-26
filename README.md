# Calculo_Numerico

# Ejercicios de Programación en Python: Ecuaciones Diferenciales Ordinarias (EDO) y Métodos Numéricos

Este repositorio contiene dos ejercicios resueltos en Python que utilizan métodos numéricos para resolver ecuaciones diferenciales ordinarias (EDO). Los métodos utilizados en ambos ejercicios son el **método de Taylor de segundo orden**, y los problemas que se abordan son el **enfriamiento de un líquido** y el **movimiento de un péndulo simple**.

## Ejercicio 1: Enfriamiento de un Líquido

### Enunciado:
El primer ejercicio aborda el problema de **enfriamiento de un café caliente** siguiendo la **Ley de Enfriamiento de Newton**. La ecuación diferencial que describe el cambio de temperatura del café es:

\[
\frac{dT}{dt} = -k(T - T_{\text{amb}})
\]

donde:
- \(T(t)\) es la temperatura del café en el tiempo \(t\),
- \(T_{\text{amb}}\) es la temperatura ambiente,
- \(k\) es la constante de proporcionalidad.

Se resuelve utilizando el **método de Taylor de segundo orden** para aproximar la solución, y se grafica la evolución de la temperatura del café en función del tiempo.

#### Parámetros:
- Temperatura inicial \(T_0 = 90 \, \text{°C}\),
- Temperatura ambiente \(T_{\text{amb}} = 25 \, \text{°C}\),
- Constante \(k = 0.1 \, \text{min}^{-1}\),
- Intervalo de tiempo: \(0 \leq t \leq 60 \, \text{min}\),
- Paso de tiempo \(h = 5 \, \text{min}\).

#### Objetivo:
- Resolver la ecuación diferencial usando el método de Taylor de segundo orden.
- Graficar la evolución de la temperatura \(T(t)\) a lo largo del tiempo y mostrar la temperatura ambiente.

---

## Ejercicio 2: Movimiento de un Péndulo Simple

### Enunciado:
El segundo ejercicio simula el movimiento de un **péndulo simple** bajo la influencia de la gravedad, modelado por la siguiente ecuación diferencial:

\[
\frac{d^2\theta}{dt^2} + \frac{g}{L} \sin(\theta) = 0
\]

donde:
- \(\theta(t)\) es el ángulo del péndulo respecto a la vertical,
- \(g = 9.8 \, \text{m/s}^2\) es la aceleración gravitacional,
- \(L\) es la longitud del péndulo.

Para este caso, se aproxima la ecuación utilizando el **método de Taylor de segundo orden** y se grafica la evolución del ángulo \(\theta(t)\) y la velocidad angular \(\omega(t)\) del péndulo.

#### Parámetros:
- Longitud del péndulo \(L = 2 \, \text{m}\),
- Ángulo inicial \(\theta_0 = 0.2 \, \text{rad}\),
- Velocidad angular inicial \(\omega_0 = 0 \, \text{rad/s}\),
- Intervalo de tiempo: \(0 \leq t \leq 10 \, \text{s}\),
- Paso de tiempo \(h = 0.1 \, \text{s}\).

#### Objetivo:
- Resolver la ecuación diferencial utilizando el método de Taylor de segundo orden.
- Graficar la evolución del ángulo \(\theta(t)\) y de la velocidad angular \(\omega(t)\) en función del tiempo.

---

## Requisitos

Para ejecutar estos ejercicios, asegúrate de tener instaladas las siguientes librerías de Python:

- `numpy`
- `matplotlib`

Puedes instalar estas librerías utilizando pip:
        pip install numpy matplotlib


