import csv

file_path = "trabajo_con_archivos/fictitious_products.csv"
update_file_path = "trabajo_con_archivos/fictitious_products_update.csv"

with open(file_path, mode="r") as file:
    csv_reader = csv.DictReader(file)
    # obtener los nombres de las columnas existenes
    fieldName = csv_reader.fieldnames + ["total_values"]

    with open(update_file_path, mode="w", newline="") as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldName)
        csv_writer.writeheader()  # escribir encabezado

        for row in csv_reader:
            row["total_value"] = float(row["Price"]) * int(row["quantity"])
            csv_writer.writerow(row)
