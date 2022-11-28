import tkinter as tk
from PIL import ImageTk, Image
from Model.login_modelo import ModeloLogin
from View.login_panel import PanelImagen
from View.login_panel import PanelElementos
from Controller.login_controlador import ControladorLogin


class Login(tk.Tk):

    def __init__(self):
        super().__init__()

        # Establecemos el icono del programa
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open('../assets/icon.ico')))

        # Establecemos los valores de la ventana
        self.anchoLogin = 1000
        self.altoLogin = 729

        # Obtenemos la dimensiones de la pantalla
        self.ancho_pantalla_login = self.winfo_screenwidth()
        self.alto_pantalla_login = self.winfo_screenheight()

        # Encontramos el punto central de la pantalla
        self.centro_x_login = int(self.ancho_pantalla_login / 2 - self.anchoLogin / 2)
        self.centro_y_login = int(self.alto_pantalla_login / 2 - self.altoLogin / 2)

        # Configuración inicial de la ventana (login)
        self.title('Listen Astro')
        self.geometry(f'{self.anchoLogin}x{self.altoLogin}+{self.centro_x_login}+{self.centro_y_login}')
        self.resizable(False, False)
        self.config(background='white')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Creamos y agragamos los paneles a la vista (login)
        panel_imagen = PanelImagen(self)
        panel_imagen.grid(column=0, row=0, sticky=tk.EW)

        panel_elementos = PanelElementos(self)
        panel_elementos.grid(column=1, row=0, sticky=tk.EW)

        # Creamos el modelo
        modelo = ModeloLogin(self)

        # Creamos el controlador
        controlador = ControladorLogin(modelo, panel_imagen, panel_elementos)

        # Actualizamos la referencia del controlador en los paneles
        panel_imagen.set_controlador(controlador)
        panel_elementos.set_controlador(controlador)
