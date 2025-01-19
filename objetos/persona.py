#clase con encapsulamiento
class Persona:
    def __init__(self, nombre, edad, ciudad):
        """
        Constructor con atributos encapsulados.
        """
        self.__nombre = nombre  # Atributos privados
        self.__edad = edad
        self.__ciudad = ciudad

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_ciudad(self):
        return self.__ciudad

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        if edad >= 0:  # Validación
            self.__edad = edad
        else:
            raise ValueError("La edad debe ser un número positivo.")

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad

    def saludar(self):
        """
        Método para saludar.
        """
        return f"Hola, me llamo {self.__nombre} y tengo {self.__edad} años. Vivo en {self.__ciudad}."

    def es_mayor_de_edad(self):
        """
        Método para verificar si la persona es mayor de edad.
        """
        return self.__edad >= 18


# Ejemplo de uso con encapsulamiento
persona1 = Persona("María", 25, "Buenos Aires")

# Acceso a través de getters y setters
print(persona1.get_nombre())  # María
persona1.set_edad(30)  # Cambiar la edad
print(persona1.saludar())  # Hola, me llamo María y tengo 30 años. Vivo en Buenos Aires.

# Intento de modificar directamente (prohibido)
# persona1.__edad = -5  # Esto no funcionará
