-- Schema clinica
CREATE SCHEMA IF NOT EXISTS clinica;

-- set search path clinica schema
SET search_path = clinica;
drop table if exists consultorio;
DROP TABLE IF EXISTS recetas_aprobadas;
DROP TABLE IF EXISTS medicamentos_recetados;
DROP TABLE IF EXISTS recetas;
DROP TABLE IF EXISTS Citas;
DROP TABLE IF EXISTS asegurados;
DROP TABLE IF EXISTS Poliza;
DROP TABLE IF EXISTS Seguro;
DROP TABLE IF EXISTS pacientes;
DROP TABLE IF EXISTS Horario;
DROP TABLE IF EXISTS farmacistas;
DROP TABLE IF EXISTS doctores;
DROP TABLE IF EXISTS Oficina;
DROP TABLE IF EXISTS turnos;
DROP TABLE IF EXISTS medicamento;


-- Tabla doctores DONE
CREATE TABLE IF NOT EXISTS doctores (
      Codigo VARCHAR(5) NOT NULL,
      Codigo_cmp VARCHAR(6) NOT NULL,
      Nombre VARCHAR(45) NOT NULL,
      Apellido VARCHAR(255) NOT NULL,
      Apellido_materno VARCHAR(255) NOT NULL,
      Fecha_nacimiento DATE NOT NULL,
      Telefono VARCHAR(9) NOT NULL,
      DNI INT NOT NULL,
      Email VARCHAR(255) NOT NULL,
      PRIMARY KEY (Codigo)
);

-- Tabla Consultorio DONE
CREATE TABLE IF NOT EXISTS Consultorio (
    doctor_codigo VARCHAR(5) NOT NULL,
    numero VARCHAR(4) NOT NULL,
    PRIMARY KEY (numero),
    constraint fk_doctor
    FOREIGN KEY (doctor_codigo)
      REFERENCES doctores (Codigo)
      ON DELETE CASCADE
      ON UPDATE CASCADE
  );

-- Tabla farmacistas DONE
CREATE TABLE IF NOT EXISTS farmacistas (
      Codigo VARCHAR(5) NOT NULL,
      Nombre VARCHAR(45) NOT NULL,
      Apellido VARCHAR(255) NOT NULL,
      Apellido_materno VARCHAR(255) NOT NULL,
      Fecha_nacimiento DATE NOT NULL,
      Telefono INT NULL,
      DNI VARCHAR(9) NOT NULL,
      Email VARCHAR(255) NOT NULL,
      PRIMARY KEY (Codigo)
);

-- Tabla Horario DONE                                 
CREATE TABLE IF NOT EXISTS Horario (
        Dia VARCHAR(9) NOT NULL,
        Hora_inicio TIMESTAMP NOT NULL,
        Hora_fin TIMESTAMP NOT NULL,
        doctor_codigo VARCHAR(5) NOT NULL,
        Estado BOOLEAN NOT NULL DEFAULT TRUE,
        PRIMARY KEY (Hora_fin, Hora_inicio, doctor_codigo),
        CONSTRAINT fk_horario_doctores
            FOREIGN KEY (doctor_codigo)
                REFERENCES doctores (Codigo)
                ON DELETE CASCADE
                ON UPDATE CASCADE
);


-- Tabla pacientes DONE                                 
CREATE TABLE IF NOT EXISTS pacientes (
      Nombre VARCHAR(45) NOT NULL,
      Apellido VARCHAR(255) NOT NULL,
      Apellido_materno VARCHAR(255) NOT NULL,
      Fecha_nacimiento DATE NOT NULL,
      Telefono VARCHAR(9) NOT NULL,
      DNI INT NOT NULL,
      Email VARCHAR(255) NOT NULL,
      PRIMARY KEY (DNI)
);

-- Tabla Seguro DONE                                 
CREATE TABLE IF NOT EXISTS Seguro (
      Id INT NOT NULL,
      Nombre INT NOT NULL,
      PRIMARY KEY (Id)
);

-- Tabla Poliza DONE                                 
CREATE TABLE IF NOT EXISTS Poliza (
      Seguro_Id INT NOT NULL,
      ID INT NOT NULL,
      Nombre VARCHAR(255) NOT NULL,
      Cobertura INT NOT NULL,
      PRIMARY KEY (ID, Seguro_Id),
      CONSTRAINT fk_poliza_seguro
          FOREIGN KEY (Seguro_Id)
              REFERENCES Seguro (Id)
              ON DELETE CASCADE
              ON UPDATE CASCADE
);


