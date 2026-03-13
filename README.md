# ⚡ Dashboard Sector Minero Energético Colombia

> Panel de control interactivo para el análisis de proyectos energéticos y mineros en Colombia.

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

<p align="center">
  <strong>Desarrollado por 
    <a href="https://github.com/FeibertGuzman/streamlit2.git">Feibert Guzmán</a>
  </strong>
</p>

---

## 🚀 Inicio Rápido

### Instalación Local

```bash
# 1. Clonar repositorio
git clone https://github.com/FeibertGuzman/streamlit2.git
cd streamlit2

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Inicializar base de datos
python init_db.py

# 4. Ejecutar aplicación
streamlit run app.py
```

🌐 La app estará disponible en: http://localhost:8501

---

## ☁️ Deployment en Streamlit Cloud

### Pasos para desplegar la aplicación:

1. **Crear cuenta en Streamlit Cloud**
   - Ve a [streamlit.io](https://streamlit.io)
   - Regístrate con tu cuenta de GitHub

2. **Conectar repositorio de GitHub**
   - En Streamlit Cloud, selecciona "New app"
   - Autoriza el acceso a GitHub
   - Selecciona tu repositorio (streamlit2)

3. **Configurar deployment**
   - Branch: main (o la rama que prefieras)
   - Main file path: app.py
   - Streamlit detectará automáticamente:
     - `requirements.txt` para las dependencias
     - `Procfile` para los comandos de inicio

4. **Despliegue automático**
   - Streamlit Cloud ejecutará automáticamente:
     - `pip install -r requirements.txt`
     - `sh setup.sh` (desde Procfile)
   - La app se desplegará y estará disponible públicamente

📝 **Nota:** La base de datos se inicializa automáticamente en el primer ejecución mediante `setup.sh`.

---

## 📊 Módulos del Dashboard

| Módulo | Descripción |
|--------|-------------|
| 🏠 Inicio | KPIs generales, distribución energética y fuentes de inversión |
| 🏗️ Proyectos | Listado y detalles de proyectos por ubicación y tipo de energía |
| 📉 Eficiencia | Series temporales de generación, costos e indicadores económicos |
| 💰 Inversiones | Análisis de montos y fuentes de financiamiento |
| 🏢 Empresas | Actores del ecosistema y su participación por proyecto |
| 🗄️ Esquema de Datos | Estructura y relaciones de la base de datos |

---

## 🗄️ Esquema de Base de Datos

### 📦 SectorMineroEnergeticoColombia.db

```
├── tipos_energia          # Catálogo: Solar, Eólica, H2, Biomasa, Geotérmica
├── proyectos              # 5 proyectos piloto con metadata geoespacial
├── eficiencia_energetica  # 50 registros diarios: kWh, costos, KPIs
├── inversiones            # Fuentes: Gobierno, Privado, ONG
├── empresas               # Operadores por proyecto
├── comunidades_energeticas # Beneficiarios locales
├── minerales              # Recursos estratégicos asociados
└── estudios               # Estudios ambientales asociados
```

---

## 🛠️ Stack Tecnológico

- **Frontend:** Streamlit + Plotly (visualizaciones interactivas)
- **Backend:** Python 3.8+ + SQLite3
- **Data Engineering:** Pandas para ETL y análisis
- **Estilo:** CSS personalizado para UI profesional y responsive

---

## 📁 Estructura del Proyecto

```
sector_minero_energy/
├── .gitignore
├── .streamlit/
│   └── config.toml
├── app.py
├── init_db.py
├── Procfile
├── requirements.txt
├── setup.sh
├── README.md
└── SectorMineroEnergeticoColombia.sql
```

---

## 📋 Archivos de Configuración

### `.gitignore`
Excluye archivos de base de datos, entorno virtual, IDE y archivos temporales del control de versiones.

### `.streamlit/config.toml`
Configuración de Streamlit para deployment en la nube:
- Ejecución sin navegador (headless)
- Configuración de tema visual

### `Procfile`
Comando de inicio para Streamlit Cloud:
```
web: sh setup.sh
```

### `setup.sh`
Script de inicialización que:
- Configura el directorio de Streamlit
- Inicializa la base de datos si no existe
- Ejecuta la aplicación

### `requirements.txt`
Dependencias del proyecto:
- streamlit==1.31.0
- pandas==2.1.4
- plotly==5.18.0

---

## ⚡ Notas Técnicas

- Los datos en `init_db.py` están sanitizados para corregir inconsistencias del dump SQL original (espacios en números, fechas mal formadas).
- La conexión a la BD usa `@st.cache_data` para optimizar rendimiento.
- Diseño mobile-first: compatible con escritorio y dispositivos móviles.
- Para Streamlit Cloud, la base de datos se crea automáticamente en cada inicio si no existe.

---

<p align="center">
<sub>© 2024 • Dashboard Sector Minero Energético Colombia •
<a href="https://github.com/FeibertGuzman/streamlit2.git">GitHub Repo</a></sub>
</p>
