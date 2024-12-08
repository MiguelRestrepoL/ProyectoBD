import psycopg2
from psycopg2 import sql

#Establece la conexión a la base de datos
def conectar():
    
    try:
        conexion = psycopg2.connect(
            user="postgres",
            password="DIMINOMBRE02",  
            host="localhost",
            port="5432",
            database="ProyectoAulas"
        )
        print("Conexión exitosa a la base de datos.")
        return conexion
    except psycopg2.OperationalError as e:
        print("Error al conectar con la base de datos:", e)
        return None



#Datos quemados de las tablas y tambien normales
def inicializar_datos(conexion, tablas):

    try:
        with conexion.cursor() as cursor:
            if tablas == "aula":
                datos = [
                    (101, 30, 1, 'Disponible'),
                    (102, 25, 1, 'Ocupado'),
                    (103, 40, 2, 'Disponible'),
                    (104, 20, 2, 'Mantenimiento'),
                ]
                query = """
                INSERT INTO aula (num_aula, capacidad, piso_aula, estado_aula)
                SELECT %s, %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT 1 FROM aula WHERE num_aula = %s
                )
                """
                for dato in datos:
                    cursor.execute(query, (*dato, dato[0]))
            elif tablas == "estudiante":
                datos = [
                    (2233498, 7543189, 'Juan', 'David', 'Pérez','Orejuela', 5, 'calle 9', 'jd@gmail.com', 3124562343),
                    (2299835, 3216734, 'Gerson', 'Alejandro', 'castro','Nieva', 3, 'calle 9', 'jd@gmail.com', 3124562343),
                    (2223658, 9872342, 'Ana', 'Dayana', 'Rico','Nieves', 1, 'calle 9', 'jd@gmail.com', 3124562343),
                    (2232109, 8975348, 'Daniela', 'Stephany', 'Lopez','Muñoz', 4, 'calle 9', 'jd@gmail.com', 3124562343),
                ]
                query = """
                INSERT INTO estudiante (cod_estudiante, dni_estudiante, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, semestre_cursante, direccion, e_mail, telefono)
                SELECT %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT 1 FROM estudiante WHERE cod_estudiante = %s
                )
                """
                for dato in datos:
                    cursor.execute(query, (*dato, dato[0]))
            elif tablas == "profesor":
                datos = [
                    (1, 'Luis', 'David', 'Gómez', '', 'Matemáticas'),
                    (2, 'María', '', 'Torres', '', 'Ciencias'),
                    (3, 'Pedro', '', 'Ramírez', '', 'Historia'),
                    (4, 'Elena', '', 'Martínez', '', 'Arte'),
                ]
                query = """
                INSERT INTO profesor (id_profesor, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, profesion)
                SELECT %s, %s, %s, %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT 1 FROM profesor WHERE id_profesor = %s
                )
                """
                for dato in datos:
                    cursor.execute(query, (*dato, dato[0]))
            elif tablas == "agenda":
                datos = [
                    (1, '2024-12-10', '08:00', '10:00', 101, 1),
                    (2, '2024-12-10', '10:00', '12:00', 102, 2),
                    (3, '2024-12-11', '08:00', '10:00', 103, 1),
                    (4, '2024-12-11', '10:00', '12:00', 104, 2),
                ]
                query = """
                INSERT INTO agenda (id_agenda, fecha, hora_inicio, hora_fin, num_aula, Id_grupo)
                WHERE NOT EXISTS (
                    SELECT 1 FROM agenda WHERE id_agenda = %s
                )
                """
                for dato in datos:
                    cursor.execute(query, (*dato, dato[0]))
            elif tablas == "agenda_profesor":
                datos = [
                    (1, 1, 'Disponible'),
                    (2, 2, 'Ocupado'),
                    (3, 3, 'Disponible'),
                    (4, 4, 'Disponible'),
                ]
                query = """
                INSERT INTO agenda_profesor (id_agenda, id_profesor, disponibilidad)
                SELECT %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT 1 FROM agenda_profesor WHERE id_agenda = %s AND id_profesor = %s
                )
                """
                for dato in datos:
                    cursor.execute(query, (*dato, dato[0]))
            elif tablas == "curso":
                datos = [
                    (1, 'Matemáticas', 5, 'Mañana', 30, 1),
                    (2, 'Ciencias', 10, 'Tarde', 25, 2),
                    (3, 'Historia', 7, 'Noche', 20, 3),
                    (4, 'Arte', 3, 'Mañana', 15, 4),
                ]
                query = """
                INSERT INTO curso (id_curso, nombre_curso, grupo_curso, jornada, cupoestudiantes, profesor_asignado)
                SELECT %s, %s, %s, %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT 1 FROM curso WHERE id_curso = %s
                )
                """
                for dato in datos:
                    cursor.execute(query, (*dato, dato[0]))
            elif tablas == "curso_horario":
                datos = [
                    (1, 1, 'Sesión 1'),
                    (2, 2, 'Sesión 2'),
                    (3, 3, 'Sesión 1'),
                    (4, 4, 'Sesión 2'),
                ]
                query = """
                INSERT INTO curso_horario (id_horario, id_curso, sesion)
                SELECT %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT 1 FROM curso_horario WHERE id_horario = %s AND id_curso = %s
                )
                """
                for dato in datos:
                    cursor.execute(query, (*dato, dato[0]))
            elif tablas == "estudiante_curso":
                datos = [
                    (2233498, 1, 'Activo', 'Presencial'),
                    (2299835, 2, 'Activo', 'Virtual'),
                    (2223658, 3, 'Activo', 'Presencial'),
                    (2232109, 4, 'Activo', 'Presencial'),
                ]
                query = """
                INSERT INTO estudiante_curso (id_estudiante, id_curso, estado, modalidad)
                SELECT %s, %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT 1 FROM estudiante_curso WHERE id_estudiante = %s AND id_curso = %s
                )
                """
                for dato in datos:
                    cursor.execute(query, (*dato, dato[0]))
            elif tablas == "horario":
                datos = [
                    (1, 'Lunes', '08:00', '10:00'),
                    (2, 'Martes', '10:00', '12:00'),
                    (3, 'Miércoles', '08:00', '10:00'),
                    (4, 'Jueves', '10:00', '12:00'),
                ]
                query = """
                INSERT INTO horario (id_horario, dia_semana, hora_inicio, hora_fin)
                SELECT %s, %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT 1 FROM horario WHERE id_horario = %s
                )
                """
                for dato in datos:
                    cursor.execute(query, (*dato, dato[0]))
            elif tablas == "profesor_horario":
                datos = [
                    (1, 1, 'Mañana'),
                    (2, 2, 'Tarde'),
                    (3, 3, 'Noche'),
                    (4, 4, 'Mañana'),
                ]
                query = """
                INSERT INTO profesor_horario (id_profesor, id_horario, jornada)
                SELECT %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT 1 FROM profesor_horario WHERE id_profesor = %s AND id_horario = %s
                )
                """
                for dato in datos:
                    cursor.execute(query, (*dato, dato[0]))
            
            # Agregar inicialización para más tablas aquí-----------------
            conexion.commit()
            print(f"Datos quemados iniciales asegurados para la tabla '{tablas}'.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al inicializar datos quemados para la tabla '{tablas}':", e)

