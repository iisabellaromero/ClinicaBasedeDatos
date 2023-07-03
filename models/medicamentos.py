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

class Medicamento:
    def __init__(self,data):
        self.receta_codigo = data[0]
        self.medicamento_codigo = data[1]
        self.nombre_medicamento = data[2]
        self.cantidad = data[3]
        self.precio_regular = data[4]
        self.precio_deducible = data[5]

   
