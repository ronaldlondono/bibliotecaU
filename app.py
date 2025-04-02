import tkinter as tk
from tkinter import ttk, messagebox
from models.BaseDeDatos import BaseDeDatos
from models.Libro import Libro
from models.GestroLibros import GestorLibros

class App:
    def __init__(self):
        self.db = BaseDeDatos('libros.db')
        self.gestor = GestorLibros(self.db)

        self.root = tk.Tk()
        self.root.title("Gestor de Libros")
        self.root.geometry("500x400")

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=5)

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = ttk.Label(self.frame, text="Gestor de Libros", font=("Arial", 16))
        self.label.pack(pady=10)

        self.boton_agregar = ttk.Button(self.frame, text="Agregar Libro", command=self.ventana_agregar)
        self.boton_agregar.pack(pady=5)
        
        self.boton_mostrar = ttk.Button(self.frame, text="Mostrar Libros", command=self.mostrar_libros)
        self.boton_mostrar.pack(pady=5)
        
        self.boton_eliminar = ttk.Button(self.frame, text="Eliminar Libro", command=self.ventana_eliminar)
        self.boton_eliminar.pack(pady=5)
        
        self.boton_actualizar = ttk.Button(self.frame, text="Actualizar Libro", command=self.ventana_actualizar)
        self.boton_actualizar.pack(pady=5)
        
        self.boton_salir = ttk.Button(self.frame, text="Salir", command=self.salir)
        self.boton_salir.pack(pady=5)
        
        self.root.mainloop()
    
    def ventana_agregar(self):
        win = tk.Toplevel(self.root)
        win.title("Agregar Libro")
        win.geometry("300x200")
        ttk.Label(win, text="Título:").pack()
        titulo = ttk.Entry(win)
        titulo.pack()
        ttk.Label(win, text="Autor:").pack()
        autor = ttk.Entry(win)
        autor.pack()
        ttk.Label(win, text="Año de publicación:").pack()
        ano_publicacion = ttk.Entry(win)
        ano_publicacion.pack()
        ttk.Button(win, text="Guardar", command=lambda: self.agregar_libro(win, titulo.get(), autor.get(), ano_publicacion.get())).pack()
    
    def agregar_libro(self, win, titulo, autor, ano_publicacion):
        if titulo and autor and ano_publicacion.isdigit():
            libro = Libro(titulo, autor, int(ano_publicacion))
            self.gestor.agregar_libro(libro)
            messagebox.showinfo("Éxito", "Libro agregado exitosamente")
            win.destroy()
        else:
            messagebox.showerror("Error", "Datos inválidos")
    
    def mostrar_libros(self):
        win = tk.Toplevel(self.root)
        win.title("Lista de Libros")
        win.geometry("800x400")
        ttk.Label(win, text="Libros en la base de datos:", font=("Arial", 14)).pack(pady=10)
        
        tree = ttk.Treeview(win, columns=("ID", "Título", "Autor", "Año"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Título", text="Título")
        tree.heading("Autor", text="Autor")
        tree.heading("Año", text="Año")
        tree.pack(fill=tk.BOTH, expand=True)
        
        for libro in self.gestor.mostrar_libros():
            tree.insert("", tk.END, values=libro)
    
    def ventana_eliminar(self):
        win = tk.Toplevel(self.root)
        win.title("Eliminar Libro")
        win.geometry("250x150")
        ttk.Label(win, text="ID del Libro a eliminar:").pack()
        libro_id = ttk.Entry(win)
        libro_id.pack()
        ttk.Button(win, text="Eliminar", command=lambda: self.eliminar_libro(win, libro_id.get())).pack()
    
    def eliminar_libro(self, win, libro_id):
        if libro_id.isdigit():
            self.gestor.eliminar_libro(int(libro_id))
            messagebox.showinfo("Éxito", "Libro eliminado exitosamente")
            win.destroy()
        else:
            messagebox.showerror("Error", "ID inválido")
    
    def ventana_actualizar(self):
        win = tk.Toplevel(self.root)
        win.title("Actualizar Libro")
        win.geometry("300x250")
        
        ttk.Label(win, text="ID del Libro:").pack()
        libro_id = ttk.Entry(win)
        libro_id.pack()
        ttk.Label(win, text="Nuevo Título:").pack()
        nuevo_titulo = ttk.Entry(win)
        nuevo_titulo.pack()
        ttk.Label(win, text="Nuevo Autor:").pack()
        nuevo_autor = ttk.Entry(win)
        nuevo_autor.pack()
        ttk.Label(win, text="Nuevo Año:").pack()
        nuevo_ano_publicacion = ttk.Entry(win)
        nuevo_ano_publicacion.pack()
        ttk.Button(win, text="Actualizar", command=lambda: self.actualizar_libro(win, libro_id.get(), nuevo_titulo.get(), nuevo_autor.get(), nuevo_ano_publicacion.get())).pack()
    
    def actualizar_libro(self, win, libro_id, nuevo_titulo, nuevo_autor, nuevo_ano_publicacion):
        if libro_id.isdigit() and nuevo_titulo and nuevo_autor and nuevo_ano_publicacion.isdigit():
            self.gestor.actualizar_libro(int(libro_id), nuevo_titulo, nuevo_autor, int(nuevo_ano_publicacion))
            messagebox.showinfo("Éxito", "Libro actualizado exitosamente")
            win.destroy()
        else:
            messagebox.showerror("Error", "Datos inválidos")
    
    def salir(self):
        self.db.cerrar()
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":
    app = App()