from tkinter import ttk, font
import tkinter as tk


class PanelElementos(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

        # CREACIÓN DE LOS WIDGETS

        # Botón atras
        self.imagen_boton = tk.PhotoImage(
            file='../assets/arrow3.png'
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
        self.label_icono_usuario.grid(column=5, row=0, padx=20, pady=15, sticky=tk.E)

        # Label titulo informacion antena
        self.label_info_antena = ttk.Label(
            self,
            style='LIA.TLabel',
            text='Ingrese la Información Sobre su Antena'

        )
        self.label_info_antena.grid(column=0, row=1, columnspan=6, pady=10)

        # Label antena
        self.label_antena = ttk.Label(
            self,
            style='LA.TLabel',
            text='Antena:'
        )
        self.label_antena.grid(column=0, row=2, columnspan=3, padx=5, pady=30, sticky=tk.E)

        # CONFIGURACIÓN DE ESTILOS
        self.style = ttk.Style()

        # Frame
        self.style.configure('TFrame', background='white')

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

        self.style.configure(
            'LIA.TLabel',
            font=('Roboto', 25),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LA.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )
