import numpy as np
import matplotlib.pyplot as plt

g = 9.8  # Aceleración gravitacional (m/s^2)
L = 2.0  # Longitud del péndulo (m)
theta0 = 0.2  # Ángulo inicial (rad)
omega0 = 0.0  # Velocidad angular inicial (rad/s)
h = 0.1  # Tamaño del paso (s)
t_max = 10.0  # Tiempo máximo (s)

def dtheta_dt(omega):
    return omega

def domega_dt(theta):
    return -(g / L) * theta

def d2theta_dt2(theta):
    return -(g / L) * dtheta_dt(theta)

def taylor_second_order_pendulum(theta0, omega0, h, t_max):
    t_values = np.arange(0, t_max + h, h)
    theta_values = [theta0]
    omega_values = [omega0]

    for i in range(1, len(t_values)):
        theta_prev = theta_values[-1]
        omega_prev = omega_values[-1]

        # Calcular siguiente valor de theta y omega
        theta_next = (
            theta_prev 
            + h * dtheta_dt(omega_prev) 
            + (h**2 / 2) * domega_dt(theta_prev)
        )
        omega_next = (
            omega_prev 
            + h * domega_dt(theta_prev) 
            + (h**2 / 2) * d2theta_dt2(theta_prev)
        )

        theta_values.append(theta_next)
        omega_values.append(omega_next)
    
    return t_values, theta_values, omega_values

t_values, theta_values, omega_values = taylor_second_order_pendulum(theta0, omega0, h, t_max)