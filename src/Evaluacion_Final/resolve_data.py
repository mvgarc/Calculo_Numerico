import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar el dataset
url = "https://raw.githubusercontent.com/CAChemE/curso-python-datos/master/data/weather_data.csv"
df = pd.read_csv(url)

# Mostrar primeras filas
print(df.head())

# 2. Tratar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())
df = df.dropna()  # O puedes usar fillna según el caso

# 3. Convertir columna 'fecha' a datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# 4. Análisis de temperatura
temp_max = df['tmax'].max()
temp_min = df['tmin'].min()
temp_mean = df['tmed'].mean()
temp_range = temp_max - temp_min

fecha_max = df[df['tmax'] == temp_max]['fecha'].values[0]
fecha_min = df[df['tmin'] == temp_min]['fecha'].values[0]

print(f"\nTemperatura media: {temp_mean:.2f} °C")
print(f"Temperatura máxima: {temp_max} °C el {fecha_max}")
print(f"Temperatura mínima: {temp_min} °C el {fecha_min}")
print(f"Rango de temperatura: {temp_range:.2f} °C")

# 5. Visualizaciones

# a) Temperaturas a lo largo del tiempo
plt.figure(figsize=(10, 4))
plt.plot(df['fecha'], df['tmax'], label='Temperatura Máxima', color='tomato')
plt.plot(df['fecha'], df['tmin'], label='Temperatura Mínima', color='skyblue')
plt.title('Temperaturas a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# b) Boxplot de humedad relativa (columna no disponible, se puede usar 'tmed' como ejemplo)
plt.figure(figsize=(6, 4))
sns.boxplot(y=df['tmed'], color='lightgreen')
plt.title('Distribución de la temperatura media')
plt.ylabel('Temperatura media (°C)')
plt.tight_layout()
plt.show()

# c) Mapa de calor de correlaciones
plt.figure(figsize=(6, 5))
columnas_interes = ['tmax', 'tmin', 'tmed', 'prec', 'sol', 'velmedia']
corr = df[columnas_interes].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de correlación entre variables climáticas')
plt.tight_layout()
plt.show()

# d) Diagrama de dispersión (Pairplot)
sns.pairplot(df[columnas_interes])
plt.suptitle('Relación entre variables climáticas', y=1.02)
plt.tight_layout()
plt.show()
