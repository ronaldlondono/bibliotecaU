import tkinter as tk
from tkinter import ttk, messagebox

class Vista:
    def __init__(self, master, controlador):
        self.master = master
        self.master.title("Gestor de Libros")
        self.master.geometry("500x400")
        self.controlador = controlador

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=5)

        self.frame = ttk.Frame(self.master, padding=20)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = ttk.Label(self.frame, text="Gestor de Libros", font=("Arial", 16))
        self.label.pack(pady=10)

        self.boton_agregar = ttk.Button(self.frame, text="Agregar Libro", command=self.ventana_agregar)
        self.boton_agregar.pack(pady=5)
        
        self.boton_mostrar = ttk.Button(self.frame, text="Mostrar Libros", command=self.controlador.mostrar_libros)
        self.boton_mostrar.pack(pady=5)
        
        self.boton_eliminar = ttk.Button(self.frame, text="Eliminar Libro", command=self.ventana_eliminar)
        self.boton_eliminar.pack(pady=5)
        
        self.boton_actualizar = ttk.Button(self.frame, text="Actualizar Libro", command=self.ventana_actualizar)
        self.boton_actualizar.pack(pady=5)
        
        self.boton_salir = ttk.Button(self.frame, text="Salir", command=self.salir)
        self.boton_salir.pack(pady=5)
    
    def ventana_agregar(self):
        win = tk.Toplevel(self.master)
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
        
        ttk.Button(win, text="Guardar", command=lambda: self.controlador.agregar_libro(titulo.get(), autor.get(), ano_publicacion.get(), win)).pack()
    
    def ventana_eliminar(self):
        win = tk.Toplevel(self.master)
        win.title("Eliminar Libro")
        win.geometry("250x150")
        
        ttk.Label(win, text="ID del Libro a eliminar:").pack()
        libro_id = ttk.Entry(win)
        libro_id.pack()
        
        ttk.Button(win, text="Eliminar", command=lambda: self.controlador.eliminar_libro(libro_id.get(), win)).pack()
    
    def ventana_actualizar(self):
        win = tk.Toplevel(self.master)
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
        
        ttk.Button(win, text="Actualizar", command=lambda: self.controlador.actualizar_libro(libro_id.get(), nuevo_titulo.get(), nuevo_autor.get(), nuevo_ano_publicacion.get(), win)).pack()
    
    def mostrar_mensaje(self, titulo, mensaje):
        """
        Muestra un cuadro de diálogo con un mensaje.
        """
        messagebox.showinfo(titulo, mensaje)
    
    def mostrar_lista_libros(self, libros):
        """
        Muestra una ventana con la lista de libros en una tabla.
        """
        win = tk.Toplevel(self.master)
        win.title("Lista de Libros")
        win.geometry("800x400")
        
        ttk.Label(win, text="Libros en la base de datos:", font=("Arial", 14)).pack(pady=10)
        
        tree = ttk.Treeview(win, columns=("ID", "Título", "Autor", "Año"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Título", text="Título")
        tree.heading("Autor", text="Autor")
        tree.heading("Año", text="Año")
        tree.pack(fill=tk.BOTH, expand=True)
        
        for libro in libros:
            tree.insert("", tk.END, values=libro)
    
    def salir(self):
        self.master.quit()
        self.master.destroy()