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
    
    def print_polynomial(self):
        """Imprime la tabla de diferencias divididas y construye el polinomio en formato legible."""
        print("Tabla de diferencias divididas de Hermite:")
        for i in range(2 * self.n):
            print(f"{self.z[i]:.5f}", end="  ")
            for j in range(i + 1):
                print(f"{self.Q[i][j]:.5f}", end="  ")
            print()

        print("\nPolinomio interpolador de Hermite:")
        terms = []
        term_expr = "1"
        for i in range(2 * self.n):
            coef = self.Q[i][i]
            if coef != 0:
                if i > 0:
                    term_expr += f" * (x - {self.z[i - 1]})"
                terms.append(f"{coef:.5f} * {term_expr}")
        print("H(x) =", " + ".join(terms))

# Datos de prueba (los de la imagen)
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 6, 5, 5]
derivatives = [1, -1, 0, -2, 1]

hermite = HermiteInterpolation(x_values, y_values, derivatives)

# Imprimir puntos y polinomio
print("Puntos dados:")
for i in range(len(x_values)):
    print(f"x = {x_values[i]}, f(x) = {y_values[i]}, f'(x) = {derivatives[i]}")
print()
hermite.print_polynomial()

# Graficar la interpolación
x_plot = [i / 10.0 for i in range(10, 51)]  # Más puntos para mayor precisión
y_plot = [hermite.evaluate(x) for x in x_plot]

plt.figure(figsize=(8, 6))
plt.plot(x_plot, y_plot, label="Interpolación de Hermite", color="blue")
plt.scatter(x_values, y_values, color="red", label="Puntos dados")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Interpolación de Hermite")
plt.legend()
plt.grid(True)
plt.show()