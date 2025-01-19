with open ("trabajo_con_archivos/file.txt", "r") as file:
   for lineas in file:
       print(lineas.strip())
# RETO conteo de las lineas del cuento de caperucita
with open ("trabajo_con_archivos/file.txt", "r") as file:
    lines = file.readlines()
    print(len(lines)) 

# sobre-escribir
with open('trabajo_con_archivos/file.txt','a')as file:
    file.write("\n\n By:Pablovass")

#sobre-escribir pero se borra tod con la w.  
with open('trabajo_con_archivos/file.txt','w')as file:
    file.write("")