#Muestra el menú principal
def mostrar_menu_principal():
    
    print("\n--- Menú Principal ---")
    print("1. Registrar")
    print("2. Actualizar")
    print("3. Borrar")
    print("4. Mostrar Registros")
    print("5. Salir")
    return input("Seleccione una opción: ")


#Permite al usuario seleccionar una tabla con la que desea trabajar
def seleccionar_tabla():
    
    print("\n--- Selección de Tabla ---")
    print("1. agenda")
    print("2. agenda_profesor")
    print("3. aula")
    print("4. curso")
    print("5. curso_horario")
    print("6. estudiante")
    print("7. estudiante_curso")
    print("8. horario")
    print("9. profesor")
    print("10. profesor_horario")
    print("0. Volver al menú principal")

    tablas = [
        "agenda", "agenda_profesor", "aula", "curso", 
        "curso_horario", "estudiante", "estudiante_curso", 
        "horario", "profesor", "profesor_horario"
    ]
    
    for i, tabla in enumerate(tablas, 1):
        print(f"{i}. {tabla}")
    # Solicitar al usuario que ingrese el número de la tabla que quiere manejar el resto del programa
    
    try:
        opcion = int(input("Seleccione una tabla (1-10): "))
        if 1 <= opcion <= len(tablas):
            return tablas[opcion - 1]
        print("Opción inválida.")
    except ValueError:
        print("Entrada inválida.")
    return None

    

