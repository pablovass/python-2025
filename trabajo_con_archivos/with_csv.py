import csv
# leer
#with open("trabajo_con_archivos/fictitious_products.csv", mode="r") as file:
#    csv_read = csv.DictReader(file)
#    for row in csv_read:
#        print(row)

#mostrar
with open("trabajo_con_archivos/fictitious_products.csv", mode="r") as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto:{row['Product']}, Precio:{row['Price']}")

#añadir un nuevo product
new_product={
    'Product':'mouse',
    'Price':'10.00',
    'Description':'es un mause argentino'
}
# mode = a de append
with open("trabajo_con_archivos/fictitious_products.csv", mode="a",newline='') as file:
    file.write('\n')
    csv_writerr=csv.DictWriter(file,fieldnames=new_product.keys())
    csv_writerr.writerow(new_product)
