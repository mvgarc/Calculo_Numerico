import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
T0 = 90  # Temperatura inicial del café (°C)
T_amb = 25  # Temperatura ambiente (°C)
k = 0.1  # Constante de proporcionalidad (min^-1)
h = 5  # Tamaño del paso (min)
t_max = 60  # Tiempo máximo (min)

def dT_dt(T):
    return -k * (T - T_amb)

def d2T_dt2(T):
    return -k * dT_dt(T)

def taylor_second_order(T0, T_amb, k, h, t_max):
    t_values = np.arange(0, t_max + h, h)
    T_values = [T0]

    for i in range(1, len(t_values)):
        T_prev = T_values[-1]
        T_next = (
            T_prev 
            + h * dT_dt(T_prev) 
            + (h**2 / 2) * d2T_dt2(T_prev)
        )
        T_values.append(T_next)
    
    return t_values, T_values

t_values, T_values = taylor_second_order(T0, T_amb, k, h, t_max)

plt.figure(figsize=(10, 6))
plt.plot(t_values, T_values, label="Temperatura del café (Taylor 2° Orden)", marker='o')
plt.axhline(y=T_amb, color='r', linestyle='--', label="Temperatura Ambiente (T_amb)")
plt.title("Enfriamiento del Café - Ley de Enfriamiento de Newton")
plt.xlabel("Tiempo (min)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid()
plt.show()