#Registrar datos manualmente en la tabla seleccionada
def registrar_datos(conexion, tabla):
    
    try:
        with conexion.cursor() as cursor:
            if tabla == "aula":
                num_aula = input("Ingrese el número del aula (101/201/301): ")
                capacidad = input("Ingrese la capacidad del aula: ")
                piso_aula = input("Ingrese el piso del aula: ")
                estado_aula = input("Ingrese el estado del aula (Disponible/Ocupado): ")
                query = """
                INSERT INTO aula (num_aula, capacidad, piso_aula, estado_aula)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (num_aula, capacidad, piso_aula, estado_aula))

            elif tabla == "profesor":
                id_profesor = input("Ingrese el ID del profesor: ")
                primer_nombre = input("Ingrese el primer nombre del profesor: ")
                segundo_nombre = input("Ingrese el segundo nombre del profesor (opcional): ")
                primer_apellido = input("Ingrese el primer apellido del profesor: ")
                segundo_apellido = input("Ingrese el segundo apellido del profesor (opcional): ")
                profesion = input("Ingrese la profesión del profesor: ")
                query = """
                INSERT INTO profesor (id_profesor, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, profesion)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (id_profesor, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, profesion))

            elif tabla == "estudiante":
                cod_estudiante = input("Ingrese el código del estudiante: ")
                dni_estudiante = input("Ingrese el documento de identidad del estudiante: ")
                primer_nombre = input("Ingrese el primer nombre del estudiante: ")
                segundo_nombre = input("Ingrese el segundo nombre del estudiante (opcional): ")
                primer_apellido = input("Ingrese el primer apellido del estudiante: ")
                segundo_apellido = input("Ingrese el segundo apellido del estudiante: ")
                semestre_cursante = input("Ingrese el semestre cursante: ")
                direccion = input("Ingrese la dirección del estudiante: ")
                e_mail = input("Ingrese el correo electrónico del estudiante: ")
                telefono = input("Ingrese el número de teléfono del estudiante: ")
                query = """
                INSERT INTO estudiante (cod_estudiante, dni_estudiante, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, semestre_cursante, direccion, e_mail, telefono)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (cod_estudiante, dni_estudiante, primer_nombre, segundo_nombre or None, primer_apellido, segundo_apellido, semestre_cursante, direccion, e_mail, telefono))

            elif tabla == "curso":
                id_curso = input("Ingrese el ID del curso: ")
                nombre_curso = input("Ingrese el nombre del curso: ")
                grupo_curso = input("Ingrese el grupo del curso: ")
                jornada = input("Ingrese la jornada (Mañana/Tarde): ")
                cupoestudiantes = input("Ingrese el cupo máximo de estudiantes: ")
                profesor_asignado = input("Ingrese el ID del profesor asignado: ")
                query = """
                INSERT INTO curso (id_curso, nombre_curso, grupo_curso, jornada, cupoestudiantes, profesor_asignado)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (id_curso, nombre_curso, grupo_curso, jornada, cupoestudiantes, profesor_asignado))

            elif tabla == "horario":
                id_horario = input("Ingrese el ID del horario: ")
                dia_semana = input("Ingrese el día de la semana: ")
                hora_inicio = input("Ingrese la hora de inicio (HH:MM): ")
                hora_fin = input("Ingrese la hora de fin (HH:MM): ")
                query = """
                INSERT INTO horario (id_horario, dia_semana, hora_inicio, hora_fin)
                VALUES %s, %s, %s, %s)
                """
                cursor.execute(query, (id_horario, dia_semana, hora_inicio, hora_fin))

            elif tabla == "curso_horario":
                id_horario = input("Ingrese el ID del horario: ")
                id_curso = input("Ingrese el ID del curso: ")
                sesion = input("Ingrese la descripción de la sesión (Ej.: Sesión 1, Sesión 2): ")
                query = """
                INSERT INTO curso_horario id_horario, id_curso, sesion)
                VALUES (%s, %s, %s)
                """
                cursor.execute(query, (id_horario, id_curso, sesion))

            elif tabla == "agenda":
                id_agenda = input("Ingrese el ID de la agenda: ")
                fecha = input("Ingrese la fecha de la agenda (YYYY-MM-DD): ")
                hora_inicio = input("Ingrese la hora de inicio (HH:MM): ")
                hora_fin = input("Ingrese la hora de fin (HH:MM): ")
                num_aula = input("Ingrese el número del aula asignada: ")
                Id_grupo = input("Ingrese el ID del grupo: ")
                query = """
                INSERT INTO agenda (id_agenda, fecha, hora_inicio, hora_fin, num_aula, Id_grupo)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (id_agenda, fecha, hora_inicio, hora_fin, num_aula, Id_grupo))

            elif tabla == "agenda_profesor":
                id_agenda = input("Ingrese el ID de la agenda: ")
                id_profesor = input("Ingrese el ID del profesor: ")
                disponibilidad = input("Ingrese la disponibilidad (Disponible/Ocupado): ")
                query = """
                INSERT INTO agenda_profesor (id_agenda, id_profesor, disponibilidad)
                VALUES (%s, %s, %s)
                """
                cursor.execute(query, (id_agenda, id_profesor, disponibilidad))

            elif tabla == "estudiante_curso":
                id_estudiante = input("Ingrese el ID del estudiante: ")
                id_curso = input("Ingrese el ID del curso: ")
                estado = input("Ingrese el estado del estudiante en el curso (Activo/Inactivo): ")
                modalidad = input("Ingrese la modalidad del curso (Presencial/Virtual): ")
                query = """
                INSERT INTO estudiante_curso (id_estudiante, id_curso, estado, modalidad)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (id_estudiante, id_curso, estado, modalidad))

            elif tabla == "profesor_horario":
                id_profesor = input("Ingrese el ID del profesor: ")
                id_horario = input("Ingrese el ID del horario: ")
                jornada = input("Ingrese la jornada (Mañana/Tarde/Noche): ")
                query = """
                INSERT INTO profesor_horario (id_profesor, id_horario, jornada)
                VALUES (%s, %s, %s)
                """
                cursor.execute(query, (id_profesor, id_horario, jornada))

            else:
                print(f"Registrar manualmente para la tabla '{tabla}' no está implementado aún.")
                return

            # Confirmar cambios
            conexion.commit()
            print(f"Registro agregado correctamente en la tabla '{tabla}'.")

    except Exception as e:
        conexion.rollback()
        print(f"Error al registrar datos en la tabla '{tabla}':", e)

