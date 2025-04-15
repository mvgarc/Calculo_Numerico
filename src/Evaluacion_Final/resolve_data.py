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
temp_max = df['tmax'].max()
temp_min = df['tmin'].min()
temp_mean = df[''].mean()
temp_range = temp_max - temp_min

fecha_max = df[df['Temperature'] == temp_max]['fecha'].values[0]
fecha_min = df[df['Temperature'] == temp_min]['fecha'].values[0]

print(f"\nTemperatura media: {temp_mean:.2f}")
print(f"Temperatura máxima: {temp_max} el {fecha_max}")
print(f"Temperatura mínima: {temp_min} el {fecha_min}")
print(f"Rango de temperatura: {temp_range}")

# 3. Visualizaciones

# Gráfico de línea: Temperatura vs. Fecha
plt.figure(figsize=(10, 4))
plt.plot(df['fecha'], df['Temperature'], color='blue')
plt.title('Temperatura a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Boxplot de humedad relativa
plt.figure(figsize=(6, 4))
sns.boxplot(y=df['Rel Hum (%)'], color='skyblue')
plt.title('Distribución de la humedad relativa')
plt.ylabel('Humedad relativa (%)')
plt.tight_layout()
plt.show()

# Heatmap de correlación
plt.figure(figsize=(6, 5))
corr = df[['Temperature', 'Dew Point Temp', 'Rel Hum (%)']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de correlación')
plt.tight_layout()
plt.show()

# También puedes probar con un scatterplot
sns.pairplot(df[['Temperature', 'Dew Point Temp', 'Rel Hum (%)']])
plt.suptitle('Relación entre temperatura, punto de rocío y humedad', y=1.02)
plt.tight_layout()
plt.show()
