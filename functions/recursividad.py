# allar el factorial de 5! = 5*4*3*2*1  4! = 4*3*2*1
# para obtener el factoria de un numero n tengo que multiplicar el numero


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


factorial_5 = print(factorial(5))


# obtener los valores de fibbonaci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = 5
print(fibonacci(number))
