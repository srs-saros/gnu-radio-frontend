class ControladorConfiguracion:

    # METODO CONSTRUCTOR
    def __init__(self, modelo, panel_encabezado, panel_informacion_antena, panel_observacion_antena):
        self.modelo = modelo
        self.panel_encabezado = panel_encabezado
        self.panel_informacion_antena = panel_informacion_antena
        self.panel_observacion_antena = panel_observacion_antena

    def botonAtras(self):
        try:
            self.modelo.atras()
        except BaseException as error:
            print("Ha ocurrido un error en el controlador: ", error)


