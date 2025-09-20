# 🐍 Conexión a PostgreSQL desde Python con psycopg2

Este proyecto muestra cómo conectar una aplicación Python a una base de datos PostgreSQL utilizando la biblioteca `psycopg2`. Además, se realizan múltiples operaciones de definición de datos (DDL) como creación de tablas, alteración de columnas, restricciones y eliminación de tablas, todo directamente desde el código Python.

> Ideal para quienes están aprendiendo bases de datos y desean automatizar operaciones DDL con Python.

---

## 📦 Requisitos Previos

Antes de ejecutar el código, asegúrate de tener lo siguiente instalado:

### 🔧 Software necesario

- **Python 3.7 o superior**
- **PostgreSQL** (local o en contenedor Docker)
- **pip** (administrador de paquetes de Python)
- **psycopg2** (controlador de PostgreSQL para Python)
- **Docker** (opcional, para entorno más limpio)

---

## 🐳 Instalar PostgreSQL con Docker (opcional pero recomendado)

Si no tienes PostgreSQL instalado localmente, puedes usar Docker para correr una base de datos en segundos:

```bash
docker run --name pg-database -e POSTGRES_PASSWORD=1726 -p 5432:5432 -d postgres

## 📦 Partes del fundamentales
### Creacion de una tabla

#### Tabla "Estudiante"

cur.execute("""
CREATE TABLE IF NOT EXISTS Estudiante (
    carnet INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
);
""")

####Tabla "Profesor"
cur.execute("""
CREATE TABLE IF NOT EXISTS Profesor (
    carnett INTEGER PRIMARY KEY,
    nombre TEXT,
    especialidad TEXT
);
""")

### Agregar columnas nuevas

cur.execute("ALTER TABLE Estudiante ADD COLUMN IF NOT EXISTS correo TEXT;")
cur.execute("ALTER TABLE Profesor ADD COLUMN IF NOT EXISTS telefono TEXT;")
print("Columnas nuevas agregadas")

### Renombrar columna
cur.execute("ALTER TABLE Estudiante RENAME COLUMN nombre TO nombre_completo;")
print("Columna renombrada")

### Eliminar columna
cur.execute("ALTER TABLE Profesor DROP COLUMN IF EXISTS telefono;")
print("Columna eliminada")

### Agregar restricción CHECK
cur.execute("ALTER TABLE Estudiante ADD CONSTRAINT chk_edad CHECK (edad >= 18);")
print("Restricción CHECK agregada")

### Eliminar tabla
cur.execute("DROP TABLE IF EXISTS Profesor;")
print("Tabla eliminada")

### Confirma cambios y cierra la conexión
conn.commit()
cur.close()
conn.close()
