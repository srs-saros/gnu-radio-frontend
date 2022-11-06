from tkinter import font, ttk
import tkinter as tk


class PanelImagen(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

        # CREACIÓN DE LOS WIDGETS

        # Imagen
        self.imagen = tk.PhotoImage(
            file='../assets/backgroundLogin.png'
        )

        # Label Fondo de pantalla
        self.imagen_label = ttk.Label(
            self,
            image=self.imagen,
            background='#213A65'
        )

        self.imagen_label.grid(column=0, row=0, sticky=tk.NS)

        # Instancia controlador
        self.controlador = None

    def set_controlador(self, controlador):
        self.controlador = controlador


class PanelElementos(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

        # CREACIÓN DE LOS WIDGETS

        # Label titulo
        self.titulo_label = ttk.Label(
            self,
            style='LT.TLabel',
            text="Bienvenido a ListenAstro"
        )
        self.titulo_label.grid(column=0, row=0, pady=50)

        # Label usuario
        self.usuario_label = ttk.Label(
            self,
            style="LU.TLabel",
            text="Usuario"
        )
        self.usuario_label.grid(column=0, row=1, sticky=tk.W)

        # Campo de texto usuario
        self.usuario_text = ttk.Entry(
            self,
            style="EU.TEntry",
            font=font.Font(family="Arial", size=15),
            width=38
        )
        self.usuario_text.focus()
        self.usuario_text.grid(column=0, row=2, pady=10)

        # Label contraseña
        self.contrasena_label = ttk.Label(
            self,
            style='LC.TLabel',
            text="Contraseña"
        )
        self.contrasena_label.grid(column=0, row=3, sticky=tk.W)

        # Campo de texto contraseña
        self.contrasena_text = ttk.Entry(
            self,
            style="EC.TEntry",
            show="*",
            width=38,
            font=font.Font(family="Arial", size=15)
        )
        self.contrasena_text.grid(column=0, row=4, pady=10)

        # Boton login
        self.boton_login = ttk.Button(
            self,
            style='BL.TButton',
            text="Ingresar"
        )
        self.boton_login.grid(column=0, row=5, ipady=10, pady=20)
        self.boton_login.config(
            command=lambda: self.controlador.loginControlador(self.usuario_text.get(), self.contrasena_text.get()))

        # Instancia controlador
        self.controlador = None

        # CONFIGURACIÓN DE ESTILOS
        self.style = ttk.Style()

        # Frame
        self.style.configure('TFrame', background='white')

        # Label
        self.style.configure(
            'LT.TLabel',
            font=('Roboto', 23, 'bold'),
            background='white',
            foreground="#283758"
        )

        self.style.configure(
            'LU.TLabel',
            font=('Roboto', 15, 'bold'),
            background='white',
            foreground="#283758"
        )

        self.style.configure(
            'LC.TLabel',
            font=('Roboto', 15, 'bold'),
            background='white',
            foreground="#283758"
        )

        # Entry
        self.style.configure(
            'EU.TEntry',
            padding=5
        )

        self.style.configure(
            'EC.TEntry',
            padding=5
        )

        # Button
        self.style.configure(
            'BL.TButton',
            background='#283758',
            foreground='white',
            font=('Roboto', 15)
        )

    # MÉTODO PARA ACTUALIZAR LA REFERENCIA AL CONTROLADOR
    def set_controlador(self, controlador):
        self.controlador = controlador
