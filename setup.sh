mkdir -p ~/.streamlit
cp .streamlit/config.toml ~/.streamlit/config.toml

# Inicializar base de datos si no existe
if [ ! -f SectorMineroEnergeticoColombia.db ]; then
    python init_db.py
fi

# Ejecutar aplicación Streamlit
streamlit run app.py
