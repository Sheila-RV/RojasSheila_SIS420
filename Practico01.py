import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Semilla para la reproducibilidad de los resultados
np.random.seed(42)  
alturas = np.random.uniform(1.4, 2.0, 100)  # Generamos 100 estaturas aleatorias entre 1.4m y 2.0m
pesos = []  
# Bucle para generar pesos aleatorios controlados según la estatura
for altura in alturas:
    # Calculo del peso mínimo y máximo usando el IMC  
    peso_min = 18.5 * (altura**2)  
    peso_max = 29.9 * (altura**2)  
    # Generar un peso aleatorio entre el peso mínimo y máximo 
    peso = np.random.uniform(peso_min, peso_max)
    pesos.append(peso) 
data = pd.DataFrame({
    'Estatura (m)': alturas,
    'Peso (kg)': pesos
})
# Calcular la pendiente (m) y la intersección (b) de la recta y = mx + b
x = data['Estatura (m)']
y = data['Peso (kg)']
m = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2)
b = np.mean(y) - m * np.mean(x)

# Crear los valores de y basados en la fórmula de la recta
y_linea = m * x + b

# Gráfico de los datos generados y la recta ajustada
plt.scatter(data['Estatura (m)'], data['Peso (kg)'], color='green', label='Datos')
plt.plot(x, y_linea, color='blue', label='Línea ajustada')
plt.title('Estatura vs Peso con Línea Ajustada')
plt.xlabel('Estatura (m)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.show()



