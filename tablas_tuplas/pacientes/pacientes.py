import random

#nombres y apellidos generados por chat gpt
def generar_tuplas(n):
    nombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Laura", "Pedro", "Sofía", "Diego", "Valentina",
               "José", "Carmen", "Manuel", "Isabella", "Miguel", "Fernanda", "Antonio", "Gabriela", "Javier",
               "Andrea", "Ricardo", "Daniela", "Francisco", "Camila", "Alejandro", "Paula", "Rafael", "Lucía",
               "Eduardo", "Mariana", "Gonzalo", "Valeria", "Roberto", "Julia", "Mario", "Natalia", "Hugo",
               "Catalina", "Fernando", "Victoria", "Alberto", "Elena", "Juan Carlos", "Marcela", "Andrés",
               "Carolina", "Emilio", "Adriana", "Raúl", "Silvia", "Emilia", "Pablo", "Verónica", "Mateo",
               "Diana", "Sebastián", "Karen", "Rodrigo", "Alexandra", "Nicolás", "Cecilia", "Renata", "Ramón",
               "Mónica", "Esteban", "Patricia", "Ignacio", "Gabriel", "Cristina", "Ángel", "Inés", "Olivia",
               "Raul", "Mara", "Emmanuel", "Alma", "Samuel", "Alicia", "Arturo", "Ximena", "Maximiliano",
               "Sara", "Benjamín", "Emily", "Salvador", "Isabel", "Rubén", "Esmeralda", "Héctor", "Jennifer",
               "Damián", "Marisol", "Mauricio", "Paulina", "Agustín", "Luciana", "Ezequiel", "Gabrielle", "Matías",
               "Valerie", "Bruno", "Olga", "Sebastiana", "Joaquín", "Carla", "Marcos", "Florencia", "Facundo",
               "René", "Santiago", "Ximena", "Samanta", "Melanie", "Daniel", "Teresa", "Lorenzo", "Regina",
               "Jaime", "Rosa", "Teodoro", "Blanca", "Orlando", "Soledad", "Elena", "Cesar", "Antonia",
               "Felipe", "Martha", "Raul", "Catalina", "Octavio", "Beatriz", "Gustavo", "Raquel", "Leonardo",
               "Hernán", "Natalie", "Federico", "Jimena", "Renato", "Aurora", "Bruno", "Miranda", "Emilio",
               "Carolina", "Iván", "Vanessa", "Roberto", "Valeria", "Héctor", "Cecilia", "Felipe", "Luciana",
               "Nicolás", "Marcela", "Gonzalo", "Renata", "Tomás", "Victoria", "Mauricio", "Camila", "Benjamín",
               "Catalina", "Gabriel", "Daniela", "Ricardo", "Isabela", "Sebastián", "Antonella", "Rodrigo",
               "Alexa", "Ignacio", "Valentina", "Mateo", "Julieta", "Manuel", "Paulina", "Andrés", "Regina",
               "Esteban", "Brenda", "Mario", "Melissa", "Cristian", "Paola", "Simón", "Laura", "Óscar",
               "Estefanía", "Arturo", "Fabiana", "Edgar", "Florencia", "Samuel", "Juliana", "Raúl", "Elisa",
               "Francisco", "Gabriela", "Ángel", "Natalia", "Diego", "Paula", "José Luis", "Mariana", "Maximiliano",
               "Mónica", "Eduardo", "Adriana", "Alejandro", "Verónica", "Pablo", "Ximena", "Oliver", "Esmeralda",
               "Joel", "Isabel", "Víctor", "Raquel", "Marcos", "Rosa", "Rafael", "Marisol", "Damián", "Patricia",
               "Fabián", "Jennifer", "Leandro", "Carmen", "Miguel Ángel", "Emily", "Matías", "Silvia", "Edwin",
               "Johana", "Augusto", "Daniella", "Lucas", "Alma", "Marco", "Alina", "Gustavo", "Elena",
               "Leonardo", "Isidora", "Iker", "Alejandra", "Óliver", "Angélica", "Ramon", "Lorena", "Lorenzo",
               "Michelle","Pablo", "Verónica", "Mateo", "Diana", "Sebastián", "Karen", "Rodrigo", "Alexandra", "Nicolás", "Cecilia",
                "Renata", "Ramón", "Mónica", "Esteban", "Patricia", "Ignacio", "Gabriel", "Cristina", "Ángel", "Inés",
                "Olivia", "Mara", "Emmanuel", "Alma", "Samuel", "Alicia", "Arturo", "Ximena", "Maximiliano", "Sara",
                "Benjamín", "Emily", "Salvador", "Isabel", "Rubén", "Esmeralda", "Héctor", "Jennifer", "Damián",
                "Marisol", "Mauricio", "Paulina", "Agustín", "Luciana", "Ezequiel", "Gabrielle", "Matías", "Valerie",
                "Bruno", "Olga", "Sebastiana", "Joaquín", "Carla", "Marcos", "Florencia", "Facundo", "René", "Santiago",
                "Samanta", "Melanie", "Daniel", "Teresa", "Lorenzo", "Regina", "Jaime", "Teodoro", "Blanca",
                "Orlando", "Soledad", "Elena", "Cesar", "Antonia", "Martha", "Octavio", "Beatriz", "Gustavo",
                "Raquel", "Leonardo", "Hernán", "Natalie", "Federico", "Jimena", "Renato", "Aurora", "Miranda",
                "Estefanía", "Fabiana", "Edgar", "Óscar", "Elisa", "José Luis", "Mariana", "Alejandro",
                "Óliver", "Víctor", "Rafael", "Pedro", "Iván", "Álvaro", "Ernesto", "Nelson", "Gael"]

    apellidos = ["Gómez", "López", "Rodríguez", "Pérez", "Martínez", "García", "Hernández", "Fernández",
                 "González", "Sánchez", "Ramírez", "Torres", "Flores", "Rivera", "Vargas", "Ruiz", "Díaz",
                 "Reyes", "Morales", "Ortega", "Castillo", "Chávez", "Mendoza", "Delgado", "Silva", "Rojas",
                 "Jiménez", "Navarro", "Cruz", "Valenzuela", "Ríos", "Gutiérrez", "Romero", "Vega", "Guerrero",
                 "Álvarez", "Montes", "Salazar", "Acosta", "Barrera", "Peña", "Cabrera", "Molina", "Soto", "Campos",
                 "Ibarra", "Vera", "Peralta", "Figueroa", "Escobar", "Araya", "Lara", "Aguilar", "Miranda",
                 "Sepúlveda", "Contreras", "Luna", "Olivares", "Avila", "Espinoza", "Cortés", "Herrera", "Ponce",
                 "Zúñiga", "Cáceres", "Fuentes", "Bravo", "Guzmán", "Tapia", "Vásquez", "Parra", "Pizarro",
                 "Paredes", "Carvajal", "Carrasco", "Valdés", "Abarca", "Vidal", "Venegas", "Andrade", "Alarcón",
                 "Aravena", "Bustos", "Bello", "Cisternas", "Cifuentes", "Duarte", "Estrada", "Gallardo", "Godoy",
                 "Hidalgo", "Ibacache", "Inostroza", "Jara", "Leiva", "Lira", "Muñoz", "Mella", "Navarro", "Lagos",
                 "Alvarado", "Sandoval", "Moreno", "Rivas", "Cordero", "Valencia", "Villalobos", "Palacios", "Mora",
                 "Castañeda", "Trujillo", "Salas", "Camacho", "Medina", "León", "Reyna", "Hurtado", "Vallejo",
                 "Montenegro", "Olivera", "Céspedes", "Nieto", "Rosales", "Pantoja", "Toro", "Méndez", "Garrido",
                 "Ortiz", "Lemus", "Cornejo", "Caro", "Valdez", "Sáez", "Riquelme", "Villanueva", "Carmona",
                 "Velasco", "Bustamante", "Carrillo", "Castro","Santos", "Mendoza", "Cortez", "Roldán", "Bermúdez", "Ochoa", "Mejía", "Lara",
                "Rojas", "Benítez", "Ávila", "Castañeda", "Villalpando", "Maldonado", "Cardozo",
                "Góngora", "Salinas", "Miramontes", "Escamilla", "Palma", "Chávez", "Villanueva",
                "Navarrete", "Báez", "Valle", "Echeverría", "Arredondo", "Orozco", "Villagrán",
                "Zambrano", "Ordoñez", "Vera", "Figueroa", "Pantoja", "Luna", "Padilla", "Gallardo",
                "Moreno", "Guzmán", "Guerrero", "Sotelo", "Duarte", "Trujillo", "Escalante", "Laguna",
                "León", "Soria", "Almanza", "Carbajal", "Vega", "Montalvo", "Zamora", "Álvarez",
                "Santillán", "Beltrán", "Cárdenas", "Aguilera", "Leiva", "Cuevas", "Uribe", "Narváez",
                "Barrera", "Ayala", "Pérez", "Urrutia", "Córdova", "Galarza", "Rojas", "Barreto",
                "Villaseñor", "Ferrer", "Peralta", "Díaz", "Córdoba", "Calderón", "Maldonado", "Solano",
                "Jaime", "Gámez", "Juárez", "Molina", "Méndez", "Escobar", "Campos", "Ángeles",
                "Burgos", "Colín", "Miranda", "Morales", "Zavala", "Arteaga", "Chávez", "Solís",
                "Molina", "Zamudio", "Nava", "Pizarro", "Tovar", "Herrera", "Medina", "Ortega",
                "Ramos", "Calzada", "Pacheco", "Guevara", "Serrano", "Navarro", "Ríos", "Villanueva",
                "Fierro", "Calderón", "Valencia", "Galván", "Marín", "Zúñiga", "Tirado", "Jiménez"]
    
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

tuplas_generadas = generar_tuplas(10000)  # Cambia el número 10 por la cantidad de tuplas que desees generar

#hice un bucle para que el archivo se corra 100 veces, ya que solo me deja generar hasta 10 mil tuplas a la vez
for _ in range(100):
    with open("paciente.txt", "a") as archivo:
        for tupla in tuplas_generadas:
            nombre, apellido1, apellido2, fecha_nacimiento, telefono, dni = tupla
            email = f"{nombre.lower()}.{apellido1.lower()}@hotmail.com"
            linea = f"{nombre}, {apellido1}, {apellido2}, {fecha_nacimiento}, {telefono}, {dni}, {email}\n"
            archivo.write(linea)

print("Archivo generado exitosamente")

