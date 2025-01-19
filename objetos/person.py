class Persona:
    def __init__(self, nombre, edad, ciudad): # self es el quivalente a this de java
        """
        Constructor de la clase Persona.
        :param nombre: Nombre de la persona (str)
        :param edad: Edad de la persona (int)
        :param ciudad: Ciudad donde vive la persona (str)
        """
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludar(self):
        """
        Método para que la persona salude.
        """
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años. Vivo en {self.ciudad}."

    def es_mayor_de_edad(self):
        """
        Método para verificar si la persona es mayor de edad.
        """
        return self.edad >= 18

    def __str__(self):
        """
        Representación en forma de cadena de la persona.
        """
        return f"Persona(nombre='{self.nombre}', edad={self.edad}, ciudad='{self.ciudad}')"


# Ejemplo de uso:
persona1 = Persona("María", 25, "Buenos Aires")
print(persona1.saludar())  # Hola, me llamo María y tengo 25 años. Vivo en Buenos Aires.
print(f"¿Es mayor de edad? {'Sí' if persona1.es_mayor_de_edad() else 'No'}")  # Sí
print(persona1)  # Persona(nombre='María', edad=25, ciudad='Buenos Aires')
