def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    elif edad < 18:
        raise Exception("La persona es menor de edad")
    else:
        return "Edad válida"
    

try:
    divisor= int(input("ingrese un numero de divisor "))
    result =100/divisor
    print(result)
except ZeroDivisionError:
    print("error: el divisor no puede ser cero")
except ValueError:
    print("Error: ingresaste un valor errorneos")
    
    