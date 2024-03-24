class Organizador_Materias():
 
    def __init__(self):
        self.lista_materias = []
        self.lista_materias.append({"Nombre":"Introducción a la programación", "Semestre":"2019-1", "Profesor":"Antonio Andrade", "Nota":4.5})
        self.lista_materias.append({"Nombre":"Estructuras de datos", "Semestre":"2019-2", "Profesor":"Hamid Abdallah", "Nota":3.5})
        self.lista_materias.append({"Nombre":"Desarrollo de software", "Semestre":"2020-1", "Profesor":"Rubby Casallas", "Nota":2.0})
        self.lista_materias.append({"Nombre":"Arquitectura de software", "Semestre":"2020-2", "Profesor":"Xiao Lihua", "Nota":4.0})
        self.actual = 0
        
    def dar_materia_actual(self):                        #Organizador_Materias:
        return self.lista_materias[self.actual]

    def avanzar(self):
        self.actual += 1
        self.actual = self.actual % len(self.lista_materias)

    def retroceder(self):
        self.actual -= 1
        self.actual = self.actual % len(self.lista_materias)
    
import sys
from gui.visor_materias import Aplicacion_Gui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QPushButton, 
QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.gui = Aplicacion_Gui()

class Aplicacion_Gui(QWidget):

    def __init__(self):
        super().__init__()

        #Se establecen las características de la ventana
        self.title = 'Mi aplicación'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320

