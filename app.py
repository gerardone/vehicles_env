import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(
    '/Users/gerardoparada/Documents/TECH/BOOT/vehicles_env/cleaned_vehicles.csv')

st.header("Información de vehículos usados")

st.write("Vista previa de los datos:")
st.dataframe(car_data.head())


st.subheader("Gráfico de histograma")

selected_column_hist = st.selectbox(
    "Selecciona una columna para el histograma:",
    options=car_data.columns, index=0)


agree_hist = st.checkbox("Crear histograma")

if agree_hist:
    st.write(f"Histograma de la columna {selected_column_hist}")
    fig = px.histogram(car_data, x=selected_column_hist,
                       title=f"Histograma de {selected_column_hist}")
    st.plotly_chart(fig, use_container_width=True)


st.subheader("Gáfico de dispersión")

x_axis = st.selectbox("Selecciona la columna para el eje X:",
                      options=car_data.columns, index=0)
y_axis = st.selectbox("Selecciona la columna para el eje Y:",
                      options=car_data.columns, index=1)

agree_scatter = st.checkbox("Gáfico de dispersión")

if agree_scatter:
    st.write(f"Gráfico de dispersión de {x_axis} vs {y_axis}")
    fig = px.scatter(car_data, x=x_axis, y=y_axis,
                     title=f"{y_axis} vs {x_axis}")
    st.plotly_chart(fig, use_container_width=True)
