from flask import Flask, redirect, render_template, session 
import psycopg2
from flask import jsonify, request
import pdb
from datetime import datetime
from flask import flash
from models.pacientes import Paciente



app = Flask(__name__)
#set up secret key
app.secret_key ='super secret key'
app.config['DATABASE'] = {
    'host': '127.0.0.1',
    'port': 5432,
    'database': 'postgres',
    'user' : "postgres",
    'password': 'china'
}

@app.route('/')
def index():
   

    return render_template('index.html')

@app.route('/agendar-cita', methods=['GET'])
def load_agendar():
    return render_template('agenda_cita.html')

def get_day_name(date_string):
    # Parse the date string into a datetime object
    date = datetime.strptime(date_string, '%Y-%m-%d')
    
    # Get the name of the day
    day_name = date.strftime('%A')

    # Dictionary mapping English day names to Spanish
    day_names_spanish = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miercoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sabado',
        'Sunday': 'Domingo'
    }

    # Get the corresponding Spanish day name from the dictionary
    day_name_spanish = day_names_spanish.get(day_name)

    return day_name_spanish


@app.route('/agendar-cita', methods=['POST'])
def send_agendar():

    date = request.form['date']
    especialidad = request.form['department']
    dia = get_day_name(date)
    conn = psycopg2.connect(
                host="127.0.0.1",
                port = 5432,
                dbname="postgres",
                user="postgres",
                password="china"
            )

    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    query = '''
            SELECT D.nombre, D.apellido, D.apellido_materno, H.dia, H.hora_inicio, H.hora_fin, D.especialidad, H.estado
            FROM clinica.doctores D
            JOIN clinica.horario H ON D.Codigo = H.doctor_codigo
            WHERE H.dia = %s
            AND D.especialidad = %s
            order by D.codigo, H.hora_inicio; '''

    cursor.execute(query,(dia,especialidad))
    resultados = cursor.fetchall()
    
    pdb.set_trace()

    return render_template('resultados_citas.html', date=date, especialidad=especialidad, resultados = resultados)

# @app.route('/agendar-cita/<date>/<especialidad>', methods=['GET'])
# def load_agendar2(date, especialidad):
#     pdb.set_trace()

#     date = '2023-01-01'
#     especialidad = 'Medicina General'

#     resultados = [[1,2,3,4,4],2,3,4,5,6,7,7,8,5]
#     pdb.set_trace()

#     return render_template('resultados_citas.html', date=date, especialidad=especialidad, resultados = resultados)


@app.route('/home-paciente')
def citas_agendadas_route():
    paciente = Paciente.get(session['user']['dni'])
    if 'user' not in session or session['user'] == None:
        return redirect('/register')
    # dni = session['user']['dni']
    # citas = Citas.get_by_dni(dni)
    # recetas = Recetas.get_by_dni(dni)
    return render_template('home_paciente.html', paciente = paciente)#, citas = citas, recetas = recetas

@app.route('/login-paciente')
def show_login():
    return render_template('login_patient.html')


@app.route('/register')
def register_paciente():
    return render_template('register.html')


@app.route('/register', methods=["POST"])
def register_paciente_post():
    if Paciente.email_free(request.form):
        paciente = Paciente.create(request.form)
        session['user'] = {
            'dni' : paciente.dni,
            'nombre': paciente.nombre,
            'apellido': paciente.apellido,  
            'telefono': paciente.telefono,
            'email': paciente.email
        }
        return redirect('/home-paciente')
    else: 
        flash("El correo ya existe", 'error')
        return redirect('/register')

def register_paciente_post(): #hacer que el si el dni ya existe te salga un error
    dni = request.form['dni']
    if Paciente.exists(dni):
        flash("Usted ya está registrado", 'error')
        return redirect('/register')
    else:
        paciente = Paciente.create(request.form)
        session['user']['dni'] = paciente.dni
        return redirect('/citas-agendadas')

@app.route('/login-paciente',methods=["POST"])
def login_paciente():
    paciente = Paciente.login(request.form)
    if paciente:
        session['user'] = paciente
        return redirect('/citas-agendadas')
    else:
        flash("Error de autenticacion",'error')
        return redirect('/login-paciente')










# @app.route('/buscar', methods=['GET', 'POST'])
# def buscar_citas_route():
#     try:
#         if request.method == 'GET':
#             # Manejar la solicitud GET aquí
#             return "Método GET permitido para la ruta /buscar"
#         elif request.method == 'POST':
#             fecha = request.form.get('date')
#             departamento = request.form.get('departament')

#             # Establecer la conexión a la base de datos
#             conn = psycopg2.connect(
#                 host="localhost",
#                 port = 5432,
#                 database="postgres",
#                 schema="clinica"
#             )

#             # Crear un cursor para ejecutar consultas
#             cursor = conn.cursor()

#             # Definir la consulta SQL
#             sql = '''
#             SELECT D.nombre, D.apellido, D.apellido_materno, H.dia, H.hora_inicio, H.hora_fin, D.especialidad, H.estado
#             FROM doctores D
#             JOIN horario H ON D.Codigo = H.doctor_codigo
#             WHERE CASE H.dia
#                     WHEN 'Lunes' THEN 1
#                     WHEN 'Martes' THEN 2
#                     WHEN 'Miercoles' THEN 3
#                     WHEN 'Jueves' THEN 4
#                     WHEN 'Viernes' THEN 5
#                     WHEN 'Sabado' THEN 6
#                     WHEN 'Domingo' THEN 0
#                     END = EXTRACT(DOW FROM TO_DATE(%s, 'MM-DD-YYYY'))
#             AND D.especialidad = %s;
#             '''

#             # Ejecutar la consulta con los datos proporcionados
#             cursor.execute(sql, (fecha, departamento))

#             # Obtener los resultados de la consulta
#             resultados = cursor.fetchall()

#             # Cerrar el cursor y la conexión
#             cursor.close()
#             conn.close()

#             # Devolver los resultados como una respuesta JSON
#             return render_template('resultados.html', resultados=resultados)

#     except psycopg2.Error as e:
#         # Capturar la excepción de psycopg2 y devolver una respuesta de error
#         error_message = str(e)
#         return "Error en la base de datos: {}".format(error_message), 500

#     except Exception as e:
#         # Capturar cualquier otra excepción y devolver una respuesta de error
#         error_message = str(e)
#         return "Error en la aplicación: {}".format(error_message), 500

if __name__ == '__main__':
    app.run(debug=True)