import cx_Oracle
import os


def generate_xml():

    # Configuración de la base de datos
    # en este caso la base esta en mi localhost
    # y el servicio es XE por estar montada en Oracle XE
    # cuyo puerto es 1521
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe')
    connection = cx_Oracle.connect(
        user='system', password='admin', dsn=dsn_tns)
    cursor = connection.cursor()

    # Consulta que generará el XML
    query = """
    SELECT XMLELEMENT("Employee",
               XMLFOREST(e.first_name AS "FirstName", e.last_name AS "LastName", d.department_name AS "DepartmentName"))
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
    """
    
    # Ejecución de la consulta para obtener el XML
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # Creación del archivo XML
    with open('employees.xml', 'w') as xml_file:
        xml_file.write('<Employees>')
        for row in rows:
            xml_data = str(row[0])
            xml_file.write(xml_data)
        xml_file.write('</Employees>')
        
    # Cierre de la conexión
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    generate_xml()
    print('XML generado con éxito')