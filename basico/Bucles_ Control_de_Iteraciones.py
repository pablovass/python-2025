numbers = [1,2,3,4,5,6]
for i in numbers:
    print (i+1) 

for i in range (3,10):  #recore los numeros entre el 3 al 9 
    print(i)

fruits= ["manzana","pera","uva","naranja","tomate"]
for fruta in fruits:
    print(fruta)
    if fruta == "naranja":
        print("naranja encontrada")

x=0
while x<5:
    if x ==3:
        break
    print(x)
    x+=1 


numbers = [1,2,3,4,5,6]
for i in numbers:
    if i ==3:
        continue # va a omitir la condicion de tres y seguira el bucle pero si pone un breck se corta al llegar a breack
    print (i+1) 