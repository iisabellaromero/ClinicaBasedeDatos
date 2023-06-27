#TUPLA -> (fecha, Hora_inicio, doctor_codigo, especialidad, paciente_dni, consultorio_codigo, precio, precio_deducible)
import csv
import random
from datetime import datetime, timedelta

# Ruta del archivo CSV
doctores_csv = "tablas_tuplas/empleados/doctores/doctores.csv"
pacientes_csv = "tablas_tuplas/pacientes/paciente.csv"
consultorios_csv = "tablas_tuplas/empleados/doctores/consultorios.csv"
numero_citas = 100

# Lista de doctores
doctores = []
pacientes = []
consultorios = []

with open(doctores_csv, "r") as archivo_csv:
    # Crear un lector de CSV
    lector_csv = csv.reader(archivo_csv)

    # Recorrer cada fila del archivo CSV
    for fila in lector_csv:
        # Agregar la fila a la lista de doctores
        doctores.append(fila)

with open(pacientes_csv, "r") as archivo_csv:
    # Crear un lector de CSV
    lector_csv = csv.reader(archivo_csv)

    # Recorrer cada fila del archivo CSV
    for fila in lector_csv:
        # Agregar la fila a la lista de pacientes
        pacientes.append(fila)

with open(consultorios_csv, "r") as archivo_csv:
    # Crear un lector de CSV
    lector_csv = csv.reader(archivo_csv)

    # Recorrer cada fila del archivo CSV
    for fila in lector_csv:
        # Agregar la fila a la lista de consultorios
        consultorios.append(fila)

citas_generadas = set()  # Utilizamos un conjunto para evitar repeticiones


#generamos fecha de la cita
def generar_fecha():
    dia = random.randint(1, 28)
    mes = random.randint(7, 12)
    ano = 2023
    fecha = f"{dia}/{mes}/{ano}"
    return fecha


# Lista de citas
def generar_citas(n):
    citas = []
    for i in range(n):
        fecha = generar_fecha()
        hora_inicio = random.randint(8, 20)
        inicio = datetime.strptime(str(hora_inicio), "%H")
        hora_inicio_formateada = f"{hora_inicio:02d}:00"
        consultorio = random.choice(consultorios)
        paciente = random.choice(pacientes)[5]
        precio = 200
        precio_deducible = 0
        
        doctor = None
        especialidad = None
        
        for doc in doctores:
            if consultorio[0] == doc[0]:
                doctor = doc
                especialidad = doc[9]
                break
        
        if doctor is not None and especialidad is not None:
            citas.append((paciente,fecha, hora_inicio_formateada, doctor[0], especialidad, consultorio[1], precio, precio_deducible))
    return citas

with open("tablas_tuplas/citas/cita.csv", "w") as archivo_csv:
    for cita in generar_citas(numero_citas):
        paciente,fecha, hora_inicio_formateada, doctor_codigo, especialidad, consultorio_codigo, precio, precio_deducible = cita
        linea = f"{paciente}, {fecha}, {hora_inicio_formateada}, {doctor_codigo}, {especialidad},{consultorio_codigo}, {precio}, {precio_deducible}\n"
        archivo_csv.write(linea)

print("Citas generadas")