class Aplicacion_Gui(QWidget):

    def __init__(self, logic):
        super().__init__()

        #Se establecen las características de la ventana
        self.title = 'Mi aplicación'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320
        self.inicializar_GUI()

    def inicializar_GUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    
    def inicializar_GUI(self):
        #inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
     
        #Creamos el distribuidor gráfico principal
        self.distr_vertical = QVBoxLayout()
        self.setLayout(self.distr_vertical)

        #Hacemos la ventana visible
        self.show()
    
    def inicializar_GUI(self):
        #inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
     
        #Creamos el distribuidor gráfico principal
        self.distr_vertical = QVBoxLayout()

        #Creamos la caja de materias
        self.caja_materias = QGroupBox("Materia")
        distr_caja_materias = QGridLayout()
        self.caja_materias.setLayout(distr_caja_materias)

        #Creamos la caja de botones
        self.caja_botones = QGroupBox()
        distr_caja_botones = QHBoxLayout()
        self.caja_botones.setLayout(distr_caja_botones)
        
        #Agregamos las cajas a nuestra aplicación
        self.distr_vertical.addWidget(self.caja_materias)
        self.distr_vertical.addWidget(self.caja_botones)

        #Definimos el distribuidor principal de la ventana.
        self.setLayout(self.distr_vertical)

        #Hacemos la ventana visible
        self.show()
    
    #Etiquetas, campos de texto y botones
    
    def inicializar_GUI(self):
        #inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Creamos el distribuidor gráfico principal
        self.distr_vertical = QVBoxLayout()

        #Creamos la caja de materias
        self.caja_materias = QGroupBox("Materia")
        distr_caja_materias = QGridLayout()
        self.caja_materias.setLayout(distr_caja_materias)

        #Creamos las etiquetas y campos de texto de la materia la caja de materias
        self.etiqueta_nombre = QLabel('Nombre')
        self.txt_nombre = QLineEdit()

        self.etiqueta_semestre = QLabel('Semestre')
        self.txt_semestre = QLineEdit()

        self.etiqueta_profesor = QLabel('Profesor')
        self.txt_profesor = QLineEdit()

        self.etiqueta_nota = QLabel('Nota')
        self.txt_nota = QLineEdit()


        #Creamos la caja de botones
        self.caja_botones = QGroupBox()
        distr_caja_botones = QHBoxLayout()
        self.caja_botones.setLayout(distr_caja_botones)
        
        #Agregamos las cajas a nuestra aplicación
        self.distr_vertical.addWidget(self.caja_materias)
        self.distr_vertical.addWidget(self.caja_botones)
        
        #Definimos el distribuidor principal de la ventana             
        self.setLayout(self.distr_vertical)

        #Hacemos la ventana visible
        self.show()
    
    #QGridLayout La primera coordenada representa la fila y la segunda la columna.
    
    def inicializar_GUI(self):
        #inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Creamos el distribuidor gráfico principal
        self.distr_vertical = QVBoxLayout()

        #Creamos la caja de materias
        self.caja_materias = QGroupBox("Materia")
        distr_caja_materias = QGridLayout()
        self.caja_materias.setLayout(distr_caja_materias)

        #Creamos las etiquetas y campos de texto de la materia la caja de materias
        self.etiqueta_nombre = QLabel('Nombre')
        self.txt_nombre = QLineEdit()

        self.etiqueta_semestre = QLabel('Semestre')
        self.txt_semestre = QLineEdit()

        self.etiqueta_profesor = QLabel('Profesor')
        self.txt_profesor = QLineEdit()

        self.etiqueta_nota = QLabel('Nota')
        self.txt_nota = QLineEdit()

        #Agregamos a la caja de materias las etiquetas
        distr_caja_materias.addWidget(self.etiqueta_nombre, 0,0)
        distr_caja_materias.addWidget(self.etiqueta_semestre, 1,0)
        distr_caja_materias.addWidget(self.etiqueta_profesor, 2,0)
        distr_caja_materias.addWidget(self.etiqueta_nota, 3,0)

        #Agregamos a la caja de materias los campos de texto
        distr_caja_materias.addWidget(self.txt_nombre, 0,1)
        distr_caja_materias.addWidget(self.txt_semestre, 1,1)
        distr_caja_materias.addWidget(self.txt_profesor, 2,1)
        distr_caja_materias.addWidget(self.txt_nota, 3,1)

        #Creamos la caja de botones
        self.caja_botones = QGroupBox()
        distr_caja_botones = QHBoxLayout()
        self.caja_botones.setLayout(distr_caja_botones)
        
        #Agregamos las cajas a nuestra aplicación
        self.distr_vertical.addWidget(self.caja_materias)
        self.distr_vertical.addWidget(self.caja_botones)
        
        #Definimos el distribuidor principal de la ventana             
        self.setLayout(self.distr_vertical)

        #Hacemos la ventana visible
        self.show()
    
    #addWidget(elemento, 0,1,1,1)
    #addWidget(elemento, 0,1,2,1)
    
    def inicializar_GUI(self):
        #inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Creamos el distribuidor gráfico principal
        self.distr_vertical = QVBoxLayout()

        #Creamos la caja de materias
        self.caja_materias = QGroupBox("Materia")
        distr_caja_materias = QGridLayout()
        self.caja_materias.setLayout(distr_caja_materias)

        #Creamos las etiquetas y campos de texto de la materia la caja de materias
        self.etiqueta_nombre = QLabel('Nombre')
        self.txt_nombre = QLineEdit()

        self.etiqueta_semestre = QLabel('Semestre')
        self.txt_semestre = QLineEdit()

        self.etiqueta_profesor = QLabel('Profesor')
        self.txt_profesor = QLineEdit()

        self.etiqueta_nota = QLabel('Nota')
        self.txt_nota = QLineEdit()

        #Agregamos a la caja de materias las etiquetas
        distr_caja_materias.addWidget(self.etiqueta_nombre, 0,0)
        distr_caja_materias.addWidget(self.etiqueta_semestre, 1,0)
        distr_caja_materias.addWidget(self.etiqueta_profesor, 2,0)
        distr_caja_materias.addWidget(self.etiqueta_nota, 3,0)

        #Agregamos a la caja de materias los campos de texto
        distr_caja_materias.addWidget(self.txt_nombre, 0,1)
        distr_caja_materias.addWidget(self.txt_semestre, 1,1)
        distr_caja_materias.addWidget(self.txt_profesor, 2,1)
        distr_caja_materias.addWidget(self.txt_nota, 3,1)

        #Creamos la caja de botones
        self.caja_botones = QGroupBox()
        distr_caja_botones = QHBoxLayout()
        self.caja_botones.setLayout(distr_caja_botones)
        
        #Creamos los botones para la caja de botones
        self.boton_retroceder = QPushButton("<<")
        self.boton_avanzar = QPushButton(">>")

        #Agregamos los botones a la caja de botones
        distr_caja_botones.addWidget(self.boton_retroceder)
        distr_caja_botones.addWidget(self.boton_avanzar)
       

        #Agregamos las cajas a nuestra aplicación
        self.distr_vertical.addWidget(self.caja_materias)
        self.distr_vertical.addWidget(self.caja_botones)
        
        #Definimos el distribuidor principal de la ventana             
        self.setLayout(self.distr_vertical)

        #Hacemos la ventana visible
        self.show()
    
    #self.caja_botones.setFixedHeight(50)
    #self.txt_nombre.setReadOnly(True)
    
    #Comunicación con la lógica de la aplicación
    def __init__(self, logica):
        super().__init__()

        #Se establecen las características de la ventana
        self.title = 'Mi aplicación'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320
        #Inicializamos la ventana principal
        self.inicializar_GUI()
        #Asignamos el valor de la lógica
        self.logica = logica
    
    #Organizador_Materias y Aplicacion_Gui pasando como parámetro la lógica
    
