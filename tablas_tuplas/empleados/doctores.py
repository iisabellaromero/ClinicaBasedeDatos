import random

#codigo, nombre, apellido1, apellido2, fecha_nacimiento, telefono, sueldo, dni, email

def generar_tuplas(n):
    nombres = ["Juan", "Pedro", "Luis", "Carlos", "Jorge", "Miguel", "Alberto", "Manuel", "Ricardo", "Javier",
           "Fernando", "Daniel", "Alejandro", "Francisco", "Pablo", "Sergio", "Antonio", "José", "David",
           "Diego", "Jesús", "Joaquín", "Rubén", "Adrián", "Óscar", "Marcos", "Tomás", "Enrique", "Mariano",
           "Andrés", "Rafael", "Vicente", "Julián", "Jordi", "Eduardo", "Jaime", "Hugo",
           "Ignacio", "Alfonso", "Gonzalo", "Salvador", "Roberto", "Guillermo", "Emilio", "Miguel Ángel",
           "Santiago", "Víctor", "Ramón", "Aitor", "Iván", "Martín", "María", "Ana", "Isabel", "Carmen", "Laura", "Marta", "Dolores", "Sara", "Cristina", "Andrea",
            "Paula", "Alba", "Sandra", "Rosa", "Lucía", "Elena", "Raquel", "Patricia", "Nuria", "Silvia",
            "Mónica", "Beatriz", "Eva", "Camila", "Mercedes", "Belén", "Cielo", "Luz", "Ángela", "Clara","Lourdes", "Natalia", "Marina", "Ángela", "Nerea", "Aitana", "Clara", "Irene", "Gloria", "Lidia",
            "Luna", "Olga", "Victoria", "Carolina", "Noelia", "Amparo", "Helena", "Aurora", "Ariadna", "Abril",
            "Estela", "Gisela", "Julia", "Celia", "Inés", "Sonia", "Elsa", "Íria", "Ada", "Isidora", "Valeria",
            "Daniela", "Elisa", "Manuela", "Adela", "Rocío", "Margarita", "Montserrat", "Cecilia", "Naiara",
            "Almudena", "Ainhoa", "Ximena", "Carla", "Esther", "África", "Eugenia", "Amelia", "Claudia", "Helga",
            "Miriam", "Renata", "Paloma", "Leire", "Salma", "Julieta", "Nora", "Adriana", "Linda", "Yolanda",
            "Berta", "Ariadna", "Emilia" ]

    apellidos = ["Gómez", "López", "Rodríguez", "Pérez", "Martínez", "García", "Hernández", "Fernández", "González",
            "Sánchez", "Ramírez", "Torres", "Flores", "Rivera", "Vargas", "Ruiz", "Díaz", "Reyes", "Morales",
            "Ortega", "Castillo", "Chávez", "Mendoza", "Delgado", "Silva", "Rojas", "Jiménez", "Navarro",
            "Cruz", "Valenzuela", "Ríos", "Gutiérrez", "Romero", "Vega", "Guerrero", "Álvarez", "Montes",
            "Salazar", "Acosta", "Barrera", "Peña", "Cabrera", "Molina", "Soto", "Campos", "Ibarra", "Vera",
            "Peralta", "Figueroa", "Escobar", "Araya", "Lara", "Aguilar", "Miranda", "Sepúlveda", "Contreras",
            "Luna", "Olivares", "Avila", "Espinoza", "Cortés", "Herrera", "Ponce", "Zúñiga", "Cáceres",
            "Fuentes", "Bravo", "Guzmán", "Tapia", "Vásquez", "Parra", "Pizarro", "Paredes", "Carvajal",
            "Carrasco", "Valdés", "Abarca", "Vidal", "Venegas", "Andrade", "Alarcón", "Aravena", "Bustos",
            "Bello", "Cisternas", "Cifuentes", "Duarte", "Estrada", "Gallardo", "Godoy", "Hidalgo", "Ibacache",]
    
    especialidades = ["Medicina General", "Pediatría","Obstetricia y Ginecología","Cardiología","Dermatología","Gastroenterología",
            "Neurología","Psiquiatría","Oftalmología","Otorrinolaringología","Cirugía General","Cirugía Plástica","Urología","Nefrología",
            "Endocrinología","Oncología","Radiología","Anestesiología","Medicina Interna","Medicina Familiar y Comunitaria"]


    nombres = list(set(nombres))
    apellidos = list(set(apellidos))
    tuplas = []


    for i in range(n):
        codigo = "D" + str(random.randint(1000, 9999))
        codigo_cmp = "0" + str(random.randint(10000, 99999))
        nombre = random.choice(nombres)
        apellido1 = random.choice(apellidos)
        apellido2 = random.choice(apellidos)
        fecha_nacimiento = generar_fecha()
        telefono = "9" + str(generar_telefono(tuplas))
        dni = generar_dni(tuplas)
        email = f"{nombre.lower()}.{apellido1.lower()}@hotmail.com"
        especialidad = random.choice(especialidades)
        tupla = (codigo, codigo_cmp, nombre, apellido1, apellido2, fecha_nacimiento, telefono, dni, email, especialidad)
        tuplas.append(tupla)
    return tuplas

#generamos fecha de nacimiento
def generar_fecha():
    dia = random.randint(1, 28)
    mes = random.randint(1, 12)
    ano = random.randint(1930, 2023)
    fecha = f"{dia}/{mes}/{ano}"
    return fecha

#generamos telefono
def generar_telefono(tuplas):
    while True:
        telefono = random.randint(10000000, 99999999)
        if telefono not in [t[4] for t in tuplas]:
            break
    return telefono

#genramos dni
def generar_dni(tuplas):
    while True:
        dni = random.randint(10000000, 99999999)
        if dni not in [t[5] for t in tuplas]:
            break
    return dni

tuplas_generadas = generar_tuplas(150)

with open("doctores.txt", "w") as archivo:
    for tupla in tuplas_generadas:
        codigo, codigo_cmp,nombre, apellido1, apellido2, fecha_nacimiento, telefono, dni, email, especialiadad = tupla
        linea = f"{codigo}, {codigo_cmp}, {nombre}, {apellido1}, {apellido2}, {fecha_nacimiento}, {telefono}, {dni}, {email}, {especialiadad}\n"
        archivo.write(linea)

print("Archivo generado exitosamente")