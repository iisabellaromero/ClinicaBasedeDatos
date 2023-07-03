from flask import Flask, redirect, render_template, session 
import psycopg2
from flask import jsonify, request
import pdb
from datetime import datetime
from flask import Flask, redirect, render_template, session 
import psycopg2
import ast
from datetime import datetime, time
from models.medicamentos import Medicamento


conn = psycopg2.connect(
                host="localhost",
                port = 5432,
                dbname="postgres"
            )

    # Crear un cursor para ejecutar consultas
cursor = conn.cursor()
            # Crear un cursor para ejecutar consultas

class Receta:
    def __init__(self,data):
        self.codigo = data[0]
        self.fecha  = data[1]
        self.doctor_codigo = data[2]
        self.paciente_dni  = data[3]

    @classmethod
    def get(cls,dni):
        paciente_dni = dni
        query='''SELECT * FROM clinica.recetas where paciente_dni = %s;'''  
        cursor.execute(query,(paciente_dni,))
        resultados = cursor.fetchall()
        print(resultados)
        receta = cls(resultados[0])
        receta.medicamentos = Receta.get_medicamentos(resultados[0][0])
        return receta

    @classmethod
    def get_medicamentos(cls,codigo):
        query='''SELECT * FROM clinica.medicamentos_recetados where receta_codigo = %s;'''  
        cursor.execute(query,(dni,))
        resultados = cursor.fetchall()
        medicamentos = []
        for resultado in resultados:
            medicamento = Medicamento(resultado)
            medicamentos.append(medicamento)
        return medicamentos