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

🌐 La app estará disponible en: http://localhost:8501
📊 Módulos del Dashboard
Módulo
Descripción
🏠 Inicio
KPIs generales, distribución energética y fuentes de inversión
🏗️ Proyectos
Listado y detalles de proyectos por ubicación y tipo de energía
📉 Eficiencia
Series temporales de generación, costos e indicadores económicos
💰 Inversiones
Análisis de montos y fuentes de financiamiento
🏢 Empresas
Actores del ecosistema y su participación por proyecto
🗄️ Esquema de Datos
12345678910
📦 SectorMineroEnergeticoColombia.db
 ├── tipos_energia          # Catálogo: Solar, Eólica, H2, Biomasa, Geotérmica
 ├── proyectos              # 5 proyectos piloto con metadata geoespacial
 ├── eficiencia_energetica  # 50 registros diarios: kWh, costos, KPIs
 ├── inversiones            # Fuentes: Gobierno, Privado, ONG
 ├── empresas               # Operadores por proyecto
 ├── comunidades_energeticas # Beneficiarios locales
 ├── minerales              # Recursos estratégicos asociados
 ├── estu
🛠️ Stack Tecnológico
Frontend: Streamlit + Plotly (visualizaciones interactivas)
Backend: Python 3.8+ + SQLite3
Data Engineering: Pandas para ETL y análisis
Estilo: CSS personalizado para UI profesional y responsive
📁 Estructura del Proyecto
123456
sector_minero_energy/
├── app.py                   # Dashboard principal
├── init_db.py               # Script de inicialización de datos
├── requirements.txt         # Dependencias Python
├── README.md                # Este archivo
└── SectorMineroEnergeticoColombia.sql  # Script SQL original
⚡ Notas Técnicas
Los datos en init_db.py están sanitizados para corregir inconsistencias del dump SQL original (espacios en números, fechas mal formadas).
La conexión a la BD usa @st.cache_data para optimizar rendimiento.
Diseño mobile-first: compatible con escritorio y dispositivos móviles.
<p align="center">
<sub>© 2024 • Dashboard Sector Minero Energético Colombia •
<a href="https://github.com/FeibertGuzman/streamlit2.git">GitHub Repo</a></sub>
</p>
```

✅ Mejoras aplicadas:
Antes
Ahora
Texto plano extenso
Badges visuales + tablas + código embebido
Instrucciones dispersas
Sección "Inicio Rápido" con 4 pasos claros
Descripción genérica
Tabla de módulos con iconos y propósitos
Sin esquema de datos
Diagrama visual de la estructura de la BD
Footer simple
Badges + enlace GitHub + copyright profesional
💡 Tip: Puedes personalizar los badges adicionales según necesites:
markdown
12
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge)
¿Te gustaría que agregue una sección de "Próximas Mejoras" o un diagrama de arquitectura en el README? 🎨
pero porfa solo un archivo todo tipo markdown para copiar y pegar 

Pensamiento completado
markdown
1234567891011121314151617181920212223242526272829303132333435
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


## 🌐 La app estará disponible en: http://localhost:8501
### 📊 Módulos del Dashboard
Módulo
Descripción
## 🏠 Inicio
KPIs generales, distribución energética y fuentes de inversión
## 🏗️ Proyectos
Listado y detalles de proyectos por ubicación y tipo de energía
## 📉 Eficiencia
Series temporales de generación, costos e indicadores económicos
## 💰 Inversiones
Análisis de montos y fuentes de financiamiento
## 🏢 Empresas
Actores del ecosistema y su participación por proyecto
## 🗄️ Esquema de Datos

### 📦 SectorMineroEnergeticoColombia.db
 ├── tipos_energia          # Catálogo: Solar, Eólica, H2, Biomasa, Geotérmica
 ├── proyectos              # 5 proyectos piloto con metadata geoespacial
 ├── eficiencia_energetica  # 50 registros diarios: kWh, costos, KPIs
 ├── inversiones            # Fuentes: Gobierno, Privado, ONG
 ├── empresas               # Operadores por proyecto
 ├── comunidades_energeticas # Beneficiarios locales
 ├── minerales              # Recursos estratégicos asociados
 ├── estu

## 🛠️ Stack Tecnológico
Frontend: Streamlit + Plotly (visualizaciones interactivas)
Backend: Python 3.8+ + SQLite3
Data Engineering: Pandas para ETL y análisis
Estilo: CSS personalizado para UI profesional y responsive

## 📁 Estructura del Proyecto

sector_minero_energy/
├── app.py                   # Dashboard principal
├── init_db.py               # Script de inicialización de datos
├── requirements.txt         # Dependencias Python
├── README.md                # Este archivo
└── SectorMineroEnergeticoColombia.sql  # Script SQL original

## ⚡ Notas Técnicas

-> Los datos en init_db.py están sanitizados para corregir inconsistencias del dump SQL original (espacios en números, fechas mal formadas).
La conexión a la BD usa @st.cache_data para optimizar rendimiento.
Diseño mobile-first: compatible con escritorio y dispositivos móviles.
<p align="center">
<sub>© 2024 • Dashboard Sector Minero Energético Colombia •
<a href="https://github.com/FeibertGuzman/streamlit2.git">GitHub Repo</a></sub>
</p>
