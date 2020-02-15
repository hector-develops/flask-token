import psycopg2

# Establish a connection to the database.
# Replace parameter values with database credentials.
try:
    credenciales = {
        "database": "stockline",
        "user": "postgres",
        "password": "htl20219503",
        "host": "localhost",
        "port": 5432
    }

    cnn = psycopg2.connect(**credenciales)
except psycopg2.Error as e:
    print("Error en la conexion a la base de datos", e)
