from tkinter import ttk, font
import tkinter as tk


class PanelEncabezado(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

        # CREACIÓN DE LOS WIDGETS

        # Botón atras
        self.imagen_boton = tk.PhotoImage(
            file='../assets/arrow.png'
        )

        self.boton_atras = ttk.Button(
            self,
            style='BA.TButton',
            image=self.imagen_boton
        )
        self.boton_atras.grid(column=0, row=0, padx=10, pady=15, sticky=tk.W)

        # Label icono usuario
        self.imagen_icono_usuario = tk.PhotoImage(
            file='../assets/iconoUsuario.png'
        )

        self.label_icono_usuario = ttk.Label(
            self,
            style="LIU.TLabel",
            image=self.imagen_icono_usuario
        )
        self.label_icono_usuario.grid(column=1, row=0, sticky=tk.E)

        # CONFIGURACIÓN DE ESTILOS
        self.style = ttk.Style()

        # Frame
        self.style.configure('FPE.TFrame', background='red')

        # Button
        self.style.configure(
            'BA.TButton',
            background='white',
            borderwidth=0
        )

        # Label
        self.style.configure(
            'LIU.TLabel',
            background='white'
        )


class PanelInfoAntena(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

        # CONFIGURACIÓN DE ESTILOS
        self.style = ttk.Style()

        # Frame
        self.style.configure('TFrame2', background='blue')


class PanelInfoObservacion(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

        # CONFIGURACIÓN DE ESTILOS
        self.style = ttk.Style()

        # Frame
        self.style.configure('TFrame3', background='green')
