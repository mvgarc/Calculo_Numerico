import matplotlib.pyplot as plt

class LagrangeInterpolation:
    def __init__(self, puntos):
        """Inicializa la clase con los puntos dados."""
        self.puntos = puntos

    def lagrange_basis(self, x, i):
        """Calcula el i-ésimo polinomio base de Lagrange en el punto x."""
        xi, _ = self.puntos[i]
        numerador = 1
        denominador = 1

        for j, (xj, _) in enumerate(self.puntos):
            if i != j:
                numerador *= (x - xj)
                denominador *= (xi - xj)

        return numerador / denominador

    def interpolate(self, x):
        """Evalúa el polinomio interpolador en el punto x."""
        resultado = 0
        for i in range(len(self.puntos)):
            resultado += self.puntos[i][1] * self.lagrange_basis(x, i)
        return resultado

    def plot(self):
        """Grafica la interpolación junto con los puntos dados."""
        # Generamos puntos para la curva interpolada
        x_min = min(self.puntos, key=lambda p: p[0])[0]
        x_max = max(self.puntos, key=lambda p: p[0])[0]
        paso = 0.1  # Ajusta el paso para mayor o menor suavidad de la curva

        x_vals = []
        y_vals = []
        x_actual = x_min
        while x_actual <= x_max:
            x_vals.append(x_actual)
            y_vals.append(self.interpolate(x_actual))
            x_actual += paso  # Ojito: Incremento manual sin NumPy

        # Graficamos la interpolación
        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label="Interpolación de Lagrange", color="blue")
        plt.scatter(*zip(*self.puntos), color="red", label="Puntos dados", zorder=3)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Interpolación de Lagrange")
        plt.legend()
        plt.grid(True)
        plt.show()

# Ejemplo de uso:
puntos = [(1, 2), (3, 6), (5, 5), (7, 10), (9, 8)]
interpolador = LagrangeInterpolation(puntos)
interpolador.plot()
