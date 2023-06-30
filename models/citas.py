from flask import Flask, redirect, render_template, session 
import psycopg2
from flask import jsonify, request
import pdb
from datetime import datetime
from flask import Flask, redirect, render_template, session 
import psycopg2
import ast
from datetime import datetime, time


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
        self.nombre = data[0]
        self.apellido = data[1]
        self.doctor_codigo = data[2]
        self.hora_inicio = data[3]
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
    def insert(cls,data):
        return None
