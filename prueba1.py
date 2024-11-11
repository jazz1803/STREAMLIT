import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Cargar datos desde el archivo Excelllll
df = pd.read_excel("vendedores.xlsx")

# Crear una nueva columna combinando "NOMBRE" y "APELLIDO"
df["Vendedor"] = df["NOMBRE"] + " " + df["APELLIDO"]

# Título de la aplicación
st.title("Análisis de Ventas por Vendedor y Región")

# Filtrar por Región
regiones = df["REGION"].unique()
region_seleccionada = st.sidebar.selectbox("Seleccione una región", ["Todas"] + list(regiones))

if region_seleccionada != "Todas":
    df = df[df["REGION"] == region_seleccionada]

# Filtrar por Vendedor
vendedores = df["Vendedor"].unique()
vendedor_seleccionado = st.sidebar.selectbox("Seleccione un vendedor", ["Todos"] + list(vendedores))

if vendedor_seleccionado != "Todos":
    df = df[df["Vendedor"] == vendedor_seleccionado]

# Mostrar la tabla filtrada
st.write("### Datos Filtrados")
st.dataframe(df)

# Gráfico 1: Unidades Vendidas por Vendedor
st.subheader("Unidades Vendidas por Vendedor")
fig1, ax1 = plt.subplots()
ax1.bar(df["Vendedor"], df["UNIDADES VENDIDAS"], color='gray')
ax1.set_title("Unidades Vendidas por Vendedor")
ax1.set_xlabel("Vendedor")
ax1.set_ylabel("Unidades Vendidas")
plt.xticks(rotation=45)
st.pyplot(fig1)

# Gráfico 2: Ventas Totales por Vendedor
st.subheader("Ventas Totales por Vendedor")
fig2, ax2 = plt.subplots()
ax2.bar(df["Vendedor"], df["VENTAS TOTALES"], color='blue')
ax2.set_title("Ventas Totales por Vendedor")
ax2.set_xlabel("Vendedor")
ax2.set_ylabel("Ventas Totales")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Gráfico 3: Porcentaje de Ventas por Vendedor
st.subheader("Porcentaje de Ventas por Vendedor")
fig3, ax3 = plt.subplots()
ax3.pie(df["PORCENTAJE DE VENTAS"], labels=df["Vendedor"], autopct='%1.1f%%', startangle=140)
ax3.set_title("Distribución del Porcentaje de Ventas")
st.pyplot(fig3)



