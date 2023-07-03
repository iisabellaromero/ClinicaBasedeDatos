
--

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
    WHERE d.especialidad = 'Neurologia'
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
    WHERE p.fecha_nacimiento > current_date - interval '18 years'
    GROUP BY d.especialidad
    order by (avg(m.precio_regular)) desc;

