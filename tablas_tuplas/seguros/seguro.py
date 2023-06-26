import random


companias_seguros = [
"Rimac Seguros de Salud",
"Pacífico Seguros de Salud",
"La Positiva Seguros de Salud",
"Mapfre Perú Seguros de Salud",
"Interseguro Seguros de Salud",
"Sura Perú Seguros de Salud",
"Oncosalud",
"Sanitas Perú",
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
"Seguros La Unión"
]

nombres_polizas = [
    "Salud Protegida",
    "Cuidado Total",
    "Familia Sana",
    "Seguro Médico Integral",
    "Bienestar Activo",
    "Salud Primordial",
    "Protección Vitalicia",
    "Cobertura Médica Plus",
    "Salud Flexible",
    "Seguro Dental Completo",
    "Prevención Total",
    "Cobertura Global de Salud",
    "Plan de Bienestar Familiar",
    "Protección en Emergencias",
    "Cuidado Preventivo",
    "Seguro de Enfermedades Crónicas",
    "Plan Materno-Infantil",
    "Seguro de Rehabilitación",
    "Cobertura de Medicamentos",
    "Cuidado Geriátrico",
    "Seguro de Asistencia Médica",
    "Cobertura de Cirugías",
    "Bienestar Mental",
    "Protección Ocular",
    "Plan de Salud Holístico",
    "Seguro de Medicina Alternativa",
    "Cobertura de Tratamientos Especiales",
    "Seguro de Terapia Física",
    "Plan de Nutrición y Dietética"
]

tuplas_seguros = []
tuplas_polizas = []

for compania in companias_seguros:
    codigo_seguro = random.randint(10000, 99999)
    tupla_seguro = (codigo_seguro, compania)
    tuplas_seguros.append(tupla_seguro)
    num_polizas = random.randint(1, 5)  # Determinar el número de pólizas para el seguro actual
    for _ in range(num_polizas):
        poliza = random.choice(nombres_polizas)
        id_poliza = random.randint(10000, 99999)
        cobertura = random.randint(10, 70)
        tupla_poliza = (codigo_seguro, poliza, id_poliza, cobertura)
        tuplas_polizas.append(tupla_poliza)

with open("tablas_tuplas/seguros/polizas_seguros.csv", "w") as archivo_polizas:
    for tupla in tuplas_polizas:
        codigo_seguro, poliza, id_poliza, cobertura = tupla
        linea = f"{codigo_seguro}, {id_poliza}, {poliza}, {cobertura}\n"
        archivo_polizas.write(linea)

with open("tablas_tuplas/seguros/companias_seguros.csv", "w") as archivo_seguros:
    for tupla in tuplas_seguros:
        codigo_seguro, nombre_seguro = tupla
        linea = f"{codigo_seguro}, {nombre_seguro}\n"
        archivo_seguros.write(linea)

print("Archivos generados exitosamente")