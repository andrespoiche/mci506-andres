# mci506-andres
Proyecto de Data Engineering - MCI506

## Descripción del Proyecto
Este proyecto tiene como objetivo desarrollar un pipeline de ingeniería de datos que incluye la extracción, transformación y carga (ETL) de datos. Se utilizarán diversas herramientas y técnicas para manejar datos en diferentes formatos y de diferentes fuentes.

## Estructura del Proyecto
El proyecto está organizado en las siguientes carpetas y archivos:

- **src/**: Contiene el código fuente del proyecto.
  - **data/**: Directorio para almacenar los datos.
    - **raw/**: Archivos de datos en bruto que se ingieren en el proyecto.
    - **processed/**: Archivos de datos procesados después de la transformación.
    - **external/**: Datos de fuentes externas.
  - **scripts/**: Scripts para el proceso ETL.
    - **extract.py**: Script para la extracción de datos (actualmente vacío).
    - **transform.py**: Script para la transformación de datos (actualmente vacío).
    - **load.py**: Script para la carga de datos (actualmente vacío).
  - **notebooks/**: Jupyter notebooks para análisis y visualización de datos.
    - **analysis.ipynb**: Notebook para análisis de datos.
  - **utils/**: Utilidades y funciones auxiliares.
    - **helpers.py**: Funciones de ayuda para el proyecto.

- **config/**: Configuraciones del proyecto.
  - **settings.py**: Archivo de configuración para el proyecto.

- **tests/**: Pruebas automatizadas para el código.
  - **test_etl.py**: Pruebas para el script de extracción.
  - **test_transform.py**: Pruebas para el script de transformación.

- **.gitignore**: Especifica archivos que deben ser ignorados por Git.

- **requirements.txt**: Lista de dependencias necesarias para el proyecto.

- **setup.py**: Archivo para empaquetar el proyecto y gestionar dependencias.

## Instrucciones de Uso
1. Clona el repositorio en tu máquina local.
2. Instala las dependencias utilizando `pip install -r requirements.txt`.
3. Ejecuta los scripts de ETL en el orden correspondiente: extracción, transformación y carga.
4. Utiliza los notebooks para realizar análisis adicionales sobre los datos procesados.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cambios o mejoras.