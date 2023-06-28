#TUPLA -> (fecha, Hora_inicio, doctor_codigo, especialidad, paciente_dni, consultorio_codigo, precio, precio_deducible)
import csv
import random
from datetime import datetime, timedelta

# Ruta del archivo CSV
doctores_csv = "tablas_tuplas/empleados/doctores/doctores.csv"
pacientes_csv = "tablas_tuplas/pacientes/paciente.csv"
consultorios_csv = "tablas_tuplas/empleados/doctores/consultorios.csv"
horarios_csv = "tablas_tuplas/empleados/doctores/horarios.csv"
numero_citas = 100

# Lista de doctores
doctores = []
pacientes = []
consultorios = []
horarios = []

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

with open(horarios_csv, "r") as archivo_csv:
    # Crear un lector de CSV
    lector_csv = csv.reader(archivo_csv)

    # Recorrer cada fila del archivo CSV
    for fila in lector_csv:
        # Agregar la fila a la lista de horarios
        horarios.append(fila)

citas_generadas = set()  # Utilizamos un conjunto para evitar repeticiones


#generamos fecha de la cita
def generar_fecha():
    dia = random.randint(1, 28)
    if dia<10:
        dia = "0" + str(dia)
    mes = random.randint(7, 12)
    if mes<10:
        mes = "0" + str(mes)
    ano = 2023
    fecha = f"{ano}-{mes}-{dia}"
    return fecha

 
# Lista de citas
def generar_citas(n):
    citas = []
    for i in range(n):
        horario = random.choice(horarios)
        fecha = generar_fecha()
        hora_inicio_formateada = horario[1]
        consultorio = 'a'
        paciente = random.choice(pacientes)[5]
        precio = 200
        precio_deducible = 0
        dia = horario[0]
        
        doctor = horario[3]

        for doc in doctores:
            if doc[0] == doctor:
                especialidad = doc[9]
                break

        for cons in consultorios:
            if doctor == cons[0]:
                consultorio = cons[1]
                break

        if doctor is not None and especialidad is not None:
            citas.append((paciente,fecha, hora_inicio_formateada, horario[3], especialidad, consultorio, precio, precio_deducible,dia))
    return citas


with open("tablas_tuplas/citas/cita.csv", "w") as archivo_csv:
    for cita in generar_citas(numero_citas):
        paciente,fecha, hora_inicio_formateada, doctor_codigo, especialidad, consultorio_codigo, precio, precio_deducible,dia = cita
        linea = f"{paciente},{fecha},{hora_inicio_formateada},{doctor_codigo},{especialidad},{consultorio_codigo},{precio},{precio_deducible},{dia}\n"
        archivo_csv.write(linea)

print("Citas generadas")