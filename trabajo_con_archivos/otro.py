import json

# Ruta al archivo JSON
file_path = "trabajo_con_archivos/fictitious_products.json"

# Cargar el archivo JSON
with open(file_path, mode="r", encoding="utf-8") as file:
    products = json.load(file)  # Cargar los productos como una lista

# Verifica que el JSON contiene una lista
if isinstance(products, list):
    # Agregar un nuevo producto
    new_product = {
        "product": "mouse",
        "price": 12.50,
        "description": "Un mouse económico y funcional",
        "quantity": 10
    }
    products.append(new_product)  # Agregar el nuevo producto a la lista

    # Guardar los cambios en el archivo JSON
    with open(file_path, mode="w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=4)
else:
    print("El archivo JSON no contiene una lista de productos.")
