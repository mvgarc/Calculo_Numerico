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

# 2. Analisis de temperatura
temp_max = df['Temperature'].max()
temp_min = df['Temperature'].min()
temp_mean = df['Temperature'].mean()
temp_range = temp_max - temp_min

fecha_max = df[df['Temperature'] == temp_max]['fecha'].values[0]
fecha_min = df[df['Temperature'] == temp_min]['fecha'].values[0]

print(f"\nTemperatura media: {temp_mean:.2f}")
print(f"Temperatura máxima: {temp_max} el {fecha_max}")
print(f"Temperatura mínima: {temp_min} el {fecha_min}")
print(f"Rango de temperatura: {temp_range}")