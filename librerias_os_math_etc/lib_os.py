import os

# Definir el nombre del directorio y del archivo
directory_name = "example_directory"
file_name = "example_file.txt"

# Crear un directorio si no existe
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    print(f"Directorio '{directory_name}' creado.")
else:
    print(f"Directorio '{directory_name}' ya existe.")

# Ruta completa del archivo
file_path = os.path.join(directory_name, file_name)

# Escribir contenido en el archivo
with open(file_path, mode="w", encoding="utf-8") as file:
    file.write("Este es un ejemplo de uso del módulo 'os' en Python.\n")
    file.write("¡Trabajar con archivos y directorios es fácil!")

print(f"Archivo '{file_name}' creado dentro de '{directory_name}'.")

# Leer el contenido del archivo
with open(file_path, mode="r", encoding="utf-8") as file:
    content = file.read()

print("\nContenido del archivo:")
print(content)

# Listar los archivos dentro del directorio
print("\nArchivos en el directorio:")
for item in os.listdir(directory_name):
    print(item)
