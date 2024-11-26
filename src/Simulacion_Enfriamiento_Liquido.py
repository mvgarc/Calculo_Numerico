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