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