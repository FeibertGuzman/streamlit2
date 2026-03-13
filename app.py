import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Minero Energético Colombia",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para un look profesional
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    .stMetric label {
        color: #555;
        font-weight: 600;
    }
    .stMetric div[data-testid="stMetricValue"] {
        color: #0068c9;
        font-size: 24px;
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Segoe UI', sans-serif;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Conexión a la base de datos
@st.cache_data
def load_data():
    try:
        conn = sqlite3.connect('SectorMineroEnergeticoColombia.db')
        query_eff = "SELECT * FROM eficiencia_energetica"
        query_proj = "SELECT * FROM proyectos"
        query_inv = "SELECT * FROM inversiones"
        query_emp = "SELECT * FROM empresas"
        query_tipos = "SELECT * FROM tipos_energia"
        
        df_eff = pd.read_sql_query(query_eff, conn)
        df_proj = pd.read_sql_query(query_proj, conn)
        df_inv = pd.read_sql_query(query_inv, conn)
        df_emp = pd.read_sql_query(query_emp, conn)
        df_tipos = pd.read_sql_query(query_tipos, conn)
        
        conn.close()
        return df_eff, df_proj, df_inv, df_emp, df_tipos
    except Exception as e:
        st.error(f"Error conectando a la base de datos: {e}")
        st.info("Por favor, ejecuta primero `python init_db.py` para crear la base de datos.")
        return None, None, None, None, None

# Cargar datos
df_eff, df_proj, df_inv, df_emp, df_tipos = load_data()

# Sidebar de Navegación
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2921/2921226.png", width=100)
st.sidebar.title("Navegación")
menu = st.sidebar.radio("Ir a:", ["Inicio", "Proyectos", "Eficiencia Energética", "Inversiones", "Empresas"])

st.sidebar.markdown("---")
st.sidebar.info("Dashboard desarrollado para el Sector Minero Energético de Colombia.")

# --- PÁGINA: INICIO ---
if menu == "Inicio":
    st.title("⚡ Dashboard Sector Minero Energético Colombia")
    st.markdown("Bienvenido al panel de control integral para el monitoreo de proyectos energéticos y mineros.")
    
    if df_eff is not None:
        # KPIs
        total_energy = df_eff['kw_h_generado'].sum()
        total_investment = df_inv['monto'].sum()
        active_projects = df_proj.shape[0]
        avg_efficiency = df_eff['indicador_economico'].mean()

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Energía Total Generada (kW/h)", f"{total_energy:,.2f}")
        col2.metric("Inversión Total (COP)", f"${total_investment:,.2f}")
        col3.metric("Proyectos Activos", active_projects)
        col4.metric("Eficiencia Económica Promedio", f"{avg_efficiency:.2f}%")

        st.markdown("<br>", unsafe_allow_html=True)

        # Gráficos Principales
        c1, c2 = st.columns(2)
        
        with c1:
            st.subheader("📊 Producción por Tipo de Energía")
            # Merge para obtener nombres de tipos
            df_merged = df_eff.merge(df_tipos, left_on='tipo_energia_id', right_on='id_tipo')
            fig_pie = px.pie(df_merged, values='kw_h_generado', names='tipo', hole=0.4, color_discrete_sequence=px.colors.sequential.Plasma)
            st.plotly_chart(fig_pie, use_container_width=True)
            
        with c2:
            st.subheader("📈 Inversión por Fuente")
            fig_bar = px.bar(df_inv, x='fuente', y='monto', color='fuente', text_auto='.2s')
            st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown("<div class='card'><h3>🗺️ Resumen de Ubicaciones</h3><p>Los proyectos están distribuidos estratégicamente en regiones clave como Andes, La Guajira, Cartagena, Cauca y Nariño, aprovechando las ventajas geográficas para cada tipo de energía.</p></div>", unsafe_allow_html=True)

# --- PÁGINA: PROYECTOS ---
elif menu == "Proyectos":
    st.title("🏗️ Gestión de Proyectos")
    if df_proj is not None:
        st.dataframe(df_proj, use_container_width=True)
        
        st.subheader("Detalle de Proyectos")
        for index, row in df_proj.iterrows():
            with st.expander(f"{row['nombre']} ({row['ubicacion']})"):
                st.write(f"**Descripción:** {row['descripcion']}")
                st.write(f"**Tipo Energía ID:** {row['tipo_energia']}")
                st.write(f"**Inicio:** {row['fecha_inicio']} | **Fin:** {row['fecha_fin']}")

# --- PÁGINA: EFICIENCIA ENERGÉTICA ---
elif menu == "Eficiencia Energética":
    st.title("📉 Análisis de Eficiencia")
    if df_eff is not None:
        # Filtros
        proj_filter = st.selectbox("Filtrar por Proyecto", df_eff['proyecto_id'].unique())
        df_filtered = df_eff[df_eff['proyecto_id'] == proj_filter]
        
        col1, col2 = st.columns(2)
        with col1:
            st.line_chart(df_filtered.set_index('fecha')['kw_h_generado'])
        with col2:
            st.line_chart(df_filtered.set_index('fecha')['indicador_economico'])
            
        st.subheader("Datos Detallados")
        st.dataframe(df_filtered, use_container_width=True)

# --- PÁGINA: INVERSIONES ---
elif menu == "Inversiones":
    st.title("💰 Inversiones y Finanzas")
    if df_inv is not None:
        total_inv = df_inv['monto'].sum()
        st.metric("Total Invertido", f"${total_inv:,.2f}")
        
        fig = px.pie(df_inv, values='monto', names='fuente', title='Distribución de Fuentes de Financiación')
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(df_inv, use_container_width=True)

# --- PÁGINA: EMPRESAS ---
elif menu == "Empresas":
    st.title("🏢 Empresas Participantes")
    if df_emp is not None:
        st.dataframe(df_emp, use_container_width=True)
        
        # Gráfico simple de industrias
        fig = px.bar(df_emp, x='nombre', y='proyecto_id', title='Empresas por Proyecto Asignado', labels={'proyecto_id': 'ID Proyecto'})
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<center>© 2024 Dashboard Sector Minero Energético Colombia. Desarrollado con Streamlit.</center>", unsafe_allow_html=True)
