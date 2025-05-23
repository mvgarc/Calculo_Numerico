class ReglaTrapecio:
    def __init__(self, funcion):
        """
        Inicializa la clase ReglaTrapecio con la función a integrar.

        Args:
            funcion: La función a integrar (debe aceptar un argumento numérico).
        """
        self.funcion = funcion
    
    def integrar(self, a, b, n):
        """
        Aproxima la integral definida de la función utilizando la Regla del Trapecio.

        Args:
            a: El límite inferior de integración.
            b: El límite superior de integración.
            n: El número de trapecios a utilizar.

        Returns:
            La aproximación de la integral definida.
        """
        h = (b - a) / n
        suma = self.funcion(a) + self.funcion(b)

        for i in range(1, n):
            suma += 2 * self.funcion(a + i * h)

        integral_aproximada = (h / 2) * suma
        return integral_aproximada
    
# Definimos la función a integrar fuera de la clase (podría ser un método de otra clase si fuera más complejo)
def funcion_a_integrar(x):
    """Función matemática que se va a integrar."""
    return x**2 + 1

# Creamos una instancia de la clase ReglaTrapecio, pasando la función a integrar
integrador = ReglaTrapecio(funcion_a_integrar)

# Definimos los parámetros de la integral
limite_inferior = 0
limite_superior = 2
numero_trapecios = 4

# Calculamos la aproximación utilizando el método 'integrar' del objeto
aproximacion = integrador.integrar(limite_inferior, limite_superior, numero_trapecios)

# Imprimimos el resultado
print(f"La aproximacion de la integral utilizando la Regla del Trapecio con {numero_trapecios} trapecios es: {aproximacion}")