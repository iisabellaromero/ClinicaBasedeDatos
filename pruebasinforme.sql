
-- Schema clinica
CREATE SCHEMA IF NOT EXISTS clinica2;

-- set search path clinica schema
SET search_path = clinica2;


--TRIGGER PRECIO CITA
-- Trigger para calcular el precio de la cita segun si el paciente tiene seguro o no
-- Ubica el porcentaje de cobertura con el dni del paciente en la tabla asegurados,
-- si el paciente tiene seguro, multiplica este valor por el precio de la cita (siempre 200 por default),
-- si el paciente no tiene seguro, mantiene el precio siendo 200. Volvemos la cobertura 0, y asi, nada se le resta al precio de la cita

CREATE OR REPLACE FUNCTION calculate_citas_precio_deducible()
    RETURNS TRIGGER AS $$
DECLARE
    cobertura_value numeric;
BEGIN
    SELECT poliza_id INTO NEW.precio_deducible
    FROM clinica2.asegurados
    WHERE paciente_dni = NEW.paciente_dni;

    SELECT cobertura INTO cobertura_value
    FROM clinica2.poliza
    WHERE id = NEW.precio_deducible;


    IF cobertura_value IS NOT NULL THEN
        NEW.precio_deducible := NEW.precio - (NEW.precio * (cobertura_value / 100));
    ELSE
        NEW.precio_deducible := NEW.precio;
    end if;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_citas_precio_deducible
    BEFORE INSERT ON citas
    FOR EACH ROW
EXECUTE FUNCTION calculate_citas_precio_deducible();

-- TRIGGER PRECIO MEDICAMENTOS RECETADOS
-- Trigger para insertar y calcular calcular el precio de los medicamentos segun si el paciente tiene seguro o no
-- Primero inserta el precio_regular del medicamento a la tabla, lo ubica segun su precio en recetas y lo multiplica por la cantidad insertada
-- Luego, si el paciente tiene seguro, hace el calculo correspondiente, ubicando el valor de la cobertura y haciendo un cast para volverlo en double precision. Con este nuevo valor, calcula el precio_deducible del medicamento, si el paciente no tiene seguro, tomara el precio_deducible como el precio regular para no dejarlo como NULL

CREATE OR REPLACE FUNCTION calcular_precio_deducible()
    RETURNS TRIGGER AS $$
DECLARE
    _precio_regular double precision;
    _cobertura double precision;
    _paciente_dni int;
BEGIN
    -- Obtener el precio_regular del medicamento
    SELECT Precio INTO _precio_regular FROM clinica.medicamentos WHERE ID = NEW.medicamento_codigo;
    SELECT paciente_dni INTO _paciente_dni FROM clinica.recetas r WHERE r.codigo = NEW.receta_codigo;

    -- Obtener la cobertura de la póliza del paciente (si existe)
    SELECT cobertura::double precision / 100 INTO _cobertura
    FROM clinica.asegurados a
             JOIN clinica.Poliza p ON a.poliza_id = p.id
    WHERE a.paciente_dni = _paciente_dni;

    -- Calcular el precio_deducible
    NEW.precio_regular := _precio_regular * NEW.cantidad;

    IF _cobertura IS NOT NULL THEN
        NEW.precio_deducible := NEW.precio_regular - (NEW.precio_regular * _cobertura);
    ELSE
        NEW.precio_deducible := NEW.precio_regular;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER calcular_precio_deducible_trigger
    BEFORE INSERT ON medicamentos_recetados
    FOR EACH ROW
EXECUTE FUNCTION calcular_precio_deducible();

-- VIEW HORARIO_DOCTORES
-- Tras normalización se requeria un acceso conveniente al horario de los doctores. Esto
-- simplifica las queries y es una abstracción útil.
CREATE VIEW Horarios_Doctores as
SELECT d.nombre, d.apellido, c.doctor_codigo, c.hora_inicio, c.dia FROM Horario c
                                                                            join doctores d on c.doctor_codigo = d.codigo;


--C1

SELECT  p.nombre, p.apellido, p.apellido_materno, m.nombre_medicamento, m.precio_regular
FROM Pacientes p
         JOIN Citas c ON p.dni = c.paciente_dni
         JOIN doctores d ON c.doctor_codigo = codigo
         JOIN Recetas r ON c.doctor_codigo = r.doctor_codigo AND c.paciente_dni = r.paciente_dni
         JOIN Medicamentos_recetados m ON r.codigo = m.receta_codigo
WHERE p.fecha_nacimiento > current_date - interval '18 years'
  AND d.especialidad = 'Oncologia'
  AND m.precio_regular > 300 and m.precio_regular < 1000;

--C2
SELECT EXTRACT(YEAR FROM AGE(current_date, p.fecha_nacimiento)) AS age,
       ROUND(AVG(m.precio_regular)::numeric,2) AS precio_promedio
FROM Pacientes p
         INNER JOIN Citas c ON p.dni = c.paciente_dni
         INNER JOIN doctores d ON c.doctor_codigo = codigo
         INNER JOIN recetas r ON c.doctor_codigo = r.doctor_codigo AND c.paciente_dni = r.paciente_dni
         INNER JOIN Medicamentos_recetados m ON r.codigo = m.receta_codigo
GROUP BY age
ORDER BY age;

