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
            # Crear un cursor para ejecutar consultas


class Paciente:
    def __init__(self,data):
        self.nombre = data[0]
        self.apellido = data[1]
        self.apellido_materno = data[2]
        self.fecha = data[3]
        self.telefono = data[4]
        self.dni = data[5]
        self.email = data[6]


    #Verifica que el correo de registro este o no en la base de datos
    @classmethod
    def email_free(cls,form_data):
        query = '''
                SELECT * FROM clinica.pacientes where email = %s;'''

        email  = form_data['email']
        cursor.execute(query,(email,))
        resultados = cursor.fetchall()
        #Si existe algo en resultados return true, si se puede usar ese email 
        if resultados:
            return False
        else:
            return True

    @classmethod
    def create(cls,form_data):
        query = '''
                INSERT INTO clinica.pacientes (nombre, apellido, apellido_materno,telefono, email, fecha_nacimiento, dni)
                VALUES (%s, %s, %s, %s, %s,%s, %s) RETURNING dni;'''
        cursor.execute(query,(form_data['nombre'],form_data['apellido'],form_data['apellido_materno'],form_data['telefono'],form_data['email'],form_data['fecha_nacimiento'],form_data['dni']))
        conn.commit()
        #return dni
        pdb.set_trace()
        obj = cls.get(form_data['dni'])


        return obj
   

    @classmethod
    def get(cls,dni):
        query='''SELECT * FROM clinica.pacientes where dni = %s;'''  
        pdb.set_trace()
        cursor.execute(query,(dni,))
        resultados = cursor.fetchall()
        print(resultados)
        pdb.set_trace()
        return cls(resultados[0])
        
    