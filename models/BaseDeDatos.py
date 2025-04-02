import sqlite3

class BaseDeDatos:
    def __init__(self, nombre_db):
        self.conexion = sqlite3.connect(nombre_db)
        self.cursor = self.conexion.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                autor TEXT,
                ano_publicacion INTEGER
            )
        ''')
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()