--C3
WITH top_medicamentos AS (
    SELECT mr.medicamento_codigo, COUNT(r.codigo) AS cantidad_recetas
    FROM medicamentos_recetados mr
             JOIN recetas r ON mr.receta_codigo = r.codigo
    GROUP BY mr.medicamento_codigo
    ORDER BY COUNT(r.codigo) DESC
    LIMIT 5
)
SELECT m.nombre AS nombre_medicamento, d.especialidad, COUNT(r.codigo) AS cantidad_recetas
FROM medicamentos m
         JOIN medicamentos_recetados mr ON m.ID = mr.medicamento_codigo
         JOIN recetas r ON mr.receta_codigo = r.codigo
         JOIN doctores d ON r.doctor_codigo = d.codigo
WHERE mr.medicamento_codigo IN (SELECT medicamento_codigo FROM top_medicamentos)
GROUP BY m.nombre, d.especialidad
ORDER BY COUNT(r.codigo) DESC;

--C4

SELECT ROUND(AVG(m.precio_regular )::numeric,2), count(m.nombre_medicamento) as cantidad, d.Especialidad AS precio_promedio
FROM Pacientes p
         INNER JOIN Citas c ON p.dni = c.paciente_dni
         INNER JOIN doctores d ON c.doctor_codigo = codigo
         INNER JOIN recetas r ON c.doctor_codigo = r.doctor_codigo AND c.paciente_dni = r.paciente_dni
         INNER JOIN Medicamentos_recetados m ON r.codigo = m.receta_codigo
 
GROUP BY d.especialidad
order by (avg(m.precio_regular)) desc;

-- Índices para la tabla "pacientes"
CREATE INDEX idx_fecha_nacimiento ON pacientes (Fecha_nacimiento);
CREATE INDEX idx_dni ON pacientes (DNI);

-- Índices para la tabla "Citas"
CREATE INDEX idx_paciente_dni ON Citas (paciente_dni);
CREATE INDEX idx_fecha ON Citas (fecha);
CREATE INDEX idx_Hora_inicio ON Citas (Hora_inicio);
CREATE INDEX idx_doctor_codigo ON Citas (doctor_codigo);

CREATE INDEX idx_medicamentos_codigo on medicamentos(nombre);
CREATE INDEX idx_medicamentos_precio on medicamentos(precio);
CREATE INDEX idx_receta_codigo on recetas(codigo);
CREATE INDEX idx_receta_codigo2 on medicamentos_recetados(receta_codigo);
CREATE INDEX idx_medicamento_Codigo2 on medicamentos_recetados(medicamento_codigo);

CREATE INDEX idx_doctores_codigo on doctores(codigo);
CREATE INDEX idx_doctores_especialidad on doctores(especialidad);



-- Indexes for the "pacientes" table
DROP INDEX IF EXISTS idx_fecha_nacimiento;
DROP INDEX IF EXISTS idx_telefono;
DROP INDEX IF EXISTS idx_dni;
DROP INDEX IF EXISTS idx_email;

-- Indexes for the "Citas" table
DROP INDEX IF EXISTS idx_paciente_dni;
DROP INDEX IF EXISTS idx_fecha;
DROP INDEX IF EXISTS idx_Hora_inicio;
DROP INDEX IF EXISTS idx_doctor_codigo;

-- Indexes for the "medicamentos" table
DROP INDEX IF EXISTS idx_medicamentos_codigo;
DROP INDEX IF EXISTS idx_medicamentos_precio;

-- Indexes for the "recetas" table
DROP INDEX IF EXISTS idx_receta_codigo;

-- Indexes for the "medicamentos_recetados" table
DROP INDEX IF EXISTS idx_receta_codigo2;
DROP INDEX IF EXISTS idx_medicamento_Codigo2;

-- Indexes for the "doctores" table
DROP INDEX IF EXISTS idx_doctores_codigo;
DROP INDEX IF EXISTS idx_doctores_especialidad;

delete from recetas_aprobadas;
delete from medicamentos_recetados;
delete from recetas;
DELETE FROM citas;
DELETE FROM horario;
delete from horarios_doctores;
DELETE FROM asegurados;
DELETE FROM consultorio;
DELETE FROM doctores;
delete from farmacistas;
delete from medicamentos;
delete from pacientes;
delete from poliza;
delete from seguro;



--9898282
select count(dni) from pacientes;
-- 302904
select count(paciente_dni) from citas;
-- 291
select count(codigo) from doctores;
-- 99
select count(codigo) from farmacistas;
-- 145
select count(nombre) from medicamentos;
--
select count(receta_codigo) from medicamentos_recetados;
select count(codigo) from recetas;
select count(receta_codigo) from recetas_aprobadas;
select count(id) from seguro;
select count(id) from poliza;

select count(paciente_dni) from asegurados;



CREATE VIEW Horarios_Doctores as
SELECT d.nombre, d.apellido, c.doctor_codigo, c.hora_inicio, c.dia FROM Horario c
                                                                            join doctores d on c.doctor_codigo = d.codigo

drop view citas_completas;
CREATE VIEW Citas_completas as
SELECT concat(p.nombre, ' ' ,p.apellido,' ', p.apellido_materno) as paciente , p.dni as paciente_dni,
       citas.dia, citas.fecha, citas.hora_inicio,
       concat(d.nombre,' ' , d.apellido)as doctor, d.codigo_cmp , d.especialidad,
       citas.precio, citas.precio_deducible from citas
join doctores d on doctor_codigo = d.codigo
join pacientes p on paciente_dni = p.dni
join consultorio c on d.codigo = c.doctor_codigo

select * from citas_completas;
