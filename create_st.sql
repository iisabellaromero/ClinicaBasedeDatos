-- Schema clinica
CREATE SCHEMA IF NOT EXISTS clinica;

-- set search path clinica schema
SET search_path = clinica;

-- Tabla turnos
CREATE TABLE IF NOT EXISTS turnos (
  Hora_inicio TIMESTAMP NOT NULL,
  Hora_fin TIMESTAMP NOT NULL,
  PRIMARY KEY (Hora_fin, Hora_inicio)
);

-- Tabla doctores
CREATE TABLE IF NOT EXISTS doctores (
  Codigo VARCHAR(5) NOT NULL,
  Nombre VARCHAR(45) NOT NULL,
  Apellido VARCHAR(255) NOT NULL,
  DNI INT NOT NULL,
  Telefono VARCHAR(9) NOT NULL,
  Especialidad VARCHAR(45) NOT NULL,
  Email VARCHAR(255) NOT NULL,
  Contrasena VARCHAR(12) NOT NULL,
  PRIMARY KEY (Codigo),
);

-- Tabla Consultorio
CREATE TABLE IF NOT EXISTS Consultorio (
  Consultorio_numero VARCHAR(4) NOT NULL,
  Codigo.doctor VARCHAR(5) NOT NULL,
  PRIMARY KEY (Consultorio)
  FOREIGN KEY (Codigo.doctor)
    REFERENCES doctores (Codigo)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Tabla farmacistas
CREATE TABLE IF NOT EXISTS farmacistas (
  Codigo VARCHAR(5) NOT NULL,
  Nombre VARCHAR(45) NOT NULL,
  Apellido VARCHAR(255) NOT NULL,
  DNI VARCHAR(9) NOT NULL,
  Telefono INT NULL,
  PRIMARY KEY (Codigo)
);

-- Tabla Horario
CREATE TABLE IF NOT EXISTS Horario (
  Hora_fin TIMESTAMP NOT NULL,
  Hora_inicio TIMESTAMP NOT NULL,
  Codigo_doctor VARCHAR(5) NOT NULL,
  Estado SMALLINT NOT NULL,
  PRIMARY KEY (Hora_fin, Hora_inicio, Codigo_doctor),
  CONSTRAINT fk_horario_turnos
    FOREIGN KEY (Hora_fin, Hora_inicio)
    REFERENCES turnos (Hora_fin, Hora_inicio)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_horario_doctores
    FOREIGN KEY (Codigo_doctor)
    REFERENCES doctores (Codigo)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Tabla pacientes
CREATE TABLE IF NOT EXISTS pacientes (
  Nombre VARCHAR(45) NOT NULL,
  Apellido VARCHAR(255) NOT NULL,
  DNI INT NOT NULL,
  Telefono INT NOT NULL,
  Email VARCHAR(255) NOT NULL,
  Edad INT NOT NULL,
  Contrasena VARCHAR(12) NOT NULL,
  PRIMARY KEY (DNI)
);

-- Tabla Seguro
CREATE TABLE IF NOT EXISTS Seguro (
  Id INT NOT NULL,
  Nombre INT NOT NULL,
  PRIMARY KEY (Id)
);

-- Tabla Poliza
CREATE TABLE IF NOT EXISTS Poliza (
  ID INT NOT NULL,
  Nombre VARCHAR(255) NOT NULL,
  Cobertura INT NOT NULL,
  Seguro_Id INT NOT NULL,
  PRIMARY KEY (ID, Seguro_Id),
  CONSTRAINT fk_poliza_seguro
    FOREIGN KEY (Seguro_Id)
    REFERENCES Seguro (Id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- Tabla asegurados
CREATE TABLE IF NOT EXISTS asegurados (
  pacientes_DNI INT NOT NULL,
  poliza_id INT NOT NULL,
  seguro_id INT NOT NULL,
  PRIMARY KEY (pacientes_DNI, poliza_id),
  CONSTRAINT fk_asegurados_pacientes
    FOREIGN KEY (pacientes_DNI)
    REFERENCES pacientes (DNI)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_asegurados_poliza
    FOREIGN KEY (poliza_id, seguro_id)
    REFERENCES Poliza (ID, Seguro_Id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);



-- Tabla Citas
CREATE TABLE IF NOT EXISTS Citas (
  Hora_fin TIMESTAMP NOT NULL,
  Hora_inicio TIMESTAMP NOT NULL,
  doctor_codigo VARCHAR(5) NOT NULL,
  pacientes_DNI INT NOT NULL,
  PRIMARY KEY (Hora_fin, Hora_inicio, doctor_codigo, pacientes_DNI),
  CONSTRAINT fk_citas_horario
    FOREIGN KEY (Hora_fin, Hora_inicio, doctor_codigo)
    REFERENCES Horario (Hora_fin, Hora_inicio, Codigo_doctor)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_citas_pacientes
    FOREIGN KEY (pacientes_DNI)
    REFERENCES pacientes (DNI)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Tabla recetas
CREATE TABLE IF NOT EXISTS recetas (
  Codigo INT NOT NULL,
  Doctor_codigo VARCHAR(5) NOT NULL,
  paciente_codigo INT NOT NULL,
  PRIMARY KEY (Codigo),
  CONSTRAINT fk_recetas_citas
    FOREIGN KEY (Doctor_codigo, paciente_codigo)
    REFERENCES Citas (doctor_codigo, pacientes_DNI)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Tabla medicamento
CREATE TABLE IF NOT EXISTS medicamento (
  ID INT NOT NULL,
  Stock INT NOT NULL,
  Detalle VARCHAR(45) NOT NULL,
  Marca VARCHAR(255) NOT NULL,
  Nombre VARCHAR(255) NOT NULL,
  PRIMARY KEY (ID)
);

-- Tabla medicamentos_recetados
CREATE TABLE IF NOT EXISTS medicamentos_recetados (
  receta_codigo INT NOT NULL,
  medicamento_codigo INT NOT NULL,
  cantidad INT NOT NULL,
  precio DOUBLE PRECISION NOT NULL,
  dosis VARCHAR(45) NOT NULL,
  PRIMARY KEY (receta_codigo, medicamento_codigo),
  CONSTRAINT fk_medicamentos_recetados_recetas
    FOREIGN KEY (receta_codigo)
    REFERENCES recetas (Codigo)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_medicamentos_recetados_medicamento
    FOREIGN KEY (medicamento_codigo)
    REFERENCES medicamento (ID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Tabla recetas_aprobadas
CREATE TABLE IF NOT EXISTS recetas_aprobadas (
  recetas_Codigo INT NOT NULL,
  recetas_paciente_codigo INT NOT NULL,
  farmacistas_Codigo VARCHAR(5) NOT NULL,
  Hora TIMESTAMP NOT NULL,
  codigo_venta INT NOT NULL,
  PRIMARY KEY (codigo_venta),
  CONSTRAINT fk_recetas_aprobadas_recetas
    FOREIGN KEY (recetas_Codigo, recetas_paciente_codigo)
    REFERENCES recetas (Codigo, paciente_codigo)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_recetas_aprobadas_farmacistas
    FOREIGN KEY (farmacistas_Codigo)
    REFERENCES farmacistas (Codigo)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);