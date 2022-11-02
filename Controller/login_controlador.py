class ControladorLogin:


    # METODO CONSTRUCTOR
    def __init__(self, modelo, panel_imagen, panel_elementos):
        self.modelo = modelo
        self.panel_imagen = panel_imagen
        self.panel_elementos = panel_elementos

    def loginControlador(self, usuario, contrasena):
        try:
            self.modelo.login(usuario, contrasena)
        except BaseException as error:
            print("Ha ocurrido un error en el controlador: ", error)
