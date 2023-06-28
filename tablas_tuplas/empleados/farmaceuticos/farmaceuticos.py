import random

#codigo, nombre, apellido1, apellido2, fecha_nacimiento, telefono, sueldo, dni, email

def generar_tuplas(n):
    nombres = ["Luis", "Juan", "Carlos", "Jorge", "Pedro", "Jose", "Miguel", "Fernando", "Ricardo", "Manuel",
                "Cesar", "Marco", "Antonio", "Daniel", "David", "Hector", "Javier", "Oscar", "Raul", "Enrique",
                "Eduardo", "Walter", "Roberto", "Alberto", "Wilfredo", "Julio", "Gustavo", "Francisco", "Mario",
                "Ernesto", "Alejandro", "Gonzalo", "Hugo", "Diego", "Felix", "Nelson", "Armando", "Erick", "Renzo",
                "Josue", "Pablo", "Efrain", "Marcos", "Nestor", "Victor", "Frank", "Sergio", "Ciro", "Edgar",
                "Marcelo", "Orlando", "Eloy", "Henry", "Fredy", "Marlon", "Edwin", "Guido", "Albert", "Roger",
                "Andres", "Emilio", "Maria", "Carmen", "Rosa", "Ana", "Luz", "Isabel", "Elena", "Juana",
                "Margarita", "Gloria", "Patricia", "Cecilia", "Sandra", "Claudia", "Ruth", "Susana", "Elizabeth",
                "Angelica", "Victoria", "Teresa", "Liliana", "Sara", "Adriana", "Rocio", "Maribel", "Nancy",
                "Martha", "Pilar", "Gisela", "Yolanda", "Ingrid", "Roxana", "Alicia", "Monica", "Magdalena",
                "Silvia", "Eva", "Veronica", "Rita", "Olga", "Beatriz", "Lidia", "Miriam", "Laura", "Lucia",
                "Cristina", "Lourdes", "Carolina", "Diana", "Julia", "Raquel", "Elsa", "Janet", "Gabriela",
                "Lilia", "Marlene", "Fiorella", "Rina", "Lissette", "Linda", "Pamela", "Esther", "Wendy", "Flor",
                "Marisol"]
    
    apellidos = ["Lopez", "Garcia", "Rodriguez", "Perez", "Gonzalez", "Torres", "Vargas", "Romero", "Flores", "Ramirez",
                  "Sanchez", "Hernandez", "Cruz", "Ramos", "Diaz", "Carranza", "Castillo", "Vega", "Gomez", "Ortega",
                  "Medina", "Salazar", "Huaman", "Pacheco", "Leon", "Gutierrez", "Silva", "Mendoza", "Paredes", "Soto",
                  "Vera", "Fernandez", "Morales", "Vargas", "Peña", "Quispe", "Estrella", "Alvarez", "Saucedo", "Arce",
                  "Rojas", "Poma", "Valencia", "Acuña", "Mamani", "Yauri", "Aguilar", "Chavez", "Valenzuela", "Calderon",
                  "Campos", "Luna", "Villanueva", "Valle", "Pizarro", "Valdez", "Castañeda", "Puma", "Zapata", "Estrada",
                  "Guerrero", "Navarro", "Morales", "Carmona", "Mayta", "Roca", "Landa", "Torres", "Vallejos", "Loayza",
                  "Chambi", "Cardenas", "Hinojosa", "Reyes", "Maldonado", "Arias", "Condori", "Miranda", "Cordova",
                  "Gallardo", "Aguirre"]


    nombres = list(set(nombres))
    apellidos = list(set(apellidos))
    tuplas = []


    for i in range(n):
        codigo = "F" + str(random.randint(1000, 9999))
        codigo_cmp = "0" + str(random.randint(10000, 99999))
        nombre = random.choice(nombres)
        apellido1 = random.choice(apellidos)
        apellido2 = random.choice(apellidos)
        fecha_nacimiento = generar_fecha()
        telefono = "9" + str(generar_telefono(tuplas))
        dni = generar_dni(tuplas)
        email = f"{nombre.lower()}.{apellido1.lower()}@vitasalud.com"
        tupla = (codigo, codigo_cmp, nombre, apellido1, apellido2, fecha_nacimiento, telefono, dni, email)
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

with open("tablas_tuplas/empleados/farmaceuticos/farmaceuticos.csv", "w") as archivo:
    for tupla in tuplas_generadas:
        codigo, codigo_cmp,nombre, apellido1, apellido2, fecha_nacimiento, telefono, dni, email= tupla
        linea = f"{codigo},{nombre},{apellido1},{apellido2},{fecha_nacimiento},{telefono},{dni},{email}\n"
        archivo.write(linea)

print("Archivo generado exitosamente")