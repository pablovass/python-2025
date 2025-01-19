import json

# lectura de archivo
with open("trabajo_con_archivos/fictitious_products.json", mode="r") as file:
    products = json.load(file)

# mostrar
for product in products:
    print(product)

print(f"Producto:{product['product']}")

new_product = {
    "Product": "mouse guitarra",
    "Price": "10.00",
    "Description": "es un mause argentino y argentino",
    "quantity": "7",
}

with open("trabajo_con_archivos/fictitious_products.json", mode="r") as file:
    products = json.load(file)
    product.append(new_product)

with open("trabajo_con_archivos/fictitious_products.json", mode="w") as file:
    json.dump(product, file, indent=4)
