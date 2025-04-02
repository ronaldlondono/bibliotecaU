from models.Libro import Libro
from models.BaseDeDatos import BaseDeDatos

class GestorLibros:
    def __init__(self, db):
        self.db = db
    
    def agregar_libro(self, libro):
        self.db.cursor.execute('''
            INSERT INTO libros (titulo, autor, ano_publicacion)
            VALUES (?, ?, ?)
        ''', (libro.titulo, libro.autor, libro.ano_publicacion))
        self.db.conexion.commit()

    def mostrar_libros(self):
        self.db.cursor.execute('SELECT * FROM libros')
        return self.db.cursor.fetchall()
    
    def eliminar_libro(self, libro_id):
        self.db.cursor.execute('DELETE FROM libros WHERE id = ?', (libro_id,))  
        self.db.conexion.commit()

    def actualizar_libro(self, libro_id, nuevo_titulo, nuevo_autor, nuevo_ano_publicacion):
        self.db.cursor.execute('''
            UPDATE libros
            SET titulo = ?, autor = ?, ano_publicacion = ?
            WHERE id = ?
        ''', (nuevo_titulo, nuevo_autor, nuevo_ano_publicacion, libro_id))
        self.db.conexion.commit()