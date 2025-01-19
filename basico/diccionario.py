numbers= {1:"uno",2:"dos",3:"tres"}
# Configuración de una aplicación
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
print("Configuración:", config)

# Contador de palabras
palabras = ["manzana", "banana", "naranja", "manzana", "banana"]
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Contador de palabras:", contador)

# Mapeo de usuarios a datos
usuarios = {
    "user123": {"nombre": "Juan", "edad": 30},
    "user456": {"nombre": "Ana", "edad": 25}
}
print("Datos de usuario user123:", usuarios["user123"])

# Almacenamiento de datos estructurados
libro = {
    "título": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967
}

print (type(libro))

############################

information= {"nombre":"carla", "apellido":"florida","altura":1.60,"edad":29}
print(information)
del information["edad"]
print(information)
# creo una variable llama llave para consultar las llave de la informacion 
clave=information.keys()
print(clave)
values=information.values()
print(values)
pairs=information.items()
print(pairs)

contacts={ "Carla":{"nombre":"carla", "apellido":"florida","altura":1.60,"edad":29},
          "Diego":{"nombre":"diego", "apellido":"Perez","altura":1.70,"edad":31}}

print(contacts["Diego"])