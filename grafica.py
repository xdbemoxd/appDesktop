import sys
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import ( QWidget, QHBoxLayout, QCheckBox, QFormLayout,
                                QApplication, QLabel, QLineEdit, QPushButton, QMessageBox )
from PySide6.QtGui import QFont

from registroUsuario import VentanaRegistroView
from mainNuevo import MainWindows

class NuevaInterfaz( QWidget ):
    
    def mostrarClave( self, clicked ):
        if clicked:
            self.passWordInput.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.passWordInput.setEchoMode( #oculta los datos ingresados, si lo colocas normal, se vera la los datos ingresados
                QLineEdit.EchoMode.Password
            )
    
    def mainWindows( self ):
        self.usuarioIniciado = MainWindows()
        self.usuarioIniciado.show()

    def ventanaPrincipal( self ):
        usuarios = []
        archivoUsuarios = "datos.txt"
        try:
            with open( archivoUsuarios, "r" ) as f:
                for linea in f:
                    usuarios.append( linea.strip("\n") )
            
            datosUsuario = f"{ self.userInput.text() },{ self.passWordInput.text() }"
            if datosUsuario in usuarios :
                QMessageBox.information( self, 'Inicio de sesion', #creacion de ventanas informativas o emergentes
                                        'Inicio de sesion exitoso',
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok )  
                self.estaLogueado= True
                self.close()
                self.mainWindows()
            else:
                QMessageBox.warning( self, "Error de inicio",
                                    "Credemciales incorrectas",
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close )
            
            
        except FileNotFoundError as e:
             QMessageBox.warning( self, "Error de inicio",
                                    "Base de dato de usuario no encontrada: {e}",
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)
             sys.exit( app.exec() )
             
        except Exception as e:
            QMessageBox.warning( self, "Error de inicio", 
                                "Error en el servidor: {e}",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
            sys.exit( app.exec() )

    def ventanaRegistro( self ):
        self.nuevoUsuario = VentanaRegistroView()
        self.nuevoUsuario.show()
        
    def primeraVentana( self ):

        #primera parte de la ventana, donde se ingresan el nombre del usuario
        tituloPrincipalLabel = QLabel( "Usuario:" )#donde se imprimen los datos
        tituloPrincipalLabel.setFont( QFont( 'times new roman', 15 ) )
       
        self.userInput = QLineEdit( self )#donde se cargan los datos
        self.userInput.setPlaceholderText( "Usuario" )
        
        #aqui se ingresa la contraseña del usuario
        passWordLabel=QLabel( "Clave:" )
        passWordLabel.setFont( QFont( 'times new roman', 15 ) )
        self.passWordInput= QLineEdit( self )
        self.passWordInput.setPlaceholderText( "clave" )
        self.passWordInput.setEchoMode( #oculta los datos ingresados, si lo colocas normal, se vera la los datos ingresados
                QLineEdit.EchoMode.Password
        )
       
        self.mirarContraseña= QCheckBox( "Ver Contraseña" )
        self.mirarContraseña.toggled.connect( self.mostrarClave )#toggled ayuda a saber si esta presionado el QCheckBox

        #boton de ingreso a la app
        self.botonIngreso = QPushButton( 'Ingresar')
        self.botonIngreso.clicked.connect( self.ventanaPrincipal )

        #boton para registrar un usuario
        self.botonRegistro= QPushButton( 'Registarse' )
        self.botonRegistro.clicked.connect( self.ventanaRegistro )

        firstLayoutH = QHBoxLayout()
        secondLayoudH = QHBoxLayout()
        formLayoud = QFormLayout()

        firstLayoutH.addWidget( tituloPrincipalLabel )
        firstLayoutH.addWidget( self.userInput )
        secondLayoudH.addWidget( passWordLabel )
        secondLayoudH.addWidget( self.passWordInput )
       

        formLayoud.addRow( firstLayoutH )
        formLayoud.addRow( secondLayoudH )
        formLayoud.addRow( self.mirarContraseña )
        formLayoud.addRow( self.botonIngreso )
        formLayoud.addRow( self.botonRegistro )

        self.setLayout( formLayoud )

    def inicializarUI( self ):
        self.setGeometry( 100, 100, 350, 150 )
        self.setWindowTitle( "Condominio" )
        self.primeraVentana()
        self.show()
    
    def __init__( self ):
        super().__init__()
        self.inicializarUI()

if __name__ == '__main__':
    app=QApplication( sys.argv )
    ventana = NuevaInterfaz()
    sys.exit( app.exec() )
