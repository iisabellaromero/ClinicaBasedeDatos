# recetas_Codigo INT NOT NULL,
#   recetas_paciente_codigo INT NOT NULL,
#   farmacistas_Codigo VARCHAR(5) NOT NULL,
#   Hora TIMESTAMP NOT NULL,
#   codigo_venta INT NOT NULL,

import csv
import random
from datetime import datetime, timedelta

recetas_csv = "tablas_tuplas/recetas/receta.csv"
farmacistas_csv = "tablas_tuplas/empleados/farmaceuticos/farmaceuticos.csv"
recetas = []
farmacistas = []

with open(recetas_csv, newline='') as csvfile:
    lector_csv = csv.reader(csvfile)
    for row in lector_csv:
        recetas.append(row)

with open(farmacistas_csv, newline='') as csvfile:
    lector_csv = csv.reader(csvfile)
    for row in lector_csv:
        farmacistas.append(row)


def generar_tuplas(n):
    recetas_approved = []
    recetas_aprobadas_set = set()  
    
    for _ in range(n):
        receta = random.choice(recetas)
        farmacista = random.choice(farmacistas)
        
        receta_codigo = receta[0]
        farmacista_codigo = farmacista[0]
        hora = random.randint(8, 21)
        hora2 = datetime.strptime(str(hora), "%H")
        hora_formateada = f"{hora:02d}:00"
        codigo_venta = random.randint(1000, 9999)
        
        # Verificar si la receta ya ha sido aprobada por algún farmacista
        if receta_codigo in recetas_aprobadas_set:
            continue  # Si la receta ya ha sido aprobada, continuar
        
        tupla = (receta_codigo, farmacista_codigo, hora_formateada, codigo_venta)
        recetas_approved.append(tupla)
        recetas_aprobadas_set.add(receta_codigo) 
    
    return recetas_approved



with open("tablas_tuplas/recetas/recetas_aprobadas.csv", "w") as archivo:
    for tupla in generar_tuplas(61):
        receta_codigo, farmacista_codigo, hora_formateada, codigo_venta = tupla
        linea = f"{receta_codigo},{farmacista_codigo},{hora_formateada},{codigo_venta}\n"
        archivo.write(linea)

print("Recetas aprobadas generadas")