#   Codigo INT NOT NULL,
#   Doctor_codigo VARCHAR(5) NOT NULL,
#   paciente_codigo INT NOT NULL,
#   fecha DATE NOT NULL,
#TODO -> crear tabla receta

import csv
import random

cita_csv = "tablas_tuplas/citas/cita.csv"
citas = []

with open(cita_csv, "r") as archivo_csv:
    # Crear un lector de CSV
    lector_csv = csv.reader(archivo_csv)

    # Recorrer cada fila del archivo CSV
    for fila in lector_csv:
        # Agregar la fila a la lista de citas
        citas.append(fila)


def generate_recetas(n):
    recetas = []
    codigo_doctor_dni_set = set()  # Conjunto para evitar duplicados de combinaciones de código de doctor y DNI de paciente
    
    # Generar n recetas
    for _ in range(n):
        codigo_receta = random.randint(10000, 99999)
        cita = random.choice(citas)  
        codigo_doctor = cita[3]  
        dni_paciente = cita[0]  
        fecha_receta = cita[1]
        
        # Verificar si la combinación de código de doctor y DNI de paciente ya ha sido utilizada
        if (codigo_doctor, dni_paciente) in codigo_doctor_dni_set:
            continue  # Si ya ha sido utilizada, pasar a la siguiente iteración sin agregar la receta
        
        # Agregar la combinación de código de doctor y DNI de paciente al conjunto
        codigo_doctor_dni_set.add((codigo_doctor, dni_paciente))
        
        # Generar la receta y agregarla a la lista de recetas
        receta = (codigo_receta, fecha_receta, codigo_doctor, dni_paciente)
        recetas.append(receta)
        
    return recetas

with open("tablas_tuplas/recetas/receta.csv", "w") as archivo_csv:
    for receta in generate_recetas(90):
        codigo_receta, fecha_receta, doctor_codigo, paciente_codigo = receta
        archivo_csv.write(f"{codigo_receta},{fecha_receta},{doctor_codigo},{paciente_codigo}\n")
 

print("Recetas generadas")