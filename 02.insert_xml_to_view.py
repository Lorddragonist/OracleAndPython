import cx_Oracle
import os
import xml.etree.ElementTree as ET


def insert_xml_to_view():

    # Configuración de la base de datos
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe')
    connection = cx_Oracle.connect(
        user='system', password='admin', dsn=dsn_tns)
    cursor = connection.cursor()

    # Verificar si la tabla existe, si no crearla
    table_check_query = """
    SELECT COUNT(*) FROM user_tables WHERE table_name = 'EMPLOYEE_VIEW'
    """
    cursor.execute(table_check_query)
    table_exists = cursor.fetchone()[0]

    if table_exists == 0:
        create_table_query = """
        CREATE TABLE employee_view (
            first_name VARCHAR2(50),
            last_name VARCHAR2(50),
            department_name VARCHAR2(100)
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        
    # Leer el archivo XML
    with open("employees.xml", "r") as xml_file:
        xml_data = xml_file.read()

    # Parsear el XML y extraer los datos
    root = ET.fromstring(xml_data)
    for employee in root.findall("Employee"):
        first_name = employee.find("FirstName").text
        last_name = employee.find("LastName").text
        department_name = employee.find("DepartmentName").text

        # Preparar la consulta para insertar los datos en la vista
        insert_query = """
        INSERT INTO employee_view (first_name, last_name, department_name) VALUES (:first_name, :last_name, :department_name)
        """

        # Ejecutar la inserción
        cursor.execute(insert_query, [first_name, last_name, department_name])
    connection.commit()

    # Cerrar cursor y conexión
    cursor.close()
    connection.close()


if __name__ == "__main__":
    insert_xml_to_view()
    print("Datos insertados en la vista exitosamente.")
