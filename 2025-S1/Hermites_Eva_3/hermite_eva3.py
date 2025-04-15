import matplotlib.pyplot as plt

class HermiteInterpolation:
    def __init__(self, x_values, y_values, derivatives):
        self.x = x_values
        self.y = y_values
        self.dy = derivatives
        self.n = len(x_values)
        self.z = []
        self.Q = []
        self.compute_divided_differences()

    def compute_divided_differences(self):
        """Construye la tabla de diferencias divididas de Hermite."""
        self.z = [xi for xi in self.x for _ in (0, 1)]  # Duplicar valores de x
        self.Q = [[0] * (2 * self.n) for _ in range(2 * self.n)]

        for i in range(self.n):
            j = 2 * i
            self.Q[j][0] = self.y[i]  # f(x_i)
            self.Q[j + 1][0] = self.y[i]  # f(x_i) repetido
            self.Q[j + 1][1] = self.dy[i]  # f'(x_i)
            if i > 0:
                self.Q[j][1] = (self.Q[j][0] - self.Q[j - 1][0]) / (self.z[j] - self.z[j - 1])

        for i in range(2, 2 * self.n):
            for j in range(2, i + 1):
                self.Q[i][j] = (self.Q[i][j - 1] - self.Q[i - 1][j - 1]) / (self.z[i] - self.z[i - j])

    def evaluate(self, x_eval):
        """Evalúa el polinomio interpolador en x_eval usando la forma de Newton."""
        n = len(self.z)
        result = self.Q[0][0]
        term = 1.0

        for i in range(1, n):
            term *= (x_eval - self.z[i - 1])
            result += self.Q[i][i] * term

        return result