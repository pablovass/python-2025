# Clase base (padre)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

# Clase derivada (hija)
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        # Llamar al constructor de la clase base
        super().__init__(nombre, edad)
        self.grado = grado

    def estudiar(self):
        return f"{self.nombre} está estudiando en el grado {self.grado}."

# Uso de las clases
estudiante = Estudiante("Ana", 20, "Universidad")
print(estudiante.saludar())  # Hola, soy Ana y tengo 20 años.
print(estudiante.estudiar())  # Ana está estudiando en el grado Universidad.
