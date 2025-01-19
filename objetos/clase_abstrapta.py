#Python no tiene clases abstractas como tal, pero puedes usar el módulo abc (Abstract Base Classes) 
# para definir clases y métodos abstractos.
from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def saludar(self):
        pass

class Estudiante(Persona):
    def saludar(self):
        return "Hola, soy un estudiante."

# Esto fallará: no puedes instanciar una clase abstracta
# persona = Persona()

estudiante = Estudiante()
print(estudiante.saludar())  # Hola, soy un estudiante.
