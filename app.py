import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import os

st.set_page_config(
    page_title="⚡ Dashboard Minero Energético Colombia",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stMetric { 
        background: white; 
        padding: 15px; 
        border-radius: 10px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    .card { 
        background: white; 
        padding: 20px; 
        border-radius: 10px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

DB_PATH = 'SectorMineroEnergeticoColombia.db'

@st.cache_data(ttl=3600)
def load_data():
    """Carga datos con validación de existencia de BD"""
    if not os.path.exists(DB_PATH):
        return None
    
    try:
        conn = sqlite3.connect(DB_PATH)
        
        tables = {
            'eficiencia': 'SELECT * FROM eficiencia_energetica',
            'proyectos': 'SELECT * FROM proyectos',
            'inversiones': 'SELECT * FROM inversiones',
            'empresas': 'SELECT * FROM empresas',
            'tipos': 'SELECT * FROM tipos_energia',
            'comunidades': 'SELECT * FROM comunidades_energeticas',
            'minerales': 'SELECT * FROM minerales'
        }
        
        data = {k: pd.read_sql_query(v, conn) for k, v in tables.items()}
        conn.close()
        return data
    except Exception as e:
        st.error(f"❌ Error cargando datos: {e}")
        return None

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2921/2921226.png", width=80)
    st.title("⚡ Menú Principal")
    page = st.radio("Navegar", ["🏠 Inicio", "🏗️ Proyectos", "📊 Eficiencia", "💰 Inversiones", "🏢 Empresas"])
    st.markdown("---")
    st.caption("Desarrollado por [Feibert Guzmán](https://github.com/FeibertGuzman)")

# Cargar datos
data = load_data()

if data is None:
    st.error("🔴 Base de datos no encontrada o con errores")
    st.info("💡 Ejecuta primero: `python init_db.py` para crear la base de datos")
    st.stop()

df_eff = data['eficiencia']
df_proj = data['proyectos']
df_inv = data['inversiones']
df_emp = data['empresas']
df_tipos = data['tipos']

# ==================== PÁGINA: INICIO ====================
if page == "🏠 Inicio":
    st.title("⚡ Dashboard Sector Minero Energético Colombia")
    st.markdown("Panel de control para monitoreo de proyectos energéticos y mineros")
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🔋 Energía Total (kW/h)", f"{df_eff['kw_h_generado'].sum():,.0f}")
    with col2:
        st.metric("💵 Inversión Total", f"${df_inv['monto'].sum():,.0f}")
    with col3:
        st.metric("🏗️ Proyectos Activos", len(df_proj))
    with col4:
        st.metric("📈 Eficiencia Promedio", f"{df_eff['indicador_economico'].mean():.1f}%")
    
    # Gráficos
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("📊 Producción por Tipo de Energía")
        df_merged = df_eff.merge(df_tipos, left_on='tipo_energia_id', right_on='id_tipo', how='left')
        fig_pie = px.pie(df_merged, values='kw_h_generado', names='tipo', 
                        hole=0.4, color_discrete_sequence=px.colors.sequential.Plasma)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with c2:
        st.subheader("💰 Inversión por Fuente")
        fig_bar = px.bar(df_inv, x='fuente', y='monto', color='fuente', text_auto='.2s')
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Tarjeta informativa
    st.markdown("""
    <div class='card'>
        <h4>🗺️ Distribución Geográfica</h4>
        <p>Proyectos estratégicos en: Andes, La Guajira, Cartagena, Cauca y Nariño.</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== PÁGINA: PROYECTOS ====================
elif page == "🏗️ Proyectos":
    st.title("🏗️ Gestión de Proyectos")
    
    for _, row in df_proj.iterrows():
        with st.expander(f"**{row['nombre']}** 📍 {row['ubicacion']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Tipo:** {row['tipo_energia']}")
                st.write(f"**Inicio:** {row['fecha_inicio']}")
            with col2:
                st.write(f"**Fin:** {row['fecha_fin']}")
                st.write(f"**Descripción:** {row['descripcion']}")
            
            # Datos asociados
            eff_proj = df_eff[df_eff['proyecto_id'] == row['id_proyecto']]
            if not eff_proj.empty:
                st.line_chart(eff_proj.set_index('fecha')['kw_h_generado'])

# ==================== PÁGINA: EFICIENCIA ====================
elif page == "📊 Eficiencia":
    st.title("📈 Análisis de Eficiencia Energética")
    
    col1, col2 = st.columns(2)
    with col1:
        proyecto_sel = st.selectbox("Seleccionar Proyecto", df_eff['proyecto_id'].unique())
    with col2:
        metrica = st.selectbox("Métrica", ['kw_h_generado', 'indicador_economico', 'costo_produccion'])
    
    df_filt = df_eff[df_eff['proyecto_id'] == proyecto_sel].copy()
    
    if not df_filt.empty and 'fecha' in df_filt.columns:
        df_filt['fecha'] = pd.to_datetime(df_filt['fecha'], errors='coerce')
        df_filt = df_filt.dropna(subset=['fecha'])
        df_filt = df_filt.sort_values('fecha')
        st.line_chart(df_filt.set_index('fecha')[metrica])
    
    with st.expander("📋 Ver datos detallados"):
        st.dataframe(df_filt, use_container_width=True)

# ==================== PÁGINA: INVERSIONES ====================
elif page == "💰 Inversiones":
    st.title("💵 Análisis de Inversiones")
    
    total = df_inv['monto'].sum()
    st.metric("💰 Total Invertido", f"${total:,.2f}")
    
    c1, c2 = st.columns(2)
    with c1:
        fig_pie = px.pie(df_inv, values='monto', names='fuente', 
                        title='Distribución por Fuente')
        st.plotly_chart(fig_pie, use_container_width=True)
    with c2:
        fig_bar = px.bar(df_inv, x='proyecto_id', y='monto', 
                        title='Inversión por Proyecto', color='fuente')
        st.plotly_chart(fig_bar, use_container_width=True)
    
    st.dataframe(df_inv, use_container_width=True)

# ==================== PÁGINA: EMPRESAS ====================
elif page == "🏢 Empresas":
    st.title("🏢 Empresas Participantes")
    
    df_full = df_emp.merge(df_proj[['id_proyecto', 'nombre', 'ubicacion']], 
                          left_on='proyecto_id', right_on='id_proyecto', how='left')
    
    st.dataframe(df_full[['nombre', 'industria', 'nombre_y', 'ubicacion']], 
                use_container_width=True,
                column_config={
                    "nombre": "Empresa",
                    "industria": "Sector",
                    "nombre_y": "Proyecto",
                    "ubicacion": "Ubicación"
                })
    
    fig = px.bar(df_emp, x='nombre', y='proyecto_id', 
                title='Empresas por Proyecto Asignado')
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<center>© 2024 • Dashboard Sector Minero Energético Colombia</center>", unsafe_allow_html=True)
