from flask import Flask
import psycopg2

app = Flask(__name__)
app.config['DATABASE'] = {
    'host': 'localhost',
    'port': 5432,
    'database': 'vitasalud',
    'user': 'postrgres',
    'password': 'china'
}

@app.before_first_request
def connect_to_database():
    conn = psycopg2.connect(
        host=app.config['DATABASE']['host'],
        port=app.config['DATABASE']['port'],
        database=app.config['DATABASE']['database'],
        user=app.config['DATABASE']['user'],
        password=app.config['DATABASE']['password']
    )
    app.config['DATABASE_CONNECTION'] = conn

class Doctor:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="vitasalud",
            user="postgres",
            password="china"
        )
        self.cursor = self.conn.cursor()
    
def get_doctors(self):
    self.cursor.execute("SELECT * FROM doctor")
    return self.cursor.fetchall()

@app.route('/')
def index():
    return 'Hello World!'
