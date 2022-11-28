import tkinter as tk
from PIL import ImageTk, Image
from Model.configuracion_modelo import ModeloConfiguracion
from Controller.configuracion_controlador import ControladorConfiguracion
from View.configuracion_panel import PanelEncabezado, PanelInformacionAntena, PanelObservacionAntena


class Configuracion(tk.Toplevel):

    # Método constructor
    def __init__(self, ventana):
        super().__init__(ventana)

        # Establecemos el icono del programa
        self.tk.call('wm', 'iconphoto', self._w, ImageTk.PhotoImage(Image.open('../assets/icon.ico')))

        # Establecemos los valores de la ventana
        self.anchoConfiguracion = 1500
        self.altoConfiguracion = 950

        # Obtenemos la dimensiones de la pantalla
        self.ancho_pantalla_Configuracion = self.winfo_screenwidth()
        self.alto_pantalla_Configuracion = self.winfo_screenheight()

        # Encontramos el punto central de la pantalla
        self.centro_x_Configuracion = int(self.ancho_pantalla_Configuracion / 2 - self.anchoConfiguracion / 2)
        self.centro_y_Configuracion = int(self.alto_pantalla_Configuracion / 2 - self.altoConfiguracion / 2)

        # Configuración inicial de la ventana (configuración)
        self.title('Listen Astro')
        self.geometry(f'{self.anchoConfiguracion}x{self.altoConfiguracion}+{self.centro_x_Configuracion}+{self.centro_y_Configuracion}')
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

        # Creamos el modelo
        modelo = ModeloConfiguracion(self, ventana)

        # Creamos el controlador
        controlador = ControladorConfiguracion(modelo, panel_encabezado, panel_informacion_antena, panel_observacion_antena)

        # Actualizamos la referencia del controlador en los paneles
        panel_encabezado.set_controlador(controlador)
        panel_informacion_antena.set_controlador(controlador)
        panel_observacion_antena.set_controlador(controlador)