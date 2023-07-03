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
                dbname="postgres",
                user = "postgres",
                password = "china"
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
        obj = cls.get(form_data['dni'])
        return obj
   

    @classmethod
    def get(cls,dni):
        query='''SELECT * FROM clinica.pacientes where dni = %s;'''  
        cursor.execute(query,(dni,))
        resultados = cursor.fetchall()
        print(resultados)
        return cls(resultados[0])
    
    @staticmethod
    def exists(dni):
        conn = psycopg2.connect(
            host="127.0.0.1",
            port=5432,
            dbname="postgres",
            password="china",
        )
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM pacientes WHERE dni = %s"
        cursor.execute(query, (dni,))
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return count > 0
        
    @classmethod
    def login(cls, dni, email):
        persona = cls.get(dni)
        if persona.email == email:
            return persona

    @classmethod
    def edit(cls,form_data,dni):
        query = '''
                UPDATE clinica.pacientes SET nombre = %s, apellido = %s, apellido_materno = %s, telefono = %s, email = %s, fecha_nacimiento = %s
                WHERE dni = %s;'''
        cursor.execute(query,(form_data['nombre'],form_data['apellido'],form_data['apellido_materno'],form_data['telefono'],form_data['email'],form_data['fecha_nacimiento'],dni,))
        conn.commit()
        obj = cls.get(dni)
        return obj