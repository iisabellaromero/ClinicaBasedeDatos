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

class Horario:
    def __init__(self,data):
        self.nombre = data[0]
        self.apellido = data[1] 
        self.doctor_codigo = data[2]
        self.hora_inicio = data[3]
        self.dia = data[4]