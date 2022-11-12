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

        # BLOQUE DE OBSERVACIÓN DE LA ANTENA

        # Label título observación antena
        self.label_info_observacion = ttk.Label(
            self,
            style='LIO.TLabel',
            text='Ingrese los datos de la observación'
        )
        self.label_info_observacion.grid(column=0, row=8, columnspan=6, pady=20)

        # Label declinación
        self.label_declinacion = ttk.Label(
            self,
            style='LD.TLabel',
            text='Declinación = '
        )
        self.label_declinacion.grid(column=0, row=9, sticky="E", pady=10)

        # Campo de texto declinación
        self.text_declinacion = ttk.Entry(
            self,
            style="ED.TEntry",
            font=font.Font(family="Arial", size=15),
            width=10
        )
        self.text_declinacion.grid(column=1, row=9, sticky=tk.W, pady=10)

        # Label ascensión recta
        self.label_ascension_recta = ttk.Label(
            self,
            style='LAR.TLabel',
            text='Ascensión recta = '
        )
        self.label_ascension_recta.grid(column=2, row=9, sticky="E", pady=10)

        # Campo de texto ascensión recta
        self.text_ascension_recta = ttk.Entry(
            self,
            style="EAR.TEntry",
            font=font.Font(family="Arial", size=15),
            width=10
        )
        self.text_ascension_recta.grid(column=3, row=9, sticky=tk.W, pady=10)

        # Label nombre
        self.label_nombre = ttk.Label(
            self,
            style='LN.TLabel',
            text='Nombre = '
        )
        self.label_nombre.grid(column=4, row=9, sticky="E", pady=10)

        # Campo de texto nombre
        self.text_nombre = ttk.Entry(
            self,
            style="EN.TEntry",
            font=font.Font(family="Arial", size=15),
            width=10
        )
        self.text_nombre.grid(column=5, row=9, sticky=tk.W, pady=10)

        # Label cénit
        self.label_cenit = ttk.Label(
            self,
            style='LC.TLabel',
            text='Cénit = '
        )
        self.label_cenit.grid(column=0, row=10, sticky="E", pady=10)

        # Campo de texto cénit
        self.text_cenit = ttk.Entry(
            self,
            style="EC.TEntry",
            font=font.Font(family="Arial", size=15),
            width=10
        )
        self.text_cenit.grid(column=1, row=10, sticky=tk.W, pady=10)

        # Label azimut
        self.label_azimut = ttk.Label(
            self,
            style='LAz.TLabel',
            text='Azimut = '
        )
        self.label_azimut.grid(column=2, row=10, sticky="E", pady=10)

        # Campo de texto azimut
        self.text_azimut = ttk.Entry(
            self,
            style="EAz.TEntry",
            font=font.Font(family="Arial", size=15),
            width=10
        )
        self.text_azimut.grid(column=3, row=10, sticky=tk.W, pady=10)

        # Botón login
        self.boton_iniciar = ttk.Button(
            self,
            style='BI.TButton',
            text="Iniciar"
        )
        self.boton_iniciar.grid(column=0, row=11, columnspan=6, ipady=10, pady=20)

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

        self.style.configure(
            'BI.TButton',
            background='#C84941',
            foreground='white',
            font=('Roboto', 15)
        )

        # Label
        self.style.configure(
            'LIU.TLabel',
            background='white'
        )

        self.style.configure(
            'LIA.TLabel',
            font=('Roboto', 30),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LA.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LIO.TLabel',
            font=('Roboto', 30),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LD.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LAR.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LN.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LC.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LAz.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        # Entry
        self.style.configure(
            'ED.TEntry',
            padding=5
        )

        self.style.configure(
            'EAR.TEntry',
            padding=5
        )

        self.style.configure(
            'EAR.TEntry',
            padding=5
        )

        self.style.configure(
            'EN.TEntry',
            padding=5
        )

        self.style.configure(
            'EC.TEntry',
            padding=5
        )

        self.style.configure(
            'EAz.TEntry',
            padding=5
        )

