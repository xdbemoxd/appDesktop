import sys
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import ( QDialog, QHBoxLayout, QCheckBox, QApplication, 
                               QLabel, QLineEdit, QPushButton, QMessageBox )
from PySide6.QtGui import QFont, QPixmap

class VentanaRegistroView( QDialog ):

    def crearUsuario( self ):
        archivoUsuarios = "datos.txt"
        nombreUsuario = self.userInput.text()
        contrasena1 = self.passWordInput.text()
        contrasena2 = self.passWordInput2.text()

        if contrasena1 == '' or contrasena2 == '' or nombreUsuario == '' :
            QMessageBox.warning(self, 'error',
                                'Por favor no deje campos vacios',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close
                                )
        elif contrasena1 != contrasena2 :
             QMessageBox.warning(self, 'error',
                                'Las contraseñas son distintas',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close
                                )
        else:
            try:
                with open( archivoUsuarios, "a+" ) as f:
                    
                    f.write( f"{ nombreUsuario },{ contrasena1 }\n" )#guardado en un archivo txt

                QMessageBox.information(self, 'Creacion exitosa',#creacion de ventanas informativas o emergentes
                                        'Usuario creado con exito',
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)  
                
                self.close()

            except FileNotFoundError as e:
                QMessageBox.warning(self, 'error',
                                'La base de datos no existe',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close
                                )
           

    def cancelarCreacion( self ):
        self.close()
    
    def ventanaPrincipal( self ):
        self.setGeometry( 100, 100, 350, 250 )
        self.setWindowTitle( "Registro usuario" )

        

        tituloPrincipalLabel = QLabel( self )#donde se imprimen los datos
        tituloPrincipalLabel.setText( "Usuario:" )
        tituloPrincipalLabel.setFont( QFont( 'times new roman', 15 ) )
        tituloPrincipalLabel.move( 20, 44 )
        self.userInput = QLineEdit( self )#donde se cargan los datos
        self.userInput.resize( 250, 24 )
        self.userInput.move( 90, 40 )

        passWordLabel=QLabel( self )
        passWordLabel.setText( "Clave:" )
        passWordLabel.setFont( QFont( 'times new roman', 13 ) )
        passWordLabel.resize( 250, 24 )
        passWordLabel.move( 20, 74 ) 
        self.passWordInput= QLineEdit( self )
        self.passWordInput.resize( 250, 24 )
        self.passWordInput.move( 90, 70 )
        self.passWordInput.setEchoMode(
            QLineEdit.EchoMode.Password
        )


        passWordLabel2=QLabel( self )
        passWordLabel2.setText( "Clave:" )
        passWordLabel2.setFont( QFont( 'times new roman', 13 ) )
        passWordLabel2.resize( 250, 24 )
        passWordLabel2.move( 20, 104 ) 
        self.passWordInput2= QLineEdit( self )
        self.passWordInput2.resize( 250, 24 )
        self.passWordInput2.move( 90, 100 )
        self.passWordInput2.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.botonCrear = QPushButton( self )
        self.botonCrear.setText( "Crear usuario" )
        self.botonCrear.resize( 150, 32 )
        self.botonCrear.move( 20, 170 )
        self.botonCrear.clicked.connect( self.crearUsuario )

        self.botonCancelar = QPushButton( self )
        self.botonCancelar.setText( "Cancelar" )
        self.botonCancelar.resize( 150, 32 )
        self.botonCancelar.move( 170, 170 )
        self.botonCancelar.clicked.connect( self.cancelarCreacion )  


    def __init__( self ):
        super().__init__()
        self.setModal(True)
        self.ventanaPrincipal()
        
