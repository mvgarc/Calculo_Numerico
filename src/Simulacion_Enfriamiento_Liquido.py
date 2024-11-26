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