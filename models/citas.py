from flask import Flask, redirect, render_template, session 
import psycopg2
from flask import jsonify, request
import pdb
from datetime import datetime
from flask import Flask, redirect, render_template, session 
import psycopg2
import ast
from datetime import datetime, time
from models.doctores import Doctor


conn = psycopg2.connect(
                host="localhost",
                port = 5432,
                dbname="postgres"
            )

    # Crear un cursor para ejecutar consultas
cursor = conn.cursor()
            # Crear un cursor para ejecutar consultas

class Cita:
    def __init__(self,data):
        self.paciente_dni = data[0]
        self.fecha = data[1]
        self.hora_inicio = data[2]
        self.doctor_codigo = data[3]
        self.dia = data[4]
        self.create_pk()

    def create_pk(self):
        self.pk = {'dia':self.dia,
        'hora_inicio':self.hora_inicio,
        'doctor_codigo':self.doctor_codigo,
    }

    @classmethod
    def to_dict(cls,input_string):
        # Remove leading and trailing whitespace and single quotes
        input_string = input_string.strip().strip("'")
        
        # Convert string to dictionary using ast.literal_eval
        input_dict = ast.literal_eval(input_string)
        
        # Convert 'hora_inicio' string to datetime.time object
        input_dict['hora_inicio'] = datetime.strptime(input_dict['hora_inicio'], "%H:%M").time()
        return input_dict

    @classmethod
    def create(cls,form_data):
        query = '''
                INSERT INTO clinica.citas (paciente_dni,fecha,hora_inicio,doctor_codigo,dia)
                VALUES (%s,%s,%s,%s,%s) RETURNING paciente_dni,fecha,hora_inicio,doctor_codigo,dia;'''

        doctor_codigo = form_data['doctor_codigo']
        hora_inicio = form_data['hora_inicio']
        dia = form_data['dia']
        fecha = form_data['fecha']
        paciente_dni = form_data['paciente_dni']
        cursor.execute(query,(paciente_dni,fecha,hora_inicio,doctor_codigo,dia,))
        conn.commit()
        #return what returns from the query
        obj = cursor.fetchone()
        cita = cls(obj)
        return cita

    @classmethod
    def get_by_dni(cls,paciente_dni):

        query='''SELECT * FROM clinica.citas where paciente_dni = %s;'''  
        cursor.execute(query,(paciente_dni,))
        resultados = cursor.fetchall()
        citas = []
        for resultado in resultados:
            cita = cls(resultado)
            cita.doctor = Doctor.get(cita.doctor_codigo)
            citas.append(cita)
        return citas

    @classmethod
    def delete(cls,dni,doctor_codigo,fecha,hora_inicio):
        dni = int(dni)
        query='''Delete FROM clinica.citas where paciente_dni = %s and doctor_codigo = %s and fecha = %s and hora_inicio = %s;'''  
        cursor.execute(query,(dni,doctor_codigo,fecha,hora_inicio,))
        conn.commit()  # Explicitly commit the changes

        return True