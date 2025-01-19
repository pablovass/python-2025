to_do=[" LangGraph y LangChain son principalmente librerías de Python",
       " diseñadas para facilitar el desarrollo de aplicaciones que interactúan con modelos de lenguaje",
         "y herramientas de inteligencia artificial. Sin embargo",
          "también tienen soporte parcial o extensiones para JavaScript/TypeScript"]

print(to_do)

numbers=[1,2,3,4,"cinco"]
print (type(numbers))

mix=["uno",2,3.14,True,[1,2,3]]
print(mix)
print(len(mix))
print('primer elemento',mix[1])

print (mix[2:-2]) # le estoy diciendo de donde a donde quiero ir. 
print (mix[:2]) # se omite el numero si quiero ir del cero hacia otro valor

mix.append(False) # estoy agregando algo mas pero no es parte dela lista. y se agrega al final 
mix.insert(1,['a','b']) # se le agrega 1ro la posicion y despues los elementos 

print(mix.index(['a','b'])) #consultando el index 
numbers= [1,2,100,9045,3,4]
print("Mayor",max(numbers))
print("Mayor",min(numbers))
del numbers [-1]
print (numbers)
del numbers[-2]
print(numbers)
del numbers
print (numbers)