#Actualizar datos en la tabla seleccionada
def actualizar_datos(conexion, tabla):
    try:
        with conexion.cursor() as cursor:
            if tabla == "aula":
                num_aula = input("Ingrese el número del aula que desea actualizar: ")
                nueva_capacidad = input("Ingrese la nueva capacidad del aula: ")
                nuevo_piso = input("Ingrese el nuevo piso del aula: ")
                nuevo_estado = input("Ingrese el nuevo estado del aula (Disponible/Ocupado): ")
                query = """
                UPDATE aula
                SET capacidad = %s, piso_aula = %s, estado_aula = %s
                WHERE num_aula = %s
                """
                cursor.execute(query, (nueva_capacidad, nuevo_piso, nuevo_estado, num_aula))

            elif tabla == "estudiante":
                cod_estudiante = input("Ingrese el código del estudiante que desea actualizar: ")
                nuevo_dni = input("Ingrese el nuevo documento de identidad del estudiante: ")
                nuevo_primer_nombre = input("Ingrese el nuevo primer nombre del estudiante: ")
                nuevo_segundo_nombre = input("Ingrese el nuevo segundo nombre del estudiante (opcional): ")
                nuevo_primer_apellido = input("Ingrese el nuevo primer apellido del estudiante: ")
                nuevo_segundo_apellido = input("Ingrese el nuevo segundo apellido del estudiante: ")
                nuevo_semestre = input("Ingrese el nuevo semestre del estudiante: ")
                nueva_direccion = input("Ingrese la nueva dirección del estudiante: ")
                nuevo_email = input("Ingrese el nuevo correo electrónico del estudiante: ")
                nuevo_telefono = input("Ingrese el nuevo número de teléfono del estudiante: ")
                query = """
                UPDATE estudiante
                SET dni_estudiante = %s, primer_nombre = %s, segundo_nombre = %s, 
                    primer_apellido = %s, segundo_apellido = %s, semestre_cursante = %s, 
                    direccion = %s, e_mail = %s, telefono = %s
                WHERE cod_estudiante = %s
                """
                cursor.execute(query, (nuevo_dni, nuevo_primer_nombre, nuevo_segundo_nombre or None, 
                                       nuevo_primer_apellido, nuevo_segundo_apellido, nuevo_semestre, 
                                       nueva_direccion, nuevo_email, nuevo_telefono, cod_estudiante))

            elif tabla == "profesor":
                id_profesor = input("Ingrese el ID del profesor que desea actualizar: ")
                nuevo_primer_nombre = input("Ingrese el nuevo primer nombre del profesor: ")
                nuevo_segundo_nombre = input("Ingrese el nuevo segundo nombre del profesor (opcional): ")
                nuevo_primer_apellido = input("Ingrese el nuevo primer apellido del profesor: ")
                nuevo_segundo_apellido = input("Ingrese el nuevo segundo apellido del profesor (opcional): ")
                nueva_profesion = input("Ingrese la nueva profesión del profesor: ")
                query = """
                UPDATE profesor
                SET primer_nombre = %s, segundo_nombre = %s, primer_apellido = %s, 
                    segundo_apellido = %s, profesion = %s
                WHERE id_profesor = %s
                """
                cursor.execute(query, (nuevo_primer_nombre, nuevo_segundo_nombre or None, 
                                       nuevo_primer_apellido, nuevo_segundo_apellido or None, 
                                       nueva_profesion, id_profesor))

            elif tabla == "curso":
                id_curso = input("Ingrese el ID del curso que desea actualizar: ")
                nuevo_nombre = input("Ingrese el nuevo nombre del curso: ")
                nuevo_grupo = input("Ingrese el nuevo grupo del curso: ")
                nueva_jornada = input("Ingrese la nueva jornada (Mañana/Tarde): ")
                nuevo_cupo = input("Ingrese el nuevo cupo máximo de estudiantes: ")
                nuevo_profesor = input("Ingrese el nuevo ID del profesor asignado: ")
                query = """
                UPDATE curso
                SET nombre_curso = %s, grupo_curso = %s, jornada = %s, 
                    cupoestudiantes = %s, profesor_asignado = %s
                WHERE id_curso = %s
                """
                cursor.execute(query, (nuevo_nombre, nuevo_grupo, nueva_jornada, 
                                       nuevo_cupo, nuevo_profesor, id_curso))

            elif tabla == "agenda":
                id_agenda = input("Ingrese el ID de la agenda que desea actualizar: ")
                nueva_fecha = input("Ingrese la nueva fecha de la agenda (YYYY-MM-DD): ")
                nueva_hora_inicio = input("Ingrese la nueva hora de inicio (HH:MM): ")
                nueva_hora_fin = input("Ingrese la nueva hora de fin (HH:MM): ")
                nuevo_num_aula = input("Ingrese el nuevo número del aula asignada: ")
                nuevo_id_grupo = input("Ingrese el nuevo ID del grupo: ")
                query = """
                UPDATE agenda
                SET fecha = %s, hora_inicio = %s, hora_fin = %s, 
                    num_aula = %s, Id_grupo = %s
                WHERE id_agenda = %s
                """
                cursor.execute(query, (nueva_fecha, nueva_hora_inicio, nueva_hora_fin, 
                                       nuevo_num_aula, nuevo_id_grupo, id_agenda))

            elif tabla == "horario":
                id_horario = input("Ingrese el ID del horario que desea actualizar: ")
                nuevo_dia = input("Ingrese el nuevo día de la semana: ")
                nueva_hora_inicio = input("Ingrese la nueva hora de inicio (HH:MM): ")
                nueva_hora_fin = input("Ingrese la nueva hora de fin (HH:MM): ")
                query = """
                UPDATE horario
                SET dia_semana = %s, hora_inicio = %s, hora_fin = %s
                WHERE id_horario = %s
                """
                cursor.execute(query, (nuevo_dia, nueva_hora_inicio, nueva_hora_fin, id_horario))

            elif tabla == "curso_horario":
                id_horario = input("Ingrese el ID del horario que desea actualizar: ")
                nuevo_id_curso = input("Ingrese el nuevo ID del curso asociado: ")
                nueva_sesion = input("Ingrese la nueva descripción de la sesión: ")
                query = """
                UPDATE curso_horario
                SET id_curso = %s, sesion = %s
                WHERE id_horario = %s
                """
                cursor.execute(query, (nuevo_id_curso, nueva_sesion, id_horario))

            elif tabla == "estudiante_curso":
                id_estudiante = input("Ingrese el ID del estudiante: ")
                id_curso = input("Ingrese el ID del curso: ")
                nuevo_estado = input("Ingrese el nuevo estado (Activo/Inactivo): ")
                nueva_modalidad = input("Ingrese la nueva modalidad (Presencial/Virtual): ")
                query = """
                UPDATE estudiante_curso
                SET estado = %s, modalidad = %s
                WHERE id_estudiante = %s AND id_curso = %s
                """
                cursor.execute(query, (nuevo_estado, nueva_modalidad, id_estudiante, id_curso))

            elif tabla == "agenda_profesor":
                id_agenda = input("Ingrese el ID de la agenda: ")
                id_profesor = input("Ingrese el ID del profesor: ")
                nueva_disponibilidad = input("Ingrese la nueva disponibilidad (Disponible/Ocupado): ")
                query = """
                UPDATE agenda_profesor
                SET disponibilidad = %s
                WHERE id_agenda = %s AND id_profesor = %s
                """
                cursor.execute(query, (nueva_disponibilidad, id_agenda, id_profesor))

            elif tabla == "profesor_horario":
                id_profesor = input("Ingrese el ID del profesor: ")
                id_horario = input("Ingrese el ID del horario: ")
                nueva_jornada = input("Ingrese la nueva jornada (Mañana/Tarde/Noche): ")
                query = """
                UPDATE profesor_horario
                SET jornada = %s
                WHERE id_profesor = %s AND id_horario = %s
                """
                cursor.execute(query, (nueva_jornada, id_profesor, id_horario))

            else:
                print(f"No se ha implementado la actualización para la tabla '{tabla}'.")
                return

            # Confirmar cambios
            conexion.commit()
            print(f"Registro actualizado correctamente en la tabla '{tabla}'.")

    except Exception as e:
        conexion.rollback()
        print(f"Error al actualizar datos en la tabla '{tabla}':", e)


