import csv
import random

# Ruta del archivo CSV
pacientes_csv = "tablas_tuplas/pacientes/paciente.csv"
polizas_y_seguros_csv = "tablas_tuplas/seguros/polizas_seguros.csv"
numero_pacientes = 10000

# Lista para almacenar los datos del CSV
pacientes = []
polizas_y_seguros = []
tuplas = []
# Abrir el archivo CSV en modo lectura
with open(pacientes_csv, "r") as archivo_csv:
    # Crear un lector de CSV
    lector_csv = csv.reader(archivo_csv)

    # Recorrer cada fila del archivo CSV
    for fila in lector_csv:
        # Agregar la fila a la lista de pacientes
        pacientes.append(fila)

with open(polizas_y_seguros_csv, "r") as archivo_csv2:
    # Crear un lector de CSV
    lector_csv = csv.reader(archivo_csv2)

    # Recorrer cada fila del archivo CSV
    for fila in lector_csv:
        # Agregar la fila a la lista de polizas_y_seguros
        polizas_y_seguros.append(fila)


#pacientes_DNI, poliza_id, seguro_id

def generar_tuplas(n):
    for _ in range(n):
        paciente = random.choice(pacientes)
        poliza = random.choice(polizas_y_seguros)
        poliza_id = poliza[0]
        seguro_id = poliza[1]
        paciente_DNI = paciente[5]
        tupla = (paciente_DNI, poliza_id, seguro_id)
        tuplas.append(tupla)
    return tuplas

tuplas_generadas = set()  # Utilizamos un conjunto para evitar repeticiones
paciente_dnis_generados = set()  # Utilizamos un conjunto para almacenar los paciente_DNI generados

# Para que no se repitan los dnis, ya que son la clave primaria (una persona no puede tener mas de dos seguros de salud)
while len(tuplas_generadas) < 600000:
    nuevas_tuplas = generar_tuplas(1000)
    for tupla in nuevas_tuplas:
        paciente_DNI, poliza_id, seguro_id = tupla
        if paciente_DNI not in paciente_dnis_generados:
            paciente_dnis_generados.add(paciente_DNI)
            tuplas_generadas.add(tupla)

with open("tablas_tuplas/asegurados/asegurado.csv", "a") as archivo_csv:
    for tupla in tuplas_generadas:
        paciente_DNI, poliza_id, seguro_id = tupla
        linea = f"{paciente_DNI},{poliza_id},{seguro_id}\n"
        archivo_csv.write(linea)

print("Archivo generado exitosamente5")