from flask import Flask, redirect, render_template, session ,flash
import psycopg2
from flask import jsonify, request
import pdb
from datetime import datetime
from flask import flash
from models.pacientes import Paciente
from models.doctores import Doctor
from models.citas import Cita



app = Flask(__name__)
#set up secret key
app.secret_key ='super secret key'
app.config['DATABASE'] = {
    'host': 'localhost',
    'port': 5432,
    'database': 'postgres'
}

@app.route('/')
def index():
   

    return render_template('index.html')

@app.route('/agendar-cita', methods=['GET'])
def load_agendar():
    if 'user' not in session or session == None: 
        flash("Debes iniciar sesion para sacar una cita", 'Error')
        return redirect('/register')
    especialidades = Doctor.get_especialidades()
    return render_template('agenda_cita.html', especialidades=especialidades)

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
    resultados = Doctor.horarios_filtro(especialidad,dia)
    return render_template('resultados_citas.html', resultados = resultados, date=date, esp = especialidad)


@app.route('/confirmacion-cita', methods = ['POST'])
def confirmacion_cita():
    values = request.form['doctor']
    values = values.split(',')
    dict_create = {
        'doctor_codigo' : values[0],
        'hora_inicio' : values[1],
        'dia' : values[2],
        'fecha' : values[3],
        'paciente_dni' : session['user']['dni']
    }
    cita = Cita.create(dict_create)
    doctor = Doctor.get(cita.doctor_codigo)
    paciente = Paciente.get(session['user']['dni'])
    
    return render_template('cita_confirmada.html', cita = cita, doctor = doctor, paciente = paciente)


@app.route('/home-paciente')
def citas_agendadas_route():
    if 'user' not in session or session['user'] == None:
        return redirect('/register')
    # dni = session['user']['dni']
    paciente = Paciente.get(session['user']['dni'])
    citas = Cita.get_by_dni(session['user']['dni'])
    # recetas = Recetas.get_by_dni(dni)
    return render_template('home_paciente.html', paciente = paciente, citas = citas) #recetas = recetas

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
        return redirect('/')

@app.route('/login-paciente',methods=["POST"])
def login_paciente():
    paciente = Paciente.login(request.form)
    if paciente:
        session['user'] = paciente
        return redirect('/citas-agendadas')
    else:
        flash("Error de autenticacion",'error')
        return redirect('/login-paciente')



if __name__ == '__main__':
    app.run(debug=True)