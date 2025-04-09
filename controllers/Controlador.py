from models.GestorLibros import GestorLibros
from models.Libro import Libro
from models.BaseDeDatos import BaseDeDatos

class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.db = BaseDeDatos('libros.db')
        self.gestor = GestorLibros(self.db)
    
    def agregar_libro(self, titulo, autor, ano_publicacion, ventana):
        if titulo and autor and ano_publicacion.isdigit():
            libro = Libro(titulo, autor, int(ano_publicacion))
            self.gestor.agregar_libro(libro)
            self.vista.mostrar_mensaje("Éxito", "Libro agregado exitosamente")
            ventana.destroy()
        else:
            self.vista.mostrar_mensaje("Error", "Datos inválidos")
    
    def mostrar_libros(self):
        libros = self.gestor.mostrar_libros()
        self.vista.mostrar_lista_libros(libros)
    
    def eliminar_libro(self, libro_id, ventana):
        if libro_id.isdigit():
            self.gestor.eliminar_libro(int(libro_id))
            self.vista.mostrar_mensaje("Éxito", "Libro eliminado exitosamente")
            ventana.destroy()
        else:
            self.vista.mostrar_mensaje("Error", "ID inválido")
    
    def actualizar_libro(self, libro_id, nuevo_titulo, nuevo_autor, nuevo_ano_publicacion, ventana):
        if libro_id.isdigit() and nuevo_titulo and nuevo_autor and nuevo_ano_publicacion.isdigit():
            self.gestor.actualizar_libro(int(libro_id), nuevo_titulo, nuevo_autor, int(nuevo_ano_publicacion))
            self.vista.mostrar_mensaje("Éxito", "Libro actualizado exitosamente")
            ventana.destroy()
        else:
            self.vista.mostrar_mensaje("Error", "Datos inválidos")