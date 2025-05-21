# Proyecto Dashboard con Streamlit

## Descripción

Este proyecto consiste en el desarrollo de una aplicación web interactiva utilizando Streamlit, con el objetivo de realizar un análisis exploratorio básico sobre un conjunto de datos de anuncios de vehículos en Estados Unidos (`vehicles_us.csv`). La aplicación permite visualizar gráficos como histogramas y diagramas de dispersión mediante botones o casillas de verificación, facilitando la exploración visual de los datos.

## Estructura del proyecto

.
├── README.md
├── app.py
├── vehicles_us.csv
└── notebooks
└── EDA.ipynb

bash
Copiar
Editar

- **app.py**: Archivo principal que contiene el código de la aplicación web con Streamlit.  
- **vehicles_us.csv**: Conjunto de datos utilizado para el análisis y visualización.  
- **notebooks/EDA.ipynb**: Notebook de Jupyter donde se realizó el análisis exploratorio inicial.  
- **README.md**: Este archivo con la descripción y guía para ejecutar el proyecto.

## Instrucciones para ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/MaryFer1807/Streamlit.git
cd Streamlit
Crear y activar un entorno virtual (opcional pero recomendado):

bash
Copiar
Editar
python -m venv vehicles_env
# Windows
vehicles_env\Scripts\activate
# macOS/Linux
source vehicles_env/bin/activate
Instalar las dependencias necesarias:

bash
Copiar
Editar
pip install pandas streamlit plotly-express
Asegurarse de que el archivo vehicles_us.csv está en la raíz del proyecto.

Ejecutar la aplicación web:

bash
Copiar
Editar
streamlit run app.py
Se abrirá una ventana en el navegador con la interfaz del dashboard.

Funcionalidades principales
Visualización de un histograma interactivo para la columna "odometer".

Visualización de un gráfico de dispersión (scatter plot).

Uso de botones o casillas de verificación para controlar la visualización de gráficos.

Encabezados y mensajes explicativos para guiar al usuario.

Datos
El conjunto de datos vehicles_us.csv contiene anuncios de vehículos usados en Estados Unidos. Está incluido en el repositorio para que la aplicación pueda cargarlo localmente y mostrar las visualizaciones.

Mary Fernández
Repositorio: https://github.com/MaryFer1807/Streamlit

markdown
Copiar
Editar

---

### Cómo guardarlo en VS Code y subirlo a GitHub

1. En VS Code, crea un archivo nuevo:
   - Click en el icono de **"Nuevo archivo"** (arriba a la izquierda).
   - Nómbralo **`README.md`** (asegúrate que la extensión sea `.md`).

2. Pega todo el contenido que te di en ese archivo.

3. Guarda el archivo con **Ctrl + S** (o Cmd + S en Mac).

4. Para que git detecte el archivo y lo suba, abre la terminal integrada de VS Code (Ctrl + `).

5. Ejecuta estos comandos:

```bash
git add README.md
git commit -m "Agrega README con descripción del proyecto"
git push origin main
