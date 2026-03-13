import sqlite3
import os
import re

DB_NAME = 'SectorMineroEnergeticoColombia.db'

def clean_value(val):
    """Limpia espacios extraños en valores numéricos y texto"""
    if val is None:
        return None
    if isinstance(val, (int, float)):
        return val
    # Remover espacios extra en números y fechas
    cleaned = re.sub(r'(\d)\s+(\d)', r'\1\2', str(val).strip())
    return cleaned

def create_db():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print("🗑️ Base de datos anterior eliminada.")
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Crear tablas
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS tipos_energia (
        id_tipo INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS proyectos (
        id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        tipo_energia INTEGER,
        ubicacion TEXT,
        fecha_inicio DATE,
        fecha_fin DATE,
        FOREIGN KEY (tipo_energia) REFERENCES tipos_energia(id_tipo)
    );

    CREATE TABLE IF NOT EXISTS eficiencia_energetica (
        id_eficiencia INTEGER PRIMARY KEY AUTOINCREMENT,
        proyecto_id INTEGER,
        tipo_energia_id INTEGER,
        fecha DATE,
        kw_h_generado REAL,
        costo_produccion REAL,
        costo_comercializacion REAL,
        tiempos_muertos INTEGER,
        clima TEXT,
        indicador_economico REAL,
        indicador_sociodemografico REAL,
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id_proyecto),
        FOREIGN KEY (tipo_energia_id) REFERENCES tipos_energia(id_tipo)
    );

    CREATE TABLE IF NOT EXISTS inversiones (
        id_inversion INTEGER PRIMARY KEY AUTOINCREMENT,
        proyecto_id INTEGER,
        monto REAL,
        fuente TEXT,
        fecha DATE,
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id_proyecto)
    );

    CREATE TABLE IF NOT EXISTS empresas (
        id_empresa INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        industria TEXT,
        proyecto_id INTEGER,
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id_proyecto)
    );

    CREATE TABLE IF NOT EXISTS comunidades_energeticas (
        id_comunidad INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        ubicacion TEXT,
        proyecto_asociado INTEGER,
        FOREIGN KEY (proyecto_asociado) REFERENCES proyectos(id_proyecto)
    );

    CREATE TABLE IF NOT EXISTS minerales (
        id_mineral INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        ubicacion TEXT,
        proyecto_asociado INTEGER,
        FOREIGN KEY (proyecto_asociado) REFERENCES proyectos(id_proyecto)
    );

    CREATE TABLE IF NOT EXISTS estudios (
        id_estudio INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        fecha DATE,
        proyecto_id INTEGER,
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id_proyecto)
    );

    CREATE TABLE IF NOT EXISTS investigadores (
        id_investigador INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        especialidad TEXT,
        proyecto_id INTEGER,
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id_proyecto)
    );
    """)

    # Tipos de energía
    tipos = [
        (1, 'Hidrógeno Verde'), (2, 'Eólica'), (3, 'Solar'), 
        (4, 'Biomasa'), (5, 'Geotérmica')
    ]
    cursor.executemany("INSERT INTO tipos_energia VALUES (?, ?)", tipos)

    # Proyectos
    proyectos = [
        (1, 'Proyecto Solar Andes', 'Desarrollo de una planta de energía solar', 3, 'Andes', '2022-01-01', '2023-01-01'),
        (2, 'Parque Eólico La Guajira', 'Generación de energía eólica', 2, 'La Guajira', '2021-05-01', '2022-12-01'),
        (3, 'Planta Hidrógeno Verde', 'Producción de hidrógeno verde', 1, 'Cartagena', '2023-03-01', '2024-03-01'),
        (4, 'Proyecto Biomasa Cauca', 'Generación de energía a partir de biomasa', 4, 'Cauca', '2022-06-01', '2023-06-01'),
        (5, 'Planta Geotérmica Nariño', 'Producción de energía geotérmica', 5, 'Nariño', '2023-01-01', '2024-01-01')
    ]
    cursor.executemany("INSERT INTO proyectos VALUES (?,?,?,?,?,?,?)", proyectos)

    # Eficiencia energética - Datos limpios (50 registros corregidos)
    eficiencia = []
    
    # Proyecto 1: Solar (10 registros)
    for i in range(1, 11):
        kw = 1500.0 + (i-1) * 2 if i <= 5 else 1500.0 - (i-5) * 2
        eficiencia.append((i, 1, 3, f'2022-01-{i:02d}', kw, 
                          100000 + i*1000, 5000 + i*100, i%3, 
                          'Soleado' if i%2==0 else 'Nublado', 
                          80.0 + i*0.5, 70.0 + i*0.5))
    
    # Proyecto 2: Eólica (10 registros)
    for i in range(1, 11):
        kw = 2000.0 + (i-1) * 2 if i <= 5 else 2000.0 - (i-5) * 2
        eficiencia.append((10+i, 2, 2, f'2021-06-{i:02d}', kw,
                          150000 + i*1000, 8000 + i*100, i%3,
                          'Ventoso' if i%2==0 else 'Lluvioso',
                          85.0 + i*0.5, 65.0 + i*0.5))
    
    # Proyecto 3: Hidrógeno (10 registros)
    for i in range(1, 11):
        kw = 1800.0 + (i-1) * 2 if i <= 5 else 1800.0 - (i-5) * 2
        eficiencia.append((20+i, 3, 1, f'2023-04-{i:02d}', kw,
                          120000 + i*1000, 6000 + i*100, i%3,
                          'Soleado' if i%2==0 else 'Lluvioso',
                          75.0 + i*0.5, 72.0 + i*0.5))
    
    # Proyecto 4: Biomasa (10 registros)
    for i in range(1, 11):
        kw = 1600.0 + (i-1) * 2 if i <= 5 else 1600.0 - (i-5) * 2
        eficiencia.append((30+i, 4, 4, f'2022-07-{i:02d}', kw,
                          110000 + i*1000, 7000 + i*100, i%3,
                          'Soleado' if i%2==0 else 'Nublado',
                          78.0 + i*0.5, 68.0 + i*0.5))
    
    # Proyecto 5: Geotérmica (10 registros)
    for i in range(1, 11):
        kw = 1700.0 + (i-1) * 2 if i <= 5 else 1700.0 - (i-5) * 2
        eficiencia.append((40+i, 5, 5, f'2023-02-{i:02d}', kw,
                          130000 + i*1000, 7500 + i*100, i%3,
                          'Frío' if i%2==0 else 'Nublado',
                          82.0 + i*0.5, 70.0 + i*0.5))
    
    cursor.executemany("""INSERT INTO eficiencia_energetica 
        VALUES (?,?,?,?,?,?,?,?,?,?,?)""", eficiencia)

    # Inversiones
    inversiones = [
        (1, 1, 1000000.00, 'Gobierno', '2022-01-01'),
        (2, 2, 5000000.00, 'Privado', '2021-06-01'),
        (3, 3, 2000000.00, 'Gobierno', '2023-04-01'),
        (4, 4, 1500000.00, 'ONG', '2022-07-01'),
        (5, 5, 3000000.00, 'Privado', '2023-02-01')
    ]
    cursor.executemany("INSERT INTO inversiones VALUES (?,?,?,?,?)", inversiones)

    # Empresas
    empresas = [
        (1, 'SolarTech', 'Energía Solar', 1),
        (2, 'WindPower', 'Energía Eólica', 2),
        (3, 'GreenH2', 'Hidrógeno Verde', 3),
        (4, 'BioEnergy', 'Biomasa', 4),
        (5, 'GeoEnergy', 'Geotermia', 5)
    ]
    cursor.executemany("INSERT INTO empresas VALUES (?,?,?,?)", empresas)

    # Comunidades
    comunidades = [
        (1, 'Comunidad Solar Andes', 'Comunidad que utiliza energía solar', 'Andes', 1),
        (2, 'Comunidad Eólica La Guajira', 'Comunidad que utiliza energía eólica', 'La Guajira', 2),
        (3, 'Comunidad Biomasa Cauca', 'Comunidad que utiliza energía de biomasa', 'Cauca', 4),
        (4, 'Comunidad Geotérmica Nariño', 'Comunidad que utiliza energía geotérmica', 'Nariño', 5)
    ]
    cursor.executemany("INSERT INTO comunidades_energeticas VALUES (?,?,?,?,?)", comunidades)

    # Minerales
    minerales = [
        (1, 'Litio', 'Mineral estratégico para baterías', 'Cauca', 1),
        (2, 'Cobalto', 'Mineral estratégico para componentes electrónicos', 'Boyacá', 2),
        (3, 'Níquel', 'Mineral estratégico para aleaciones metálicas', 'Antioquia', 3),
        (4, 'Cobre', 'Mineral estratégico para conductividad eléctrica', 'Chocó', 4),
        (5, 'Uranio', 'Mineral estratégico para energía nuclear', 'Guainía', 5)
    ]
    cursor.executemany("INSERT INTO minerales VALUES (?,?,?,?,?)", minerales)

    # Estudios
    estudios = [
        (1, 'Estudio de Viabilidad Solar', 'Análisis de viabilidad para la planta solar en Andes', '2021-12-01', 1),
        (2, 'Impacto Ambiental Eólico', 'Evaluación del impacto ambiental del parque eólico en La Guajira', '2020-11-01', 2),
        (3, 'Producción de Hidrógeno', 'Estudio de métodos de producción de hidrógeno verde', '2022-05-01', 3),
        (4, 'Biomasa y Sostenibilidad', 'Análisis de sostenibilidad de la planta de biomasa en Cauca', '2021-09-01', 4),
        (5, 'Eficiencia Geotérmica', 'Estudio de eficiencia de la planta geotérmica en Nariño', '2023-03-01', 5)
    ]
    cursor.executemany("INSERT INTO estudios VALUES (?,?,?,?,?)", estudios)

    # Investigadores
    investigadores = [
        (1, 'Juan', 'Pérez', 'Energía Solar', 1),
        (2, 'Ana', 'Gómez', 'Energía Eólica', 2),
        (3, 'Luis', 'Martínez', 'Hidrógeno Verde', 3),
        (4, 'María', 'Rodríguez', 'Biomasa', 4),
        (5, 'Carlos', 'López', 'Geotermia', 5)
    ]
    cursor.executemany("INSERT INTO investigadores VALUES (?,?,?,?,?)", investigadores)

    conn.commit()
    conn.close()
    print(f"✅ Base de datos '{DB_NAME}' creada exitosamente con {len(eficiencia)} registros de eficiencia.")

if __name__ == "__main__":
    create_db()
