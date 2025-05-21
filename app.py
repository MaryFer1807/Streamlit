import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la app
st.title("Análisis de Datos de Vehículos")

# Función para cargar datos (con caché para optimizar)
@st.cache_data
def cargar_datos():
    return pd.read_csv("vehicles_us.csv")

# Carga el DataFrame
df = cargar_datos()

# Sección: Vista general del dataset
st.header("Vista general del dataset")
st.write("Primeras filas del DataFrame:")
st.dataframe(df.head())

# Barra lateral: filtros para seleccionar modelo y rango de años
st.sidebar.header("Filtros")
modelo = st.sidebar.selectbox("Selecciona un modelo:", df['model'].dropna().unique())
anio_min, anio_max = int(df['model_year'].min()), int(df['model_year'].max())
anio = st.sidebar.slider("Selecciona el rango de años:", anio_min, anio_max, (anio_min, anio_max))

# Filtrado del DataFrame según filtros seleccionados
df_filtrado = df[(df['model'] == modelo) & 
                 (df['model_year'] >= anio[0]) & 
                 (df['model_year'] <= anio[1])]

# Mostrar resultados filtrados
st.write(f"Vehículos del modelo **{modelo}** entre los años {anio[0]} y {anio[1]}:")
st.dataframe(df_filtrado)

# --- Aquí comienza la parte para selección y visualización de gráficos ---

# Barra lateral: selector de gráfico
st.sidebar.header("Visualizaciones")
grafico = st.sidebar.selectbox("Selecciona un gráfico:",
                               ["Distribución de precios", 
                                "Precio vs Año", 
                                "Cantidad por condición"])

# Mostrar gráficos sólo si hay datos filtrados
if not df_filtrado.empty:
    if grafico == "Distribución de precios":
        fig = px.histogram(df_filtrado, x="price", nbins=30,
                           title=f"Distribución de precios para {modelo}")
        st.plotly_chart(fig)

    elif grafico == "Precio vs Año":
        fig = px.scatter(df_filtrado, x="model_year", y="price", color="condition",
                         title=f"Precio vs Año para {modelo}")
        st.plotly_chart(fig)

    elif grafico == "Cantidad por condición":
        conteo = df_filtrado['condition'].value_counts().reset_index()
        conteo.columns = ['condition', 'count']
        fig = px.bar(conteo, x='condition', y='count', title="Cantidad de vehículos por condición")
        st.plotly_chart(fig)
else:
    st.warning("No hay datos para el modelo y rango de años seleccionados.")

# --- Fin de la app ---





