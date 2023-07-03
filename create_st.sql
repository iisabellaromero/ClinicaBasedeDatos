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


-- TABLA DOCTORES
CREATE TABLE IF NOT EXISTS doctores (
    Codigo VARCHAR(5) NOT NULL CONSTRAINT chk_codigo_doctor CHECK (Codigo LIKE 'D%'),
    Codigo_cmp VARCHAR(6) NOT NULL,
    Nombre VARCHAR(45) NOT NULL,
    Apellido VARCHAR(255) NOT NULL,
    Apellido_materno VARCHAR(255) NOT NULL,
    Fecha_nacimiento DATE NOT NULL CONSTRAINT chk_fecha_nacimiento CHECK (Fecha_nacimiento < CURRENT_DATE),
    Telefono VARCHAR(9) NOT NULL CONSTRAINT chk_telefono CHECK (Telefono ~ '^9\d{8}$'),
    DNI INT NOT NULL CONSTRAINT chk_dni CHECK (DNI BETWEEN 10000000 AND 99999999),
    Email VARCHAR(255) NOT NULL CONSTRAINT chk_email CHECK (Email ~ '^.+@vitasalud\.com$'),
    Especialidad VARCHAR(255) NOT NULL,
    PRIMARY KEY (Codigo)
);



-- TABLA CONSULTORIO
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


-- TABLA FARMACISTAS
CREATE TABLE IF NOT EXISTS farmacistas (
    Codigo VARCHAR(5) NOT NULL CONSTRAINT chk_codigo_farmacista CHECK (Codigo LIKE 'F%'),
    Nombre VARCHAR(45) NOT NULL,
    Apellido VARCHAR(255) NOT NULL,
    Apellido_materno VARCHAR(255) NOT NULL,
    Fecha_nacimiento DATE NOT NULL CONSTRAINT chk_fecha_nacimientof CHECK (Fecha_nacimiento < CURRENT_DATE),
    Telefono VARCHAR(9) NULL CONSTRAINT chk_telefonof CHECK (Telefono ~ '^9\d{8}$'),
    DNI VARCHAR(9) NOT NULL CONSTRAINT chk_dnif CHECK (DNI BETWEEN '10000000' AND '99999999'),
    Email VARCHAR(255) NOT NULL CONSTRAINT chk_emailf CHECK (Email ~ '^.+@vitasalud\.com$'),
    PRIMARY KEY (Codigo)
);


-- TABLA HORARIO
CREATE TABLE IF NOT EXISTS Horario (
    Dia VARCHAR(9) NOT NULL,
    Hora_inicio TIME NOT NULL,
    Hora_fin TIME NOT NULL,
    Doctor_codigo VARCHAR(6) NOT NULL,
    PRIMARY KEY (Dia, Hora_inicio, Doctor_codigo),
    CONSTRAINT fk_horario_doctores FOREIGN KEY (Doctor_codigo)
        REFERENCES Doctores (Codigo)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT chk_horario CHECK (Hora_inicio < Hora_fin - INTERVAL '1 hour')
);


-- TABLA PACIENTES
CREATE TABLE IF NOT EXISTS pacientes (
    Nombre VARCHAR(45) NOT NULL,
    Apellido VARCHAR(255) NOT NULL,
    Apellido_materno VARCHAR(255) NOT NULL,
    Fecha_nacimiento DATE NOT NULL,
    Telefono VARCHAR(9) NOT NULL,
    DNI INT NOT NULL,
    Email VARCHAR(255) NOT NULL,
    PRIMARY KEY (DNI),
    CONSTRAINT chk_fecha_nacimiento_paciente CHECK (Fecha_nacimiento < CURRENT_DATE),
    CONSTRAINT chk_telefono_paciente CHECK (Telefono ~ '^9\d{8}$'),
    CONSTRAINT chk_dni_paciente CHECK (DNI BETWEEN 10000000 AND 99999999),
    CONSTRAINT chk_email_paciente CHECK (Email ~ '^.+@.+\..+$')
);


-- TABLA SEGURO
CREATE TABLE IF NOT EXISTS Seguro (
    Id INT NOT NULL,
    Nombre VARCHAR(255) NOT NULL,
    PRIMARY KEY (Id)
);


-- TABLA POLIZA
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
            ON UPDATE CASCADE,
    CONSTRAINT chk_cobertura CHECK (Cobertura > 0)
);


