def greet():
    print("saludar")

def greet_with_params(name):
    print ("hola ",name)

def greet_with_params_2(name, last_name="no tien apellido"):
    print("hola", name,last_name)

greet()
greet_with_params("pablo")
greet_with_params_2("Jose","Pepe")
greet_with_params_2("Adrian")

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def producto(a,b):
    return a * b

def division(a,b):
    if b == 0:
        print('Error: No se puede dividir por 0')
    else:
        return a / b


def calculadora():
    while True:
        print('Seleccione una opción del 1 al 5:')
        print('1. Suma')
        print('2. Resta')
        print('3. Producto')
        print('4. Division')
        print('5. Salir')

        try:
            opcion = int(input('Ingrese la opción elegida: '))
        except:
            print('Entrada no válida, por favor ingrese un valor entre 1 y 5')
            continue

        if opcion == 5:
            print('Saliendo de la calculadora')
            break

        if opcion in [1,2,3,4]:
            try:
                num1 = float(input('Ingrese el primer número: '))
                num2 = float(input('Ingrese el segundo número: '))
            except:
                print('Entrada no válida. Por favor ingrese números válidos.')
                continue

            if opcion == 1:
                print(f'{num1} + {num2} = ', suma(num1,num2))
            elif opcion ==2:
                print(f'{num1} - {num2} = ', resta(num1,num2))
            elif opcion == 3:
                print(f'{num1} * {num2} = ', producto(num1,num2))
            elif opcion == 4:
                print(f'{num1} / {num2} = ', division(num1,num2))
        else:
            print('No es una opción valida. Intente nuevamente por favor')

calculadora()