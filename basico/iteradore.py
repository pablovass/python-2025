#ejemplos de iteradores 
#crear una lista
my_list=[1,2,3,4]
my_iter=iter(my_list)
# print(next(my_iter)) #solo imprime el prmer numero
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

texto="hola mundo"
iter_text=iter(texto)

for char in iter_text:
    print(char)


#crear un iterador para los numeros impres 
# limite 
limit=10 
odd_iter = iter (range(1,limit+1,2)) # impares pero si quiero el par  (range(0,limit+1,2))
#usar el iterdor
for num in odd_iter:
    print(num)

#fibonacci 
# 0 1 1 2 3 5 8 13 21
def fibonacci(limit):
    a,b=0,1
    while a < limit: 
        yield a 
        a,b=b, a+b

for num in fibonacci(10):
    print(num)
    