-- TABLA ASEGURADOS
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
            REFERENCES Poliza (id, Seguro_Id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS Citas (
    paciente_dni INT NOT NULL,
    fecha DATE NOT NULL,
    Hora_inicio TIME NOT NULL,
    doctor_codigo VARCHAR(5) NOT NULL,
    precio INT DEFAULT 200,
    precio_deducible INT,
    dia VARCHAR(9),
    PRIMARY KEY (fecha, doctor_codigo, paciente_dni),
    CONSTRAINT unique_cita_time UNIQUE (fecha, Hora_inicio, doctor_codigo),
    CONSTRAINT fk_citas_horario
        FOREIGN KEY (dia, Hora_inicio, doctor_codigo)
        REFERENCES Horario (dia, Hora_inicio, doctor_codigo)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_citas_pacientes
        FOREIGN KEY (paciente_dni)
        REFERENCES pacientes (DNI)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);



-- TABLA RECETAS
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


-- TABLA MEDICAMENTOS
CREATE TABLE IF NOT EXISTS medicamentos (
    ID INT NOT NULL,
    Nombre VARCHAR(255) NOT NULL,
    Laboratorio VARCHAR(255) NOT NULL,
    Precio DOUBLE PRECISION NOT NULL CHECK (Precio > 0),
    Unidad INT NOT NULL CHECK (Unidad > 0),
    Stock INT NOT NULL CHECK (Stock >= 0),
    PRIMARY KEY (ID)
);


-- TABLA MEDICAMENTOS_RECETADOS
CREATE TABLE IF NOT EXISTS medicamentos_recetados (
    receta_codigo INT NOT NULL,
    medicamento_codigo INT NOT NULL,
    nombre_medicamento VARCHAR(45) NOT NULL,
    cantidad INT NOT NULL,
    precio_regular double precision  not null,
    precio_deducible double precision,
    PRIMARY KEY (receta_codigo, medicamento_codigo),
    CONSTRAINT fk_codigo_receta
        FOREIGN KEY (receta_codigo)
            REFERENCES recetas (Codigo)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    CONSTRAINT fk_medicamento_codigo
        FOREIGN KEY (medicamento_codigo)
            REFERENCES medicamentos (ID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

-- TABLA RECETAS_APROBADAS
CREATE TABLE IF NOT EXISTS recetas_aprobadas (
    receta_codigo INT NOT NULL,
    farmacista_codigo VARCHAR(5) NOT NULL,
    Hora time NOT NULL,
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


CREATE OR REPLACE FUNCTION calculate_citas_precio_deducible()
    RETURNS TRIGGER AS $$
DECLARE
    cobertura_value numeric;
BEGIN
    -- Retrieve the poliza_id from asegurados table using paciente_dni
    SELECT poliza_id INTO NEW.precio_deducible
    FROM clinica.asegurados
    WHERE paciente_dni = NEW.paciente_dni;

    BEGIN
        -- Retrieve the cobertura from Poliza table using poliza_id
        SELECT cobertura INTO cobertura_value
        FROM clinica.poliza
        WHERE id = NEW.precio_deducible;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            cobertura_value := 0; -- Set a default value when paciente_dni is not found
    END;

    -- Calculate and set the value for Citas.precio_deducible
    NEW.precio_deducible := NEW.precio - (NEW.precio * (cobertura_value / 100));

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_citas_precio_deducible
    BEFORE INSERT ON citas
    FOR EACH ROW
EXECUTE FUNCTION calculate_citas_precio_deducible();

CREATE OR REPLACE FUNCTION calculate_medicamento_recetado_precios()
    RETURNS TRIGGER AS $$
DECLARE
    poliza_cobertura INT;
    pdni INT;
BEGIN
    -- Retrieve the medicamento price from medicamento table
    SELECT precio INTO NEW.precio_regular
    FROM postgres.clinica.medicamentos
    WHERE id = NEW.medicamento_codigo;

    -- Retrieve the paciente_dni from recetas table
    SELECT recetas.paciente_dni INTO pdni
    FROM postgres.clinica.recetas
    WHERE recetas.Codigo = NEW.receta_codigo;

    -- Retrieve the poliza_id and cobertura from asegurados and poliza tables using paciente_dni
    SELECT asegurados.poliza_id, poliza.cobertura INTO poliza_cobertura
    FROM postgres.clinica.asegurados
             JOIN postgres.clinica.poliza ON poliza.id = asegurados.poliza_id
    WHERE asegurados.paciente_dni = pdni;

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
EXECUTE FUNCTION calculate_medicamento_recetado_precios();


CREATE VIEW Horarios_Doctores as
SELECT d.nombre, d.apellido, c.doctor_codigo, c.hora_inicio, c.dia FROM Horario c
join doctores d on c.doctor_codigo = d.codigo


select count(codigo) from doctores;

select count(codigo) from farmacistas;

select count(id) from medicamentos;
select * from medicamentos;

select count(id) from poliza ;

select count(id) from seguro;

select  * from asegurados;

select count(dni) from pacientes;

select count(codigo_venta) from  recetas_aprobadas;

select count(doctor_codigo) from consultorio;

select count(paciente_dni) from asegurados;



select d.codigo, concat(d.nombre,' ',d.apellido) as doctor,c.especialidad
from doctores d
join citas c on c.doctor_codigo = d.codigo
join asegurados on c.paciente_dni = asegurados.paciente_dni
where c.especialidad = 'Gastroenterología';


select d.codigo, concat(d.nombre,' ',d.apellido) as doctor,c.especialidad
from doctores d
         join citas c on c.doctor_codigo = d.codigo
         join asegurados on c.paciente_dni = asegurados.paciente_dni
where c.especialidad = 'Gastroenterología';

select cobertura, m.precio_regular, m.cantidad, m.precio_deducible from asegurados
join poliza on poliza.id = asegurados.poliza_id
join recetas r on r.paciente_dni = asegurados.paciente_dni
join medicamentos_recetados m on r.Codigo = m.receta_codigo
where asegurados.paciente_dni =  '11939913';

select precio_regular, precio_deducible, nombre_medicamento from medicamentos_recetados
join recetas on medicamentos_recetados.receta_codigo = recetas.codigo
where paciente_dni = '11939913';

select precio, precio_deducible, p.cobertura from citas
join asegurados a on Citas.paciente_dni = a.paciente_dni
join poliza p on a.poliza_id = p.id;






--Consultas backend: 

-- Citas: 

select * from clinica.horarios_doctores where
                                            horarios_doctores.doctor_codigo in
                                        (select codigo from clinica.doctores where especialidad= 'Pediatria')
and dia  = 'Martes'