-- Tabla asegurados DONE                                 
CREATE TABLE IF NOT EXISTS asegurados (
      paciente_dni INT NOT NULL,
      poliza_id INT NOT NULL,
      seguro_id INT NOT NULL,
      PRIMARY KEY (paciente_dni),
      CONSTRAINT fk_asegurados_pacientes
          FOREIGN KEY (paciente_dni)
              REFERENCES pacientes (DNI)
              ON DELETE CASCADE
              ON UPDATE CASCADE,
      CONSTRAINT fk_asegurados_poliza
          FOREIGN KEY (poliza_id, seguro_id)
              REFERENCES Poliza (ID, Seguro_Id)
              ON DELETE CASCADE
              ON UPDATE CASCADE
);



-- Tabla Citas DONE                                 
CREATE TABLE IF NOT EXISTS Citas (
      fecha DATE NOT NULL,
      Hora_inicio TIMESTAMP NOT NULL,
      Hora_fin TIMESTAMP NOT NULL,
      doctor_codigo VARCHAR(5) NOT NULL,
      especialidad VARCHAR(45) NOT NULL,
      paciente_dni INT NOT NULL,
      consultorio VARCHAR(4) NOT NULL,
      precio INT DEFAULT 200,
      precio_deducible INT DEFAULT 200,
      PRIMARY KEY (fecha,doctor_codigo,paciente_dni),
      CONSTRAINT unique_cita_time UNIQUE (doctor_codigo, fecha, Hora_inicio, Hora_fin),
      CONSTRAINT fk_citas_horario
          FOREIGN KEY (Hora_fin, Hora_inicio, doctor_codigo)
              REFERENCES Horario (Hora_fin, Hora_inicio, doctor_codigo)
              ON DELETE CASCADE
              ON UPDATE CASCADE,
      CONSTRAINT fk_citas_pacientes
          FOREIGN KEY (paciente_dni)
              REFERENCES pacientes (DNI)
              ON DELETE CASCADE
              ON UPDATE CASCADE
);

--
CREATE TABLE IF NOT EXISTS recetas (
      Codigo INT NOT NULL,
      fecha DATE NOT NULL,
      Doctor_codigo VARCHAR(5) NOT NULL,
      paciente_dni INT NOT NULL,
      PRIMARY KEY (Codigo),
      CONSTRAINT fk_recetas_citas
          FOREIGN KEY (fecha, Doctor_codigo, paciente_dni)
              REFERENCES Citas (fecha, doctor_codigo, paciente_dni)
              ON DELETE CASCADE
              ON UPDATE CASCADE
);

-- Tabla medicamento DONE                                 
CREATE TABLE IF NOT EXISTS medicamento (
      ID INT NOT NULL,
      Nombre VARCHAR(255) NOT NULL,
      Laboratorio VARCHAR(255) NOT NULL,
      Precio DOUBLE PRECISION NOT NULL,
      Unidad INT NOT NULL,
      Stock INT NOT NULL,
      PRIMARY KEY (ID)
);

-- Tabla medicamentos_recetados DONE                                 
CREATE TABLE IF NOT EXISTS medicamentos_recetados (
      receta_codigo INT NOT NULL,
      medicamento_codigo INT NOT NULL,
      nombre_medicamento VARCHAR(45) NOT NULL,
        cantidad INT NOT NULL,
        precio_regular double precision  not null,
        precio_deducible double precision not null,
      PRIMARY KEY (receta_codigo, medicamento_codigo),
      CONSTRAINT fk_codigo_receta
          FOREIGN KEY (receta_codigo)
              REFERENCES recetas (Codigo)
              ON DELETE CASCADE
              ON UPDATE CASCADE,
      CONSTRAINT fk_medicamento_codigo
          FOREIGN KEY (medicamento_codigo)
              REFERENCES medicamento (ID)
              ON DELETE CASCADE
              ON UPDATE CASCADE
);

-- Tabla recetas_aprobadas
CREATE TABLE IF NOT EXISTS recetas_aprobadas (
    receta_codigo INT NOT NULL,
    farmacista_codigo VARCHAR(5) NOT NULL,
    Hora TIMESTAMP NOT NULL,
    codigo_venta INT NOT NULL,
    PRIMARY KEY (codigo_venta),
    CONSTRAINT fk_recetas_aprobadas_recetas
        FOREIGN KEY (receta_codigo)
            REFERENCES recetas (codigo)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    CONSTRAINT fk_recetas_aprobadas_farmacistas
        FOREIGN KEY (farmacista_codigo)
            REFERENCES farmacistas (Codigo)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

-- Triggers 