#Permite borrar datos de la tabla seleccionada
def borrar_datos(conexion, tabla):
    try:
        with conexion.cursor() as cursor:
            # Definir claves primarias para cada tabla
            claves_primarias = {
                "agenda": ["id_agenda"],
                "agenda_profesor": ["id_agenda", "id_profesor"],
                "aula": ["num_aula"],
                "curso": ["id_curso"],
                "curso_horario": ["id_horario", "id_curso"],
                "estudiante": ["cod_estudiante"],
                "estudiante_curso": ["id_estudiante", "id_curso"],
                "horario": ["id_horario"],
                "profesor": ["id_profesor"],
                "profesor_horario": ["id_profesor", "id_horario"]
            }

            # Verificar si la tabla tiene definida una clave primaria
            if tabla not in claves_primarias:
                print(f"La tabla '{tabla}' no está definida o no tiene claves primarias configuradas.")
                return

            # Confirmar la operación antes de borrar
            confirmacion = input(f"¿Está seguro de que desea borrar un registro en la tabla '{tabla}'? (s/n): ").lower()
            if confirmacion != "s":
                print("Operación cancelada.")
                return

            # Construir la condición WHERE para la consulta
            condiciones = " AND ".join(f"{clave} = %s" for clave in claves_primarias[tabla])
            query = sql.SQL(f"DELETE FROM {{}} WHERE {condiciones}").format(
                sql.Identifier(tabla)
            )

            # Solicitar los valores de las claves primarias
            valores = []
            for clave in claves_primarias[tabla]:
                valor = input(f"Ingrese el valor de '{clave}': ")
                valores.append(valor)

            # Ejecutar la consulta
            cursor.execute(query, tuple(valores))
            conexion.commit()
            print(f"Registro con claves {', '.join(claves_primarias[tabla])} borrado correctamente de la tabla '{tabla}'.")

    except Exception as e:
        conexion.rollback()
        print(f"Error al borrar datos en la tabla '{tabla}':", e)



