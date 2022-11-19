import tkinter as tk
from PIL import ImageTk, Image
from View.configuracion_panel import PanelEncabezado, PanelInformacionAntena, PanelObservacionAntena


class Configuracion(tk.Toplevel):

    # Método constructor
    def __init__(self, ventana):
        super().__init__(ventana)

        # Establecemos el icono del programa
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open('../assets/icon.ico')))

        # Establecemos los valores de la ventana
        ancho = 1500
        alto = 950

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
        # self.overrideredirect(1)
        self.config(background='white')
        self.columnconfigure(0, weight=1)

        # Creamos y agregamos los paneles a la vista (login)
        panel_encabezado = PanelEncabezado(self)
        panel_encabezado.grid(row=0, column=0, sticky=tk.EW)
        panel_encabezado.columnconfigure(0, weight=1)
        panel_encabezado.columnconfigure(1, weight=1)

        panel_informacion_antena = PanelInformacionAntena(self)
        panel_informacion_antena.grid(row=1, column=0, sticky=tk.EW)
        panel_informacion_antena.columnconfigure(0, weight=1)
        panel_informacion_antena.columnconfigure(1, weight=1)
        panel_informacion_antena.columnconfigure(2, weight=1)
        panel_informacion_antena.columnconfigure(3, weight=1)
        panel_informacion_antena.columnconfigure(4, weight=1)
        panel_informacion_antena.columnconfigure(5, weight=1)

        panel_observacion_antena = PanelObservacionAntena(self)
        panel_observacion_antena.grid(row=2, column=0, sticky=tk.EW)
        panel_observacion_antena.columnconfigure(0, weight=1)
        panel_observacion_antena.columnconfigure(1, weight=1)
        panel_observacion_antena.columnconfigure(2, weight=1)
        panel_observacion_antena.columnconfigure(3, weight=1)
        panel_observacion_antena.columnconfigure(4, weight=1)
        panel_observacion_antena.columnconfigure(5, weight=1)
