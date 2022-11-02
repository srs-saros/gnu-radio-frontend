import pyrebase
from View.configuracion_ventana import Configuracion
from tkinter.messagebox import showerror

# Configuración Firebase
firebaseConfig = {
    'apiKey': "AIzaSyBHE8vCL8OFjAvdxOOe2fD8yZZm7Dmbu34",
    'authDomain': "lisenastro.firebaseapp.com",
    'databaseURL': "https://lisenastro.firebaseio.com",
    'projectId': "lisenastro",
    'storageBucket': "lisenastro.appspot.com"
}

# Inicialización de Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


class ModeloLogin:

    def __init__(self, ventana):
        self.ventana = ventana

    # METODO LOGIN
    def login(self, usuario, contrasena):
        try:
            login = auth.sign_in_with_email_and_password(usuario, contrasena)
            self.ventana.withdraw()
            configuracion = Configuracion(self.ventana)

        except BaseException as error:
            print(showerror(title='Error', message='Lo sentimos, el usuario o la contraseña son incorrectos.'))
            print("Error", error)
