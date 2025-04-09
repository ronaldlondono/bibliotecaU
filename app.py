import tkinter as tk
from views.Vista import Vista
from controllers.Controlador import Controlador

class App:
    def __init__(self):
        root = tk.Tk()
        controlador = Controlador(None)
        vista = Vista(root, controlador)
        controlador.vista = vista
        root.mainloop()

if __name__ == "__main__":
    app = App()