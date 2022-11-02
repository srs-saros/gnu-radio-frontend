import tkinter as tk
from PIL import ImageTk, Image


class Configuracion(tk.Toplevel):

    # Método constructor
    def __init__(self, ventana):
        super().__init__(ventana)

        # Establecemos el icono del programa
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open('../assets/icon.ico')))

        # Establecemos los valores de la ventana
        ancho = 1000
        alto = 729

        # Obtenemos la dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        # Encontramos el punto central de la pantalla
        centro_x = int(ancho_pantalla / 2 - ancho / 2)
        centro_y = int(alto_pantalla / 2 - alto / 2)

        # Configuración inicial de la ventana (configuración)
        self.title('Listen Astro')
        self.geometry(f'{ancho}x{alto}+{centro_x}+{centro_y}')
        self.resizable(False, False)
        self.config(background='white')