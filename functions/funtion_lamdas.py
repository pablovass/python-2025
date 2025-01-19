#las landas son funciones anonimas

add = lambda a,b: a+b # es la suma de a +b 
print(add(10,4))

# el cuadrado de cada numero 
numbers= range(11)
squared_numer = list(map(lambda x: x**2,numbers))
print("Cuadrado: ", squared_numer)

#obtener los resultados de numeros pares 
even_numbers= list(filter(lambda x:x%2==0, numbers))
print("pares:", even_numbers)

