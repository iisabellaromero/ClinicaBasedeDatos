import random


companias_seguros = [
"Rimac Seguros de Salud",
"Pacifico Seguros de Salud",
"La Positiva Seguros de Salud",
"Mapfre Peru Seguros de Salud",
"Interseguro Seguros de Salud",
"Sura Peru Seguros de Salud",
"Oncosalud",
"Sanitas Peru",
"Essalud",
"Previred",
"Penta Salud",
"La Molina Seguros",
"Seguros Falabella",
"Protecta",
"Grupo Breca",
"Global Seguros",
"Rigel Seguros",
"Seguros Sura",
"Seguros Pelayo",
"Seguros RCI",
"Seguros SBS",
"Seguros Interamericana",
"Seguros Wiese",
"Seguros Credicorp",
"Seguros Chubb",
"Seguros Generali",
"Seguros Zurich",
"Seguros HDI",
"Seguros Rimac EPS",
"Seguros La Union"
]

nombres_polizas = [
    "Salud Protegida",
    "Cuidado Total",
    "Familia Sana",
    "Seguro Medico Integral",
    "Bienestar Activo",
    "Salud Primordial",
    "Proteccion Vitalicia",
    "Cobertura Medica Plus",
    "Salud Flexible",
    "Seguro Dental Completo",
    "Prevencion Total",
    "Cobertura Global de Salud",
    "Plan de Bienestar Familiar",
    "Proteccion en Emergencias",
    "Cuidado Preventivo",
    "Seguro de Enfermedades Cronicas",
    "Plan Materno-Infantil",
    "Seguro de Rehabilitacion",
    "Cobertura de Medicamentos",
    "Cuidado Geriatrico",
    "Seguro de Asistencia Medica",
    "Cobertura de Cirugias",
    "Bienestar Mental",
    "Proteccion Ocular",
    "Plan de Salud Holistico",
    "Seguro de Medicina Alternativa",
    "Cobertura de Tratamientos Especiales",
    "Seguro de Terapia Fisica",
    "Plan de Nutricion y Dietetica"
]

tuplas_seguros = []
tuplas_polizas = []

for compania in companias_seguros:
    codigo_seguro = random.randint(10000, 99999)
    tupla_seguro = (codigo_seguro, compania)
    tuplas_seguros.append(tupla_seguro)
    num_polizas = random.randint(1, 5)  # Determinar el numero de polizas para el seguro actual
    for _ in range(num_polizas):
        poliza = random.choice(nombres_polizas)
        id_poliza = random.randint(10000, 99999)
        cobertura = random.randint(10, 70)
        tupla_poliza = (codigo_seguro, poliza, id_poliza, cobertura)
        tuplas_polizas.append(tupla_poliza)

with open("tablas_tuplas/seguros/polizas_seguros.csv", "w") as archivo_polizas:
    for tupla in tuplas_polizas:
        codigo_seguro, poliza, id_poliza, cobertura = tupla
        linea = f"{codigo_seguro},{id_poliza},{poliza},{cobertura}\n"
        archivo_polizas.write(linea)

with open("tablas_tuplas/seguros/companias_seguros.csv", "w") as archivo_seguros:
    for tupla in tuplas_seguros:
        codigo_seguro, nombre_seguro = tupla
        linea = f"{codigo_seguro},{nombre_seguro}\n"
        archivo_seguros.write(linea)

print("Archivos generados exitosamente")