import sys
from logica.organizador_materias import Organizador_Materias
from gui.visor_materias import Aplicacion_Gui
from PyQt5.QtWidgets import QApplication


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.logica = Organizador_Materias()
        self.gui = Aplicacion_Gui(self.logica)
        
    #crear un método que actualice los valores de la interfaz por nosotros
    
    class Aplicacion_Gui(QWidget):

    def __init__(self, logica):
        super().__init__()

        #Se establecen las características de la ventana
        self.title = 'Mi aplicación'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320
        #Inicializamos la ventana principal
        self.inicializar_GUI()
        #Asignamos el valor de la lógica
        self.logica = logica
        self.actualizar_materia()
    
    def actualizar_materia(self):
        actual = self.logica.dar_materia_actual()
        self.txt_nombre.setText(actual["Nombre"])
        self.txt_semestre.setText(actual["Semestre"])
        self.txt_profesor.setText(actual["Profesor"])
        self.txt_nota.setText(str(actual["Nota"]))
    
    #Manejo de eventos de botón
    
    class Aplicacion_Gui(QWidget):

     def actualizar_materia(self):
          actual = self.logica.dar_materia_actual()
          self.txt_nombre.setText(actual["Nombre"])
          self.txt_semestre.setText(actual["Semestre"])
          self.txt_profesor.setText(actual["Profesor"])
          self.txt_nota.setText(str(actual["Nota"]))

     def avanzar_materia(self):
          self.logica.avanzar()
          self.actualizar_materia()
    
     def retroceder_materia(self):
          self.logica.retroceder()
          self.actualizar_materia()
          
    #clicked.connect de la clase QPushButton
    
    def inicializar_GUI(self):

        ...

        #Creamos la caja de botones
        self.caja_botones = QGroupBox()
        distr_caja_botones = QHBoxLayout()
        self.caja_botones.setFixedHeight(50)
        self.caja_botones.setLayout(distr_caja_botones)

        #Creamos los botones para la caja de botones
        self.boton_retroceder = QPushButton("<<")
        self.boton_retroceder.clicked.connect(self.retroceder_materia)
        self.boton_avanzar = QPushButton(">>")
        self.boton_avanzar.clicked.connect(self.avanzar_materia)

        #Agregamos los botones a la caja de botones
        distr_caja_botones.addWidget(self.boton_retroceder)
        distr_caja_botones.addWidget(self.boton_avanzar)

        ...

        #Hacemos la ventana visible
        self.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())








    
    
    