#Muestra todos los registros de la tabla seleccionada.
def mostrar_registros(conexion, tabla):
    try:
        with conexion.cursor() as cursor:
            # Verificar si la tabla existe
            cursor.execute("""
                SELECT EXISTS (
                    SELECT 1 FROM information_schema.tables
                    WHERE table_name = %s
                )
            """, (tabla,))
            if not cursor.fetchone()[0]:
                print(f"La tabla '{tabla}' no existe en la base de datos.")
                return

            # Obtener los nombres de las columnas
            cursor.execute(f"SELECT * FROM {tabla} LIMIT 0")
            columnas = [desc[0] for desc in cursor.description]

            # Ejecutar la consulta para obtener los registros
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(tabla))
            cursor.execute(query)
            registros = cursor.fetchall()

            if registros:
                print(f"\n--- Registros en la tabla '{tabla}' ---")
                print(" | ".join(columnas))  # Mostrar los nombres de las columnas
                print("-" * 50)  # Separador
                for registro in registros:
                    print(" | ".join(map(str, registro)))  # Imprimir los registros
            else:
                print(f"\nLa tabla '{tabla}' no contiene registros.")

    except Exception as e:
        print(f"Error al mostrar registros en la tabla '{tabla}':", e)




# Flujo principal del programa-Maneja las opciones principales y cierra la conexion
# Flujo principal del programa - Maneja las opciones principales y cierra la conexión
conexion = conectar()
if conexion:
    try:
        while True:
            print("\n--- Menú Principal ---")
            print("1. Seleccionar tabla")
            print("2. Registrar datos")
            print("3. Actualizar datos")
            print("4. Borrar datos")
            print("5. Mostrar registros")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                tabla = seleccionar_tabla()
                if tabla:
                    inicializar_datos(conexion, tabla)
                else:
                    print("No se seleccionó una tabla.")
            elif opcion in {"2", "3", "4", "5"}:
                if not tabla:
                    print("Primero debe seleccionar una tabla.")
                    continue

                if opcion == "2":
                    registrar_datos(conexion, tabla)
                elif opcion == "3":
                    actualizar_datos(conexion, tabla)
                elif opcion == "4":
                    borrar_datos(conexion, tabla)
                elif opcion == "5":
                    mostrar_registros(conexion, tabla)
            elif opcion == "6":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida.")
    finally:
        conexion.close()
        print("Conexión cerrada.")




