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