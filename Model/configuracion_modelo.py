from tkinter.messagebox import showerror


class ModeloConfiguracion:

    def __init__(self, ventanaConfiguracion, ventanaLogin):
        self.ventanaConfiguracion = ventanaConfiguracion
        self.ventanaLogin = ventanaLogin

    def atras(self):
        self.ventanaConfiguracion.destroy()
        self.ventanaLogin.destroy()
