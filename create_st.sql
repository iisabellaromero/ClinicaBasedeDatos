-- FALTAN RESTRICCIONES Y CHECKS
-- Schema clinica
CREATE SCHEMA IF NOT EXISTS clinica;

-- set search path clinica schema
SET search_path = clinica;

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
  PRIMARY KEY (Codigo),
); 

-- Tabla Consultorio DONE
CREATE TABLE IF NOT EXISTS Consultorio (
  Codigo.doctor VARCHAR(5) NOT NULL,
  Consultorio_numero VARCHAR(4) NOT NULL,
  PRIMARY KEY (Consultorio)
  FOREIGN KEY (Codigo.doctor)
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

-- Tabla Horario DONE                                 CHECK
CREATE TABLE IF NOT EXISTS Horario (
  Dia VARCHAR(9) NOT NULL,
  Hora_inicio TIMESTAMP NOT NULL,
  Hora_fin TIMESTAMP NOT NULL,
  Codigo_doctor VARCHAR(5) NOT NULL,
  Estado BOOLEAN NOT NULL DEFAULT TRUE,
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


-- Tabla pacientes DONE                                 CHECK
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

-- Tabla Seguro DONE                                 CHECK
CREATE TABLE IF NOT EXISTS Seguro (
  Id INT NOT NULL,
  Nombre INT NOT NULL,
  PRIMARY KEY (Id)
); 

-- Tabla Poliza DONE                                 CHECK
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


-- Tabla asegurados DONE                                 CHECK
CREATE TABLE IF NOT EXISTS asegurados (
  pacientes_DNI INT NOT NULL,
  poliza_id INT NOT NULL,
  seguro_id INT NOT NULL,
  PRIMARY KEY (pacientes_DNI), --la llave primaria deberia ser paciente dni, ya que un paciente no puede tener mas de un seguro de salud
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



-- Tabla Citas DONE                                 CHECK
CREATE TABLE IF NOT EXISTS Citas (
  fecha DATE NOT NULL,
  Hora_inicio TIMESTAMP NOT NULL,
  Hora_fin TIMESTAMP NOT NULL,
  doctor_codigo VARCHAR(5) NOT NULL,
  especialidad VARCHAR(45) NOT NULL,
  pacientes_DNI INT NOT NULL,
  consultorio VARCHAR(4) NOT NULL,
  precio INT DEFAULT 200,
  precio_deducible INT DEFAULT 0,
  -- PRIMARY KEY (fecha, Hora_fin, Hora_inicio, doctor_codigo)
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

-- Tabla recetas DONE                                 CHECK
CREATE TABLE IF NOT EXISTS recetas (
  Codigo INT NOT NULL,
  FECHA DATE NOT NULL,
  Doctor_codigo VARCHAR(5) NOT NULL,
  paciente_codigo INT NOT NULL,
  -- fecha DATE NOT NULL,
  PRIMARY KEY (Codigo),
  CONSTRAINT fk_recetas_citas
    FOREIGN KEY (Doctor_codigo, paciente_codigo)
    REFERENCES Citas (doctor_codigo, pacientes_DNI)
    ON DELETE CASCADE
    ON UPDATE CASCADE
); 

-- Tabla medicamento DONE                                 CHECK
CREATE TABLE IF NOT EXISTS medicamento (
  ID INT NOT NULL,
  Nombre VARCHAR(255) NOT NULL,
  Laboratorio VARCHAR(255) NOT NULL,
  Precio DOUBLE PRECISION NOT NULL,
  Unidad INT NOT NULL,
  Stock INT NOT NULL,
  PRIMARY KEY (ID)
); 

-- Tabla medicamentos_recetados DONE                                 CHECK
CREATE TABLE IF NOT EXISTS medicamentos_recetados (
  receta_codigo INT NOT NULL,
  medicamento_codigo INT NOT NULL,
  nombre_medicamento VARCHAR(45) NOT NULL
  cantidad INT NOT NULL,
  -- dosis VARCHAR(45) NOT NULL, yo lo borre
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

--Triggers
CREATE OR REPLACE FUNCTION calculate_citas_precio_deducible()
RETURNS TRIGGER AS $$
BEGIN
  -- Retrieve the poliza_id from asegurados table using paciente_dni
  SELECT poliza_id INTO NEW.poliza_id
  FROM asegurados
  WHERE pacientes_dni = NEW.pacientes_dni;

  -- Retrieve the cobertura from Poliza table using poliza_id
  SELECT cobertura INTO NEW.cobertura
  FROM poliza
  WHERE id = NEW.poliza_id;

  -- Calculate and set the value for Citas.precio_deducible
  NEW.precio_deducible := (NEW.precio * (NEW.cobertura / 100));

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- Trigger2
CREATE TRIGGER set_citas_precio_deducible
BEFORE INSERT ON citas
FOR EACH ROW
EXECUTE FUNCTION calculate_citas_precio_deducible();

CREATE OR REPLACE FUNCTION calculate_medicamento_recetado_precio_regular()
RETURNS TRIGGER AS $$
DECLARE
  poliza_cobertura INT;
BEGIN
  -- Retrieve the medicamento price from medicamentos table
  SELECT precio INTO NEW.precio_regular
  FROM medicamento
  WHERE id = NEW.medicamento_codigo;

  -- Retrieve the poliza_id and cobertura from asegurados and poliza tables using paciente_dni
  SELECT a.poliza_id, p.cobertura INTO NEW.poliza_id, poliza_cobertura
  FROM asegurados a
  JOIN poliza p ON p.id = a.poliza_id
  WHERE a.pacientes_dni = NEW.paciente_codigo;

  -- Calculate and set the value for medicamentos_recetados.precio_regular
  NEW.precio_regular := (NEW.precio_regular * NEW.cantidad);

  -- Calculate and set the value for medicamentos_recetados.precio_deducible
  NEW.precio_deducible := (NEW.precio_regular * (poliza_cobertura / 100));

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_medicamento_recetado_precios
BEFORE INSERT ON medicamentos_recetados
FOR EACH ROW
EXECUTE FUNCTION calculate_medicamento_recetado_precio_regular();