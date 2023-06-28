import random

#nombres y apellidos generados por chat gpt
def generar_tuplas(n):
    nombres = ["Juan", "Maria", "Carlos", "Ana", "Luis", "Laura", "Pedro", "Sofia", "Diego", "Valentina",
               "Jose", "Carmen", "Manuel", "Isabella", "Miguel", "Fernanda", "Antonio", "Gabriela", "Javier",
               "Andrea", "Ricardo", "Daniela", "Francisco", "Camila", "Alejandro", "Paula", "Rafael", "Lucia",
               "Eduardo", "Mariana", "Gonzalo", "Valeria", "Roberto", "Julia", "Mario", "Natalia", "Hugo",
               "Catalina", "Fernando", "Victoria", "Alberto", "Elena", "Juan Carlos", "Marcela", "Andres",
               "Carolina", "Emilio", "Adriana", "Raul", "Silvia", "Emilia", "Pablo", "Veronica", "Mateo",
               "Diana", "Sebastian", "Karen", "Rodrigo", "Alexandra", "Nicolas", "Cecilia", "Renata", "Ramon",
               "Monica", "Esteban", "Patricia", "Ignacio", "Gabriel", "Cristina", "angel", "Ines", "Olivia",
               "Raul", "Mara", "Emmanuel", "Alma", "Samuel", "Alicia", "Arturo", "Ximena", "Maximiliano",
               "Sara", "Benjamin", "Emily", "Salvador", "Isabel", "Ruben", "Esmeralda", "Hector", "Jennifer",
               "Damian", "Marisol", "Mauricio", "Paulina", "Agustin", "Luciana", "Ezequiel", "Gabrielle", "Matias",
               "Valerie", "Bruno", "Olga", "Sebastiana", "Joaquin", "Carla", "Marcos", "Florencia", "Facundo",
               "Rene", "Santiago", "Ximena", "Samanta", "Melanie", "Daniel", "Teresa", "Lorenzo", "Regina",
               "Jaime", "Rosa", "Teodoro", "Blanca", "Orlando", "Soledad", "Elena", "Cesar", "Antonia",
               "Felipe", "Martha", "Raul", "Catalina", "Octavio", "Beatriz", "Gustavo", "Raquel", "Leonardo",
               "Hernan", "Natalie", "Federico", "Jimena", "Renato", "Aurora", "Bruno", "Miranda", "Emilio",
               "Carolina", "Ivan", "Vanessa", "Roberto", "Valeria", "Hector", "Cecilia", "Felipe", "Luciana",
               "Nicolas", "Marcela", "Gonzalo", "Renata", "Tomas", "Victoria", "Mauricio", "Camila", "Benjamin",
               "Catalina", "Gabriel", "Daniela", "Ricardo", "Isabela", "Sebastian", "Antonella", "Rodrigo",
               "Alexa", "Ignacio", "Valentina", "Mateo", "Julieta", "Manuel", "Paulina", "Andres", "Regina",
               "Esteban", "Brenda", "Mario", "Melissa", "Cristian", "Paola", "Simon", "Laura", "Oscar",
               "Estefania", "Arturo", "Fabiana", "Edgar", "Florencia", "Samuel", "Juliana", "Raul", "Elisa",
               "Francisco", "Gabriela", "Angel", "Natalia", "Diego", "Paula", "Jose Luis", "Mariana", "Maximiliano",
               "Monica", "Eduardo", "Adriana", "Alejandro", "Veronica", "Pablo", "Ximena", "Oliver", "Esmeralda",
               "Joel", "Isabel", "Victor", "Raquel", "Marcos", "Rosa", "Rafael", "Marisol", "Damian", "Patricia",
               "Fabian", "Jennifer", "Leandro", "Carmen", "Miguel-Angel", "Emily", "Matias", "Silvia", "Edwin",
               "Johana", "Augusto", "Daniella", "Lucas", "Alma", "Marco", "Alina", "Gustavo", "Elena",
               "Leonardo", "Isidora", "Iker", "Alejandra", "Oliver", "Angelica", "Ramon", "Lorena", "Lorenzo",
               "Michelle","Pablo", "Veronica", "Mateo", "Diana", "Sebastian", "Karen", "Rodrigo", "Alexandra", "Nicolas", "Cecilia",
                "Renata", "Ramon", "Monica", "Esteban", "Patricia", "Ignacio", "Gabriel", "Cristina", "Angel", "Ines",
                "Olivia", "Mara", "Emmanuel", "Alma", "Samuel", "Alicia", "Arturo", "Ximena", "Maximiliano", "Sara",
                "Benjamin", "Emily", "Salvador", "Isabel", "Ruben", "Esmeralda", "Hector", "Jennifer", "Damian",
                "Marisol", "Mauricio", "Paulina", "Agustin", "Luciana", "Ezequiel", "Gabrielle", "Matias", "Valerie",
                "Bruno", "Olga", "Sebastiana", "Joaquin", "Carla", "Marcos", "Florencia", "Facundo", "Rene", "Santiago",
                "Samanta", "Melanie", "Daniel", "Teresa", "Lorenzo", "Regina", "Jaime", "Teodoro", "Blanca",
                "Orlando", "Soledad", "Elena", "Cesar", "Antonia", "Martha", "Octavio", "Beatriz", "Gustavo",
                "Raquel", "Leonardo", "Hernan", "Natalie", "Federico", "Jimena", "Renato", "Aurora", "Miranda",
                "Estefania", "Fabiana", "Edgar", "oscar", "Elisa", "Jose Luis", "Mariana", "Alejandro",
                "Oliver", "Victor", "Rafael", "Pedro", "Ivan", "Alvaro", "Ernesto", "Nelson", "Gael"]

    apellidos = ["Gomez", "Lopez", "Rodriguez", "Perez", "Martinez", "Garcia", "Hernandez", "Fernandez",
                 "Gonzalez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera", "Vargas", "Ruiz", "Diaz",
                 "Reyes", "Morales", "Ortega", "Castillo", "Chavez", "Mendoza", "Delgado", "Silva", "Rojas",
                 "Jimenez", "Navarro", "Cruz", "Valenzuela", "Rios", "Gutierrez", "Romero", "Vega", "Guerrero",
                 "alvarez", "Montes", "Salazar", "Acosta", "Barrera", "Peña", "Cabrera", "Molina", "Soto", "Campos",
                 "Ibarra", "Vera", "Peralta", "Figueroa", "Escobar", "Araya", "Lara", "Aguilar", "Miranda",
                 "Sepulveda", "Contreras", "Luna", "Olivares", "Avila", "Espinoza", "Cortes", "Herrera", "Ponce",
                 "Zuñiga", "Caceres", "Fuentes", "Bravo", "Guzman", "Tapia", "Vasquez", "Parra", "Pizarro",
                 "Paredes", "Carvajal", "Carrasco", "Valdes", "Abarca", "Vidal", "Venegas", "Andrade", "Alarcon",
                 "Aravena", "Bustos", "Bello", "Cisternas", "Cifuentes", "Duarte", "Estrada", "Gallardo", "Godoy",
                 "Hidalgo", "Ibacache", "Inostroza", "Jara", "Leiva", "Lira", "Muñoz", "Mella", "Navarro", "Lagos",
                 "Alvarado", "Sandoval", "Moreno", "Rivas", "Cordero", "Valencia", "Villalobos", "Palacios", "Mora",
                 "Castañeda", "Trujillo", "Salas", "Camacho", "Medina", "Leon", "Reyna", "Hurtado", "Vallejo",
                 "Montenegro", "Olivera", "Cespedes", "Nieto", "Rosales", "Pantoja", "Toro", "Mendez", "Garrido",
                 "Ortiz", "Lemus", "Cornejo", "Caro", "Valdez", "Saez", "Riquelme", "Villanueva", "Carmona",
                 "Velasco", "Bustamante", "Carrillo", "Castro","Santos", "Mendoza", "Cortez", "Roldan", "Bermudez", "Ochoa", "Mejia", "Lara",
                "Rojas", "Benitez", "avila", "Castañeda", "Villalpando", "Maldonado", "Cardozo",
                "Gongora", "Salinas", "Miramontes", "Escamilla", "Palma", "Chavez", "Villanueva",
                "Navarrete", "Baez", "Valle", "Echeverria", "Arredondo", "Orozco", "Villagran",
                "Zambrano", "Ordoñez", "Vera", "Figueroa", "Pantoja", "Luna", "Padilla", "Gallardo",
                "Moreno", "Guzman", "Guerrero", "Sotelo", "Duarte", "Trujillo", "Escalante", "Laguna",
                "Leon", "Soria", "Almanza", "Carbajal", "Vega", "Montalvo", "Zamora", "Alvarez",
                "Santillan", "Beltran", "Cardenas", "Aguilera", "Leiva", "Cuevas", "Uribe", "Narvaez",
                "Barrera", "Ayala", "Perez", "Urrutia", "Cordova", "Galarza", "Rojas", "Barreto",
                "Villaseñor", "Ferrer", "Peralta", "Diaz", "Cordoba", "Calderon", "Maldonado", "Solano",
                "Jaime", "Gamez", "Juarez", "Molina", "Mendez", "Escobar", "Campos", "Angeles",
                "Burgos", "Colin", "Miranda", "Morales", "Zavala", "Arteaga", "Chavez", "Solis",
                "Molina", "Zamudio", "Nava", "Pizarro", "Tovar", "Herrera", "Medina", "Ortega",
                "Ramos", "Calzada", "Pacheco", "Guevara", "Serrano", "Navarro", "Rios", "Villanueva",
                "Fierro", "Calderon", "Valencia", "Galvan", "Marin", "Zuñiga", "Tirado", "Jimenez"]
    
    #para que los nombres y apellidos sean unicos en la lista
    nombres = list(set(nombres))
    apellidos = list(set(apellidos))
    tuplas = []
    
    #generamos las tuplas
    for _ in range(n):
        nombre = random.choice(nombres)
        apellido1 = random.choice(apellidos)
        apellido2 = random.choice(apellidos)
        fecha_nacimiento = generar_fecha()
        telefono = "9" + str(generar_telefono(tuplas))
        dni = generar_dni(tuplas)

        tupla = (nombre, apellido1, apellido2, fecha_nacimiento, telefono, dni)
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
    dni = random.randint(10000000, 99999999)  # Generar un DNI aleatorio de 8 dígitos

    # Verificar si el DNI ya existe en las tuplas
    while any(dni == t[0] for t in tuplas):
        dni = random.randint(10000000, 99999999)  # Generar un nuevo DNI aleatorio si ya existe
    return dni

tuplas_generadas = set()  # Utilizamos un conjunto para evitar repeticiones

while len(tuplas_generadas) < 1000000:
    tuplas_generadas.update(generar_tuplas(1000000 - len(tuplas_generadas)))

with open("tablas_tuplas/pacientes/paciente.csv", "a") as archivo:
    for tupla in tuplas_generadas:
        nombre, apellido1, apellido2, fecha_nacimiento, telefono, dni = tupla
        email = f"{nombre.lower()}.{apellido1.lower()}.{apellido2.lower()}@hotmail.com"
        linea = f"{nombre},{apellido1},{apellido2},{fecha_nacimiento},{telefono},{dni},{email}\n"
        archivo.write(linea)

print("Archivo generado exitosamente")