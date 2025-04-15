import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 0. Cargar el dataset
url = "https://raw.githubusercontent.com/CAChemE/curso-python-datos/master/data/weather_data.csv"
df = pd.read_csv(url)

# Mostrar primeras filas
print(df.head())

# 1. Tratar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())
df = df.dropna()  # Se eliminan filas con valores nulos (puedes cambiar por fillna si prefieres)

# Convertir columna de fecha a tipo datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')