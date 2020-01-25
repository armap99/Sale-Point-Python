#fuentes https://doc.qt.io/qtforpython/quickstart.html fuente https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html
import sys#Sistema
from PySide2.QtWidgets import QApplication
from VentanaConfg import MainWindow#Clase donde se configura la ventana
import pymysql #Base de Datos
#Diseño de ventana
#pyside2-uic mainwindow.ui > ui_mainwindow.py comando para transformar el diseño ui a py


db = pymysql.connect(host="localhost", port=3306, user="UsuarioVenta", passwd="123", db="Muebleria");

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(db)
    window.show()

    sys.exit(app.exec_())

db.close();