from flask import Flask, render_template
import psycopg2
from flask import jsonify, request

app = Flask(__name__)
app.config['DATABASE'] = {
    'host': 'localhost',
    'port': 5432,
    'database': 'postgres',
    'user': 'postgres',
    'password': 'china',
    'schema': 'clinica'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar_citas_route():
    try:
        if request.method == 'GET':
            # Manejar la solicitud GET aquí
            return "Método GET permitido para la ruta /buscar"
        elif request.method == 'POST':
            fecha = request.form.get('date')
            departamento = request.form.get('departament')

            # Establecer la conexión a la base de datos
            conn = psycopg2.connect(
                host="localhost",
                database="vitasalud",
                user="postgres",
                password="china"
            )

            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()

            # Definir la consulta SQL
            sql = '''
            SELECT D.nombre, D.apellido, D.apellido_materno, H.dia, H.hora_inicio, H.hora_fin, D.especialidad, H.estado
            FROM doctores D
            JOIN horario H ON D.Codigo = H.doctor_codigo
            WHERE CASE H.dia
                    WHEN 'Lunes' THEN 1
                    WHEN 'Martes' THEN 2
                    WHEN 'Miercoles' THEN 3
                    WHEN 'Jueves' THEN 4
                    WHEN 'Viernes' THEN 5
                    WHEN 'Sabado' THEN 6
                    WHEN 'Domingo' THEN 0
                    END = EXTRACT(DOW FROM TO_DATE(%s, 'MM-DD-YYYY'))
            AND D.especialidad = %s;
            '''

            # Ejecutar la consulta con los datos proporcionados
            cursor.execute(sql, (fecha, departamento))

            # Obtener los resultados de la consulta
            resultados = cursor.fetchall()

            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

            # Devolver los resultados como una respuesta JSON
            return render_template('resultados.html', resultados=resultados)

    except psycopg2.Error as e:
        # Capturar la excepción de psycopg2 y devolver una respuesta de error
        error_message = str(e)
        return "Error en la base de datos: {}".format(error_message), 500

    except Exception as e:
        # Capturar cualquier otra excepción y devolver una respuesta de error
        error_message = str(e)
        return "Error en la aplicación: {}".format(error_message), 500

if __name__ == '__main__':
    app.run(debug=True)
