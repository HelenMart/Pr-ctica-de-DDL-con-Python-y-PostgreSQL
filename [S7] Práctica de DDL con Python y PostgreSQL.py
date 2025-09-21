import psycopg2 # type: ignore

# conexión a la base de datos de postgres
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres", 
    user="postgres",    
    password="1726"   
)
cur = conn.cursor() #ejecuta comandosSQL

# crear tabla Estudiante
cur.execute("""
CREATE TABLE IF NOT EXISTS Estudiante (
    carnet INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
);
""")

# crear tabla Profesor
cur.execute("""
CREATE TABLE IF NOT EXISTS Profesor (
    carnett INTEGER PRIMARY KEY,
    nombre TEXT,
    especialidad TEXT
);
""")
print("Tablas creadas")

# agregar columnas nuevas
cur.execute("ALTER TABLE Estudiante ADD COLUMN IF NOT EXISTS correo TEXT;")
cur.execute("ALTER TABLE Profesor ADD COLUMN IF NOT EXISTS telefono TEXT;")
print("Columnas nuevas agregadas")

# renombrar columna
# cur.execute("ALTER TABLE Estudiante RENAME COLUMN nombre TO nombre_completo;")
# print("Columna renombrada")

# eliminar columna
cur.execute("ALTER TABLE Profesor DROP COLUMN IF EXISTS telefono;")
print("Columna eliminada")

# agregar restricción CHECK
# cur.execute("ALTER TABLE Estudiante ADD CONSTRAINT chk_edad CHECK (edad >= 18);")
# print("Restricción CHECK agregada")

# eliminar tabla
cur.execute("DROP TABLE IF EXISTS Profesor;")
print("Tabla eliminada")

# confirma cambios y cierra la conexión
conn.commit()
cur.close()
conn.close()
print("Conexión cerrada")
