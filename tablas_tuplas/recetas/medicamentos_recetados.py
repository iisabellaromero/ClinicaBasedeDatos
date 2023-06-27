# receta_codigo INT NOT NULL,
#   medicamento_codigo INT NOT NULL,
#   nombre_medicamento VARCHAR(45) NOT NULL, <- lo agregue yo
#   cantidad INT NOT NULL,
#   precio DOUBLE PRECISION NOT NULL,


import csv
import random

medicamentos_csv = "tablas_tuplas/medicamentos/medicamentos.csv"
receta_csv = "tablas_tuplas/recetas/receta.csv"

medicamentos = []
recetas = []

with open(medicamentos_csv, "r") as archivo_csv:
    # Crear un lector de CSV
    lector_csv = csv.reader(archivo_csv)

    # Recorrer cada fila del archivo CSV
    for fila in lector_csv:
        # Agregar la fila a la lista de medicamentos
        medicamentos.append(fila)

with open(receta_csv, "r") as archivo_csv:
    # Crear un lector de CSV
    lector_csv = csv.reader(archivo_csv)

    # Recorrer cada fila del archivo CSV
    for fila in lector_csv:
        # Agregar la fila a la lista de recetas
        recetas.append(fila)

def generate_medicamentos_recetados(n):
    medic_recetados = []
    for _ in range(n):
        numero = random.randint(1,7)
        receta = random.choice(recetas)
        codigo_receta = receta[0]
        for i in range(numero):
            medicamento = random.choice(medicamentos)
            codigo_medicamento = medicamento[0]
            nombre_medicamento = medicamento[1]
            cantidad = random.randint(1, 10)
            medic_recetado = (codigo_receta, codigo_medicamento, nombre_medicamento, cantidad)
            medic_recetados.append(medic_recetado)
    return medic_recetados


with open("tablas_tuplas/recetas/recetas_aprobadas.csv", "w") as archivo_csv:
    for medic_recetado in generate_medicamentos_recetados(90):
        codigo_receta, codigo_medicamento, nombre_medicamento, cantidad = medic_recetado
        linea = f"{codigo_receta},{codigo_medicamento},{nombre_medicamento},{cantidad}\n"
        archivo_csv.write(linea)
print("Medicamentos recetados generados")
