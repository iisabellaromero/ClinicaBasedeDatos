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


CREATE TABLE IF NOT EXISTS Horario (
                                       Dia VARCHAR(9) NOT NULL,
                                       Hora_inicio time NOT NULL,
                                       Hora_fin time NOT NULL,
                                       doctor_codigo VARCHAR(6) NOT NULL,
                                       Estado BOOLEAN NOT NULL DEFAULT TRUE,
                                       PRIMARY KEY (dia, hora_inicio, doctor_codigo),
                                        FOREIGN KEY (doctor_codigo)
                                               REFERENCES doctores (Codigo)
                                               ON DELETE cascade
                                               ON UPDATE CASCADE
);



-- Alter the data type of Hora_inicio column and handle leading spaces
ALTER TABLE Horario
    ALTER COLUMN Hora_inicio TYPE TIME USING CAST(REPLACE(Hora_inicio::TEXT, ' ', '') AS TIME);

-- Alter the data type of Hora_fin column and handle leading spaces
ALTER TABLE Horario
    ALTER COLUMN Hora_fin TYPE TIME USING CAST(REPLACE(Hora_fin::TEXT, ' ', '') AS TIME);


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
                                      Nombre VARCHAR(255) NOT NULL,
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
                                          paciente_dni INT NOT NULL,
                                          poliza_id INT NOT NULL,
                                          seguro_id INT NOT NULL,
                                          PRIMARY KEY (paciente_dni), --la llave primaria deberia ser paciente dni, ya que un paciente no puede tener mas de un seguro de salud
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


-- Tabla Citas DONE                                 CHECK
CREATE TABLE IF NOT EXISTS Citas (
                                     paciente_dni INT NOT NULL,
                                     fecha DATE NOT NULL,
                                     Hora_inicio time NOT NULL,
                                     doctor_codigo VARCHAR(5) NOT NULL,
                                     especialidad VARCHAR(45) NOT NULL,
                                     consultorio VARCHAR(4) NOT NULL,
                                     precio INT,
                                     precio_deducible INT DEFAULT 200,
                                     dia varchar(9),
                                     Hora_fin time,
                                     PRIMARY KEY (fecha,doctor_codigo,paciente_dni),
                                     CONSTRAINT unique_cita_time unique (fecha, hora_inicio, doctor_codigo),
                                     CONSTRAINT fk_citas_horario
                                         FOREIGN KEY ( dia, Hora_inicio, doctor_codigo)
                                             REFERENCES Horario ( dia, Hora_inicio, doctor_codigo)
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

-- Tabla medicamento DONE                                 CHECK
CREATE TABLE IF NOT EXISTS medicamentos (
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

-- Tabla recetas_aprobadas
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
); --2/2
delete from citas;

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
            cobertura_value := 100; -- Set a default value when paciente_dni is not found
    END;

    -- Calculate and set the value for Citas.precio_deducible
    NEW.precio_deducible := (NEW.precio * (cobertura_value / 100));

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

