import random
from datetime import datetime, timedelta
#codigo, codigo_cmp, nombre, apellido1, apellido2, fecha_nacimiento, telefono,  dni, email

def generar_tuplas(n):
    nombres = ["Juan", "Pedro", "Luis", "Carlos", "Jorge", "Miguel", "Alberto", "Manuel", "Ricardo", "Javier",
           "Fernando", "Daniel", "Alejandro", "Francisco", "Pablo", "Sergio", "Antonio", "Jose", "David",
           "Diego", "Jesus", "Joaquin", "Ruben", "Adrian", "oscar", "Marcos", "Tomas", "Enrique", "Mariano",
           "Andres", "Rafael", "Vicente", "Julian", "Jordi", "Eduardo", "Jaime", "Hugo",
           "Ignacio", "Alfonso", "Gonzalo", "Salvador", "Roberto", "Guillermo", "Emilio", "Miguel angel",
           "Santiago", "Victor", "Ramon", "Aitor", "Ivan", "Martin", "Maria", "Ana", "Isabel", "Carmen", "Laura", "Marta", "Dolores", "Sara", "Cristina", "Andrea",
            "Paula", "Alba", "Sandra", "Rosa", "Lucia", "Elena", "Raquel", "Patricia", "Nuria", "Silvia",
            "Monica", "Beatriz", "Eva", "Camila", "Mercedes", "Belen", "Cielo", "Luz", "angela", "Clara","Lourdes", "Natalia", 
            "Marina", "angela", "Nerea", "Aitana", "Clara", "Irene", "Gloria", "Lidia",
            "Luna", "Olga", "Victoria", "Carolina", "Noelia", "Amparo", "Helena", "Aurora", "Ariadna", "Abril",
            "Estela", "Gisela", "Julia", "Celia", "Ines", "Sonia", "Elsa", "iria", "Ada", "Isidora", "Valeria",
            "Daniela", "Elisa", "Manuela", "Adela", "Rocio", "Margarita", "Montserrat", "Cecilia", "Naiara",
            "Almudena", "Ainhoa", "Ximena", "Carla", "Esther", "africa", "Eugenia", "Amelia", "Claudia", "Helga",
            "Miriam", "Renata", "Paloma", "Leire", "Salma", "Julieta", "Nora", "Adriana", "Linda", "Yolanda",
            "Berta", "Ariadna", "Emilia" ]

    apellidos = ["Gomez", "Lopez", "Rodriguez", "Perez", "Martinez", "Garcia", "Hernandez", "Fernandez", "Gonzalez",
            "Sanchez", "Ramirez", "Torres", "Flores", "Rivera", "Vargas", "Ruiz", "Diaz", "Reyes", "Morales",
            "Ortega", "Castillo", "Chavez", "Mendoza", "Delgado", "Silva", "Rojas", "Jimenez", "Navarro",
            "Cruz", "Valenzuela", "Rios", "Gutierrez", "Romero", "Vega", "Guerrero", "alvarez", "Montes",
            "Salazar", "Acosta", "Barrera", "Peña", "Cabrera", "Molina", "Soto", "Campos", "Ibarra", "Vera",
            "Peralta", "Figueroa", "Escobar", "Araya", "Lara", "Aguilar", "Miranda", "Sepulveda", "Contreras",
            "Luna", "Olivares", "Avila", "Espinoza", "Cortes", "Herrera", "Ponce", "Zuñiga", "Caceres",
            "Fuentes", "Bravo", "Guzman", "Tapia", "Vasquez", "Parra", "Pizarro", "Paredes", "Carvajal",
            "Carrasco", "Valdes", "Abarca", "Vidal", "Venegas", "Andrade", "Alarcon", "Aravena", "Bustos",
            "Bello", "Cisternas", "Cifuentes", "Duarte", "Estrada", "Gallardo", "Godoy", "Hidalgo", "Ibacache"]
    
    especialidades = ["Medicina General", "Pediatria","Obstetricia y Ginecologia","Cardiologia","Dermatologia","Gastroenterologia",
            "Neurologia","Psiquiatria","Oftalmologia","Otorrinolaringologia","Cirugia General","Cirugia Plastica","Urologia","Nefrologia",
            "Endocrinologia","Oncologia","Radiologia","Anestesiologia","Medicina Interna","Medicina Familiar y Comunitaria"]


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
        email = f"{nombre.lower()}.{apellido1.lower()}@vitasalud.com"
        especialidad = random.choice(especialidades)
        tupla = (codigo, codigo_cmp, nombre, apellido1, apellido2, fecha_nacimiento, telefono, dni, email, especialidad)
        tuplas.append(tupla)
    return tuplas

