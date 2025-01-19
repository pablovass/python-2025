class Deportista:
    def entrenar(self):
        return "Estoy entrenando."

class Estudiante:
    def estudiar(self):
        return "Estoy estudiando."

# Clase hija que hereda de ambas
class EstudianteDeportista(Deportista, Estudiante):
    pass

persona = EstudianteDeportista()
print(persona.entrenar())  # Estoy entrenando.
print(persona.estudiar())  # Estoy estudiando.
