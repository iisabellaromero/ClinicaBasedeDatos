from flask import Flask, redirect, render_template, session 
import psycopg2
from flask import jsonify, request
import pdb
from datetime import datetime
from flask import Flask, redirect, render_template, session 
import psycopg2

conn = psycopg2.connect(
                host="localhost",
                port = 5432,
                dbname="postgres"
            )
            # Crear un cursor para ejecutar consultas
cursor = conn.cursor()


class Paciente:
    def __init__(self,data):
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.apellido_materno = data['apellido_materno']
        self.email = data['email']
        self.fecha = data['fecha_nacimiento']
        self.dni = data['dni']
    #Validacion del registro
    @staticmethod
    def validate_user(form_data):
        is_valid = True
        if len(form_data['full_name']) <4:
            flash("Name must be at least 4 characters.",'error')
            is_valid = False
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!",'error')
            is_valid = False
        if len(form_data['password']) < 8:
            flash("Password must be at least 8 characters.",'error')
            is_valid = False
        if form_data["password"] != form_data["confirm_password"]:
            flash('Passwords must match!','error')
            is_valid = False
        if is_valid == True:
            flash('Valid credentials! Please fill in aditional info', 'info')
        return is_valid

    #Verifica que el correo de registro este o no en la base de datos
    @classmethod
    def email_free(cls,form_data):
        
        query = '''
                SELECT * FROM clinica.pacientes where email = %s;'''

        email  = form_data['email']
        pdb.set_trace()
        cursor.execute(query,(email))
        resultados = cursor.fetchall()
        #Si existe algo en resultados return true, si se puede usar ese email 
        if resultados:
            return False
        else:
            return True

    @classmethod
    def create(cls,form_data):
        query = '''
                INSERT INTO clinica.pacientes (nombre, apellido, apellido_materno, email, fecha_nacimiento, dni, password)
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;'''
        cursor.execute(query,(form_data['nombre'],form_data['apellido'],form_data['apellido_materno'],form_data['email'],form_data['fecha_nacimiento'],form_data['dni']))
        conn.commit()
        return True
    
    