# Proyecto: Migración de Datos Oracle a XML y Carga en Vista de Aplicación

## Descripción

Este proyecto tiene como objetivo extraer datos de una base de datos Oracle y convertirlos en un archivo XML. Posteriormente, los datos en XML se insertan en una vista específica para su uso en una aplicación. Incluye dos scripts principales:

1. **01.oracle_to_xml.py**: Extrae datos de Oracle y los convierte en un archivo XML.
2. **02.insert_xml_to_view.py**: Lee el archivo XML y lo inserta en una vista de aplicación para su consulta.

## Archivos

- `01.oracle_to_xml.py`: Script que se conecta a Oracle, realiza la consulta y genera un archivo XML con los datos.
- `02.insert_xml_to_view.py`: Script que toma el XML generado, lo procesa y lo carga en la vista de la aplicación.
- `employees.xml`: Ejemplo de archivo XML generado, contiene una lista de empleados con información de sus departamentos.
- `requirements.txt`: Lista de dependencias necesarias, en este caso, la librería `cx_Oracle` para la conexión a la base de datos.

## Prerrequisitos

1. **Python** 3.x
2. **Oracle Database** con los datos a extraer.
3. **cx_Oracle** (ver instalación en la sección "Instalación de Dependencias").

## Instalación de Dependencias

Ejecuta el siguiente comando para instalar las dependencias especificadas:

```bash
pip install -r requirements.txt
```

## Configuración
Asegúrate de tener las credenciales y la cadena de conexión a la base de datos Oracle.
Modifica los scripts `01.oracle_to_xml.py` y `02.insert_xml_to_view.py` para ingresar tus credenciales y parámetros específicos de conexión.

## Uso
1. **Extracción de Datos:** Ejecuta `01.oracle_to_xml.py` para extraer los datos y generar el archivo XML.

```bash
python 01.oracle_to_xml.py
```

2. **Inserción en Vista:** Una vez generado el archivo XML, ejecuta `02.insert_xml_to_view.py` para cargar los datos en la vista de la aplicación.


```bash
python 02.insert_xml_to_view.py
```

## Ejemplo de Datos
El archivo `employees.xml` tiene la siguiente estructura:


```xml
<Employees>
    <Employee>
        <FirstName>Steven</FirstName>
        <LastName>King</LastName>
        <DepartmentName>Executive</DepartmentName>
    </Employee>
    <!-- Más empleados... -->
</Employees>
```

Cada empleado incluye `FirstName`, `LastName` y `DepartmentName`, representando la información básica extraída desde la base de datos Oracle.

## Notas
Revisa el archivo `employees.xml` generado antes de cargarlo en la vista para asegurar la precisión de los datos.
Si cambian los campos en la base de datos, deberás actualizar los scripts para reflejar dichos cambios.

## Créditos
Desarrollado por Andrés Vargas.