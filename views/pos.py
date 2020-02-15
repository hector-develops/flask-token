import psycopg2
from basesdatos.postgrresql import cnn as connection


def pos():
    try:

        cursor = connection.cursor()
        cursor.execute(""" SELECT * from tbl_pos_stockline """)

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error ocurrido en pos", e)

    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Conexion cerrada")

pos()