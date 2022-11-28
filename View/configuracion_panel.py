from tkinter import ttk, font
import tkinter as tk


class PanelEncabezado(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

        # CREACIÓN DE LOS WIDGETS

        # ENCABEZADO PANEL
        # Botón atras
        self.imagen_boton = tk.PhotoImage(
            file='../assets/exit.png'
        )

        self.boton_atras = ttk.Button(
            self,
            style='BA.TButton',
            image=self.imagen_boton
        )
        self.boton_atras.grid(column=0, row=0, padx=10, pady=15, sticky=tk.W)
        self.boton_atras.config(
            command=lambda: self.controlador.botonAtras())

        # Label icono usuario
        self.imagen_icono_usuario = tk.PhotoImage(
            file='../assets/iconoUsuario.png'
        )

        self.label_icono_usuario = ttk.Label(
            self,
            style="LIU.TLabel",
            image=self.imagen_icono_usuario
        )
        self.label_icono_usuario.grid(column=1, row=0, padx=20, pady=15, sticky=tk.E)

        # Label titulo informacion antena
        self.label_info_antena = ttk.Label(
            self,
            style='LIA.TLabel',
            text='Ingrese la Información Sobre su Antena'

        )
        self.label_info_antena.grid(column=0, row=1, columnspan=2, pady=20)

        # Label antena
        self.label_antena = ttk.Label(
            self,
            style='LA.TLabel',
            text='Antena: '
        )
        self.label_antena.grid(column=0, row=2, pady=30, sticky=tk.E)

        # Combobox antena
        self.combobox_valor = tk.StringVar()

        self.combobox_antena = ttk.Combobox(
            self,
            style='CA.TCombobox',
            width=30,
            justify='center',
            textvariable=self.combobox_valor
        )

        self.combobox_antena['values'] = ['Antena Sergio Arboleda', 'Otra']

        self.combobox_antena['state'] = 'readonly'

        self.combobox_antena.focus()

        self.combobox_antena.grid(column=1, row=2, pady=30, sticky=tk.W)

        # Instancia controlador
        self.controlador = None

        # CONFIGURACIÓN DE ESTILOS
        self.style = ttk.Style()

        # Frame
        self.style.configure('TFrame', background='White')

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

        # Combobox
        self.style.configure(
            'CA.TCombobox',
            bordercolor='#283758',
            selectbackground='#d9d9d9',
            foreground='black',
            selectforeground='black',
            selectborderwidth=0,
            padding=5

        )

    # MÉTODO PARA ACTUALIZAR LA REFERENCIA AL CONTROLADOR
    def set_controlador(self, controlador):
        self.controlador = controlador


class PanelInformacionAntena(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

        # CREACIÓN DE LOS WIDGETS

        # BLOQUES DE INFORMACIÓN DE LA ANTENA
        # Label Alias
        self.label_alias = ttk.Label(
            self,
            style='LAL.TLabel',
            text='Alias = '
        )
        self.label_alias.grid(column=1, row=3, pady=10, sticky=tk.E)

        # Entry Alias
        self.entry_alias = ttk.Entry(
            self,
            style='EA.TEntry',
            font=font.Font(family="Arial", size=12),
            width=25
        )
        self.entry_alias.grid(column=2, row=3, pady=10, sticky=tk.W)

        # Label valor ROE
        self.label_ROE = ttk.Label(
            self,
            style='LROE.TLabel',
            text='ROE = '
        )
        self.label_ROE.grid(column=3, row=3, pady=10, sticky=tk.E)

        # Entry valor ROE
        self.entry_ROE = ttk.Entry(
            self,
            style='EROE.TEntry',
            font=font.Font(family="Arial", size=12),
            width=25
        )
        self.entry_ROE.grid(column=4, row=3, pady=10, sticky=tk.W)

        # Label localizaciòn
        self.label_localizacion = ttk.Label(
            self,
            style='LL.TLabel',
            text='Localización = '
        )
        self.label_localizacion.grid(column=1, row=4, pady=10, sticky=tk.E)

        # Entry localización
        self.entry_localizacion = ttk.Entry(
            self,
            style='EL.TEntry',
            font=font.Font(family="Arial", size=12),
            width=25
        )
        self.entry_localizacion.grid(column=2, row=4, pady=10, sticky=tk.W)

        # Label ganancia
        self.label_ganancia = ttk.Label(
            self,
            style='LG.TLabel',
            text='Ganancia = '
        )
        self.label_ganancia.grid(column=3, row=4, pady=10, sticky=tk.E)

        # Entry ganancia
        self.entry_ganacia = ttk.Entry(
            self,
            style='EG.TEntry',
            font=font.Font(family="Arial", size=12),
            width=25
        )
        self.entry_ganacia.grid(column=4, row=4, pady=10, sticky=tk.W)

        # Label tamaño
        self.label_tamaño = ttk.Label(
            self,
            style='LTT.TLabel',
            text='Tamaño = '
        )
        self.label_tamaño.grid(column=1, row=5, pady=10, sticky=tk.E)

        # Entry tamaño
        self.entry_tamaño = ttk.Entry(
            self,
            style='ET.TEntry',
            font=font.Font(family="Arial", size=12),
            width=25
        )
        self.entry_tamaño.grid(column=2, row=5, pady=10, sticky=tk.W)

        # Label impedancia
        self.label_impedancia = ttk.Label(
            self,
            style='LIM.TLabel',
            text='Impedancia = '
        )
        self.label_impedancia.grid(column=1, row=6, pady=10, sticky=tk.E)

        # Entry impedancia
        self.entry_impedancia = ttk.Entry(
            self,
            style='EIM.TEntry',
            font=font.Font(family="Arial", size=12),
            width=25
        )
        self.entry_impedancia.grid(column=2, row=6, pady=10, sticky=tk.W)

        # Botón guardar

        self.button_guardar = ttk.Button(
            self,
            style='BG.TButton',
            text='Guardar'
        )
        self.button_guardar.grid(column=0, row=7, columnspan=6, ipadx=15, ipady=5, pady=35)

        # Instancia controlador
        self.controlador = None

        # CONFIGURACIÓN DE ESTILOS
        self.style = ttk.Style()

        # Frame
        self.style.configure('TFrame', background='White')

        # Label
        self.style.configure(
            'LAL.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LROE.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LL.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LG.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LTT.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        self.style.configure(
            'LIM.TLabel',
            font=('Roboto', 15),
            background='white',
            foreground="#000000"
        )

        # Entry
        self.style.configure(
            'EA.TEntry',
            padding=5
        )

        self.style.configure(
            'EROE.TEntry',
            padding=5
        )

        self.style.configure(
            'EL.TEntry',
            padding=5
        )

        self.style.configure(
            'EG.TEntry',
            padding=5
        )

        self.style.configure(
            'ET.TEntry',
            padding=5
        )

        self.style.configure(
            'EIM.TEntry',
            padding=5
        )

        # Button
        self.style.configure(
            'BG.TButton',
            background='#C84941',
            foreground='white',
            font=('Roboto', 15)
        )

    # MÉTODO PARA ACTUALIZAR LA REFERENCIA AL CONTROLADOR
    def set_controlador(self, controlador):
        self.controlador = controlador


class PanelObservacionAntena(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

        # CREACIÓN DE LOS WIDGETS

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
        self.label_declinacion.grid(column=0, row=9, sticky=tk.E, pady=10)

        # Campo de texto declinación
        self.text_declinacion = ttk.Entry(
            self,
            style="ED.TEntry",
            font=font.Font(family="Arial", size=12),
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
            font=font.Font(family="Arial", size=12),
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
            font=font.Font(family="Arial", size=12),
            width=10
        )
        self.text_nombre.grid(column=5, row=9, sticky=tk.W, pady=10)

        # Label cénit
        self.label_cenit = ttk.Label(
            self,
            style='LCE.TLabel',
            text='Cénit = '
        )
        self.label_cenit.grid(column=0, row=10, sticky="E", pady=10)

        # Campo de texto cénit
        self.text_cenit = ttk.Entry(
            self,
            style="EC.TEntry",
            font=font.Font(family="Arial", size=12),
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
            font=font.Font(family="Arial", size=12),
            width=10
        )
        self.text_azimut.grid(column=3, row=10, sticky=tk.W, pady=10)

        # Botón iniciar
        self.boton_iniciar = ttk.Button(
            self,
            style='BI.TButton',
            text="Iniciar"
        )
        self.boton_iniciar.grid(column=0, row=11, columnspan=6, ipadx=15, ipady=5, pady=35)

        # Instancia controlador
        self.controlador = None

        # CONFIGURACIÓN DE ESTILOS
        self.style = ttk.Style()

        # Frame
        self.style.configure('TFrame', background='White')

        # Label
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
            'LCE.TLabel',
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

        self.style.configure(
            'BI.TButton',
            background='#C84941',
            foreground='white',
            font=('Roboto', 15)
        )

    # MÉTODO PARA ACTUALIZAR LA REFERENCIA AL CONTROLADOR
    def set_controlador(self, controlador):
        self.controlador = controlador
