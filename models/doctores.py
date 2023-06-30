from flask import Flask, redirect, render_template, session 
import psycopg2
from flask import jsonify, request
import pdb
from datetime import datetime
from flask import Flask, redirect, render_template, session 
import psycopg2
from models.horarios import Horario

conn = psycopg2.connect(
                host="localhost",
                port = 5432,
                dbname="postgres"
            )

    # Crear un cursor para ejecutar consultas
cursor = conn.cursor()
            # Crear un cursor para ejecutar consultas


class Doctor:
    def __init__(self,data):
        self.codigo = data[0]
        self.codigo_cmp = data[1]
        self.nombre = data[2]
        self.apellido = data[3]
        self.apellido_materno = data[4]
        self.fecha = data[5]
        self.telefono = data[6]
        self.dni = data[7]
        self.email = data[8]
        self.especialidad = data[9]
 
    @classmethod
    def get_especialidades(cls):
        query='''SELECT DISTINCT especialidad FROM clinica.doctores;'''  
        cursor.execute(query)
        resultados = cursor.fetchall()
        especialidades = []
        for resultado in resultados: 
            especialidades.append(resultado[0])
        return especialidades

    @classmethod 
    def horarios_filtro(cls, especialidad,dia):
        query='''select * from clinica.Horarios_Doctores
                where doctor_codigo in 
                (select codigo from clinica.doctores where especialidad = %s)
                and dia = %s;'''  
        cursor.execute(query,(especialidad,dia,))
        resultados = cursor.fetchall()
        horarios = []
        for resultado in resultados:
            horario = Horario(resultado)
            horarios.append(horario)

        return horarios

    @classmethod
    def get(cls,codigo):
        query='''SELECT * FROM clinica.doctores where codigo = %s;'''  
        cursor.execute(query,(codigo,))
        resultados = cursor.fetchall()
        pdb.set_trace()
        print(resultados)
        return cls(resultados[0])
        
    