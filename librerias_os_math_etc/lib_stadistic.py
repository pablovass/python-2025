import statistics as stats

# Datos de ejemplo
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Calcular la media
mean = stats.mean(data)
print(f"Media: {mean}")

# Calcular la mediana
median = stats.median(data)
print(f"Mediana: {median}")

# Calcular la moda (valor más frecuente)
try:
    mode = stats.mode(data)
    print(f"Moda: {mode}")
except stats.StatisticsError:
    print("No hay moda (todos los valores son únicos o hay más de una moda).")

# Calcular la varianza
variance = stats.variance(data)
print(f"Varianza: {variance}")

# Calcular la desviación estándar
std_dev = stats.stdev(data)
print(f"Desviación estándar: {std_dev}")

# Calcular el rango (diferencia entre el valor máximo y el mínimo)
range_value = max(data) - min(data)
print(f"Rango: {range_value}")
