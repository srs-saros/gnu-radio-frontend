from tkinter import font, ttk
import tkinter as tk


class PanelImagen(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

        # CREACIÓN DE LOS WIDGETS

        # Imagen
        self.imagen = tk.PhotoImage(
            file='../assets/backgroundLogin.png')

        # Label Fondo de pantalla
        self.imagen_label = ttk.Label(
            self,
            image=self.imagen,
            background='#213A65'
        )

        self.imagen_label.pack()

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
            text="Welcome to ListenAstro",
            font="Roboto 25 bold",
            background='white'

        )
        self.titulo_label.grid(column=0, row=3, padx=15, ipady=50)

        # Label usuario
        self.usuario_label = ttk.Label(
            self,
            text="Usuario",
            font="Roboto 15 bold",
            background='white'
        )
        self.usuario_label.grid(column=0, row=5, padx=25, sticky=tk.W)

        # Campo de texto usuario
        self.usuario_text = ttk.Entry(
            self,
            style="EU.TEntry",
            width=40,
            font=font.Font(family="Arial", size=15)
        )
        self.usuario_text.focus()
        self.usuario_text.grid(column=0, row=6, pady=10)

        # Label contraseña
        self.contrasena_label = ttk.Label(
            self,
            text="Contraseña",
            font="Roboto 15 bold",
            background='white'
        )
        self.contrasena_label.grid(column=0, row=8, padx=25, ipady=10, sticky=tk.W)

        # Campo de texto contraseña
        self.contrasena_text = ttk.Entry(
            self,
            style="EC.TEntry",
            show="*",
            width=40,
            font=font.Font(family="Arial", size=15)
        )
        self.contrasena_text.grid(column=0, row=9, pady=10)

        # Boton login
        self.boton_login = tk.Button(
            self,
            text="Ingresar",
            background='#283758',
            foreground='white',
            font="Roboto 15"
        )
        self.boton_login.grid(column=0, row=11, ipady=10, ipadx=20, pady=30)
        self.boton_login.config(
            command=lambda: self.controlador.loginControlador(self.usuario_text.get(), self.contrasena_text.get()))

        # Instancia controlador
        self.controlador = None

        # CONFIGURACIÓN DE ESTILOS
        self.style = ttk.Style()

        # Frame
        self.style.configure('TFrame', background='white')

        # Entry
        self.style.configure(
            'EU.TEntry',
            padding=5
        )
        self.style.configure(
            'EC.TEntry',
            padding=5
        )

    # MÉTODO PARA ACTUALIZAR LA REFERENCIA AL CONTROLADOR
    def set_controlador(self, controlador):
        self.controlador = controlador