#generamos fecha de nacimiento
def generar_fecha():
    dia = random.randint(1, 28)
    if dia<10:
        dia = "0" + str(dia)
    mes = random.randint(1, 12)
    if mes<10:
        mes = "0" + str(mes)
    ano = random.randint(1930, 2023)
    fecha = f"{ano}-{mes}-{dia}"
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

#asignar a cada doctor un consultorio, estos se componen por una letra de la A a la J y un numero del 100 al 999 random
consultorios = []
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for i in range(10):
    for j in range(100, 1000):
        letra = random.choice(letras)
        consultorio = letra + str(j)
        consultorios.append(consultorio)

#tabla horarios

#generamos horainicio y horafin junto con dia de la semana y estado (disponible o no disponible) con el codigo del doctor
import random

def generar_horarios(tuplas):
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    horarios = []
    horarios_generados = set()
    
    for tupla in tuplas:
        codigo_doctor = tupla[0]
        horarios_doctor = set()
        
        while len(horarios_doctor) < 20:
            dia = random.choice(dias)
            hora_inicio = random.randint(8, 20)
            hora_fin = (hora_inicio + 1) % 24
            hora_inicio_formateada = f"{hora_inicio:02d}:00"
            hora_fin_formateada = f"{hora_fin:02d}:00"
            
            horario = (dia, hora_inicio_formateada, hora_fin_formateada, codigo_doctor, True)
            
            # Verificar si el horario ya ha sido generado para el doctor actual
            if horario in horarios_doctor:
                continue  # Si el horario ya existe, continuar con la siguiente iteracion
            
            horarios.append(horario)
            horarios_doctor.add(horario)
        
        horarios_generados.update(horarios_doctor)
    
    return horarios

horarios = generar_horarios(tuplas_generadas)

with open("tablas_tuplas/empleados/doctores/horarios.csv", "w") as archivo:
    for horario in horarios:
        dia, hora_inicio_formateada, hora_fin_formateada, codigo_doctor,estado = horario
        linea = f"{dia},{hora_inicio_formateada},{hora_fin_formateada},{codigo_doctor},{estado}\n"
        archivo.write(linea)

#guardar en un archivo de texto el codigo del doctor con su respectivo consultorio
with open("tablas_tuplas/empleados/doctores/consultorios.csv", "w") as archivo:
    for i in range(len(tuplas_generadas)):
        codigo, codigo_cmp,nombre, apellido1, apellido2, fecha_nacimiento, telefono, dni, email, especialiadad = tuplas_generadas[i]
        linea = f"{codigo},{consultorios[i]}\n"
        archivo.write(linea)

with open("tablas_tuplas/empleados/doctores/doctores.csv", "w") as archivo:
    for tupla in tuplas_generadas:
        codigo, codigo_cmp,nombre, apellido1, apellido2, fecha_nacimiento, telefono, dni, email, especialiadad = tupla
        linea = f"{codigo},{codigo_cmp},{nombre},{apellido1},{apellido2},{fecha_nacimiento},{telefono},{dni},{email},{especialiadad}\n"
        archivo.write(linea)

print("Archivo generado exitosamente")