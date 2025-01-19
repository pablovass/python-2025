class Persona:
    def saludar(self):
        return "Hola, soy una persona."

class Estudiante(Persona):
    def saludar(self):
        # Llamar al método saludar de la clase base
        saludo_base = super().saludar()
        return f"{saludo_base} También soy un estudiante."

# Crear una instancia de Estudiante
estudiante = Estudiante()
print(estudiante.saludar())  # Hola, soy una persona. También soy un estudiante.

#EJEMPLO AVANZADO
class A:
    def mostrar(self):
        print("Clase A")

class B(A):
    def mostrar(self):
        print("Clase B")
        super().mostrar()

class C(B):
    def mostrar(self):
        print("Clase C")
        super().mostrar()

obj = C()
obj.mostrar()
