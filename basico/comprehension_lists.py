# es una forma mas consisa para crear lista y recorrela con un for mas consiso 

# obtener los numeros cuadrados del 1 al 10 
squares=[x**2 for x in range(1,11)]
#print("Cuadrado", squares)

# transformar de celsius a fahrenheit
celsius=[0,10,20,30,40]
fahrenheit=[(temp*9/5)*32 for temp in celsius]

#print("Temperatura en F:" ,fahrenheit)

#numeros pares 
evens=[x for x in range(1,20)if x%2==0]
#print(evens)

# allar la transpues de una matris 

matrice= [[1,2,3],
          [4,5,6],
          [7,8,9,]]
trasposed= [[row [i] for row in matrice] for i in range (len(matrice[0]))]
print(matrice)
print(trasposed)