'''Configuracion de la venta o creacion de funciones a los botones'''
#Fuente https://doc.qt.io/qtforpython/tutorials/expenses/expenses.html

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QHeaderView, QTableWidgetItem, QSpinBox, QMessageBox, QDialog
from PySide2.QtCore import Qt, Slot #Para botones
from Ventana import Ui_MainWindow
import pymysql



class MainWindow(QMainWindow):
    def __init__(self,Prueba):
        self.Carrito = {}
        self.db = Prueba
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.table = QTableWidget(self.ui.scrollAreaPrincipal);  # Creacion de Tabla
        self.TableCarro = QTableWidget(self.ui.scrollAreaPago)
        self.__activarBotones()
        self.__MostrarTabla()


    #Activar eventes de botones
    def __activarBotones(self):
        #self.NombreObjeto.NombreObjetoQT.connect(NombreDeFuncionConLaQueSEConecta) Botones
        self.ui.Agregar.clicked.connect(self.__agregarCarrp)
        self.ui.Pagar.clicked.connect(self.__pagarPedido)
        self.ui.lineEditBusqueda.textChanged.connect(self.__BusquedaNombre)
        self.ui.PagarDefinitivo.clicked.connect(self.__PagarFin)
        self.ui.pushButtonClientes.clicked.connect(self.__ListaClientes)
        self.ui.pushButtonCompras.clicked.connect(self.__ListasCompras)

    def __MostrarTabla(self):
        self.table.setColumnCount(6)#Numero de columnas
        self.table.setHorizontalHeaderLabels(["Id", "Nombre", "Precio", "Existencia", "Alto", "Ancho"])#Contenido de la columna
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#Ajustar Contenido
        self.table.resizeColumnsToContents()
        Contenido = self.db.cursor()
        Contenido.execute("select * from Articulo")
        NProductos = self.db.cursor()
        NProductos.execute("select count(*) from Articulo")#Para saber cuantos productos existen
        self.table.setRowCount(NProductos.fetchone()[0])#Generar las columnas para los productos

        i = 0
        for id, Nombre, Precio, Existencia, Altura, Ancho in Contenido.fetchall():#Llenar tabla
            id_item = QTableWidgetItem("{:d}".format(id))
            Nombre_item = QTableWidgetItem(Nombre)
            Precio_item = QTableWidgetItem("{:.2f}".format(Precio))
            Existencia_item = QTableWidgetItem("{:d}".format(Existencia))
            Altura_item = QTableWidgetItem("{:.2f}".format(Altura))
            Ancho_item = QTableWidgetItem("{:.2f}".format(Ancho))
            self.table.resizeColumnToContents(1)
            self.table.setItem(i, 0, id_item)
            self.table.setItem(i, 1, Nombre_item)
            self.table.setItem(i, 2, Precio_item)
            self.table.setItem(i, 3, Existencia_item)
            self.table.setItem(i, 4, Altura_item)
            self.table.setItem(i, 5, Ancho_item)
            i += 1

        self.ui.gridLayoutPrincipal.addWidget(self.table)#Agregar a la ventana

    def __BusquedaNombre(self):
        self.table.setRowCount(0);
        Contenido = self.db.cursor()
        Contenido.execute("select * from Articulo where Articulo.Nombre like '%"+self.ui.lineEditBusqueda.text() + "%'")
        NProductos = self.db.cursor()
        NProductos.execute("select count(*) from Articulo where Articulo.Nombre like '%"+self.ui.lineEditBusqueda.text() + "%'")  # Para saber cuantos productos existen
        self.table.setRowCount(NProductos.fetchone()[0])  # Generar las columnas para los productos
        i = 0
        for id, Nombre, Precio, Existencia, Altura, Ancho in Contenido.fetchall():  # Llenar tabla
            id_item = QTableWidgetItem("{:d}".format(id))
            Nombre_item = QTableWidgetItem(Nombre)
            Precio_item = QTableWidgetItem("{:.2f}".format(Precio))
            Existencia_item = QTableWidgetItem("{:d}".format(Existencia))
            Altura_item = QTableWidgetItem("{:.2f}".format(Altura))
            Ancho_item = QTableWidgetItem("{:.2f}".format(Ancho))
            self.table.resizeColumnToContents(1)
            self.table.setItem(i, 0, id_item)
            self.table.setItem(i, 1, Nombre_item)
            self.table.setItem(i, 2, Precio_item)
            self.table.setItem(i, 3, Existencia_item)
            self.table.setItem(i, 4, Altura_item)
            self.table.setItem(i, 5, Ancho_item)
            i += 1
        self.ui.gridLayoutPrincipal.addWidget(self.table)  # Agregar a la ventana

    def __agregarCarrp(self):
        if (self.ui.lineEditID.text().__len__() != 0) and (self.ui.spinBox.value() != 0):
            ProductoBuscado = self.db.cursor()
            data = self.ui.lineEditID.text()
            self.ui.lineEditID.clear()
            ProductoBuscado.execute("select * from Articulo where Articulo.id = " + data);
            if ProductoBuscado.fetchone() is None:
                Error = QMessageBox.warning(self,self.tr("Error"),self.tr("Id Inexistente"))
                return

            cantidad = self.ui.spinBox.value()
            ProductoBuscado.execute("select Existencia from Articulo where Articulo.id = "+data)
            if cantidad > ProductoBuscado.fetchone()[0]:
                Error = QMessageBox.warning(self, self.tr("Error"), self.tr("Inventario Insuficiente"))
                return
            else:
                self.Carrito[data] = cantidad
                self.ui.spinBox.setValue(0)


    def __pagarPedido(self):
        self.ui.Paginas.setCurrentIndex(1);
        self.__MostrarCompras()

    def __PagarFin(self):
        self.Carrito.clear();
        self.ui.Paginas.setCurrentIndex(0)

    def __MostrarCompras(self):
        Contenido = self.db.cursor()
        self.TableCarro.setColumnCount(4)
        self.TableCarro.setHorizontalHeaderLabels(["Id", "Nombre", "Cantidad", "Precio"])
        #self.TableCarro.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Ajustar Contenido
        #self.TableCarro.resizeColumnsToContents()
        self.TableCarro.setRowCount(self.Carrito.__len__())
        i = 0
        Total = 0
        for id in self.Carrito.keys():
            idItem = QTableWidgetItem(id)
            cantItem = QTableWidgetItem("{:d}".format(self.Carrito[id]))
            Contenido.execute("select Precio,Nombre from Articulo where Articulo.id = " + id);
            Resultado = Contenido.fetchall()
            precioItem = QTableWidgetItem("{:.2f}".format(Resultado[0][0]))
            nombreItem = QTableWidgetItem(Resultado[0][1])
            self.TableCarro.setItem(i, 0, idItem)
            self.TableCarro.setItem(i, 1, nombreItem)
            self.TableCarro.setItem(i, 2, cantItem)
            self.TableCarro.setItem(i, 3, precioItem)
            Total = Total + (self.Carrito[id] * Resultado[0][0])
            i += 1
        self.ui.gridLayoutPago.addWidget(self.TableCarro)
        self.ui.lineEditTotal.setText(Total.__str__())

    def __ListaClientes(self):
        #self.ui.gridLayoutPago.removeWidget(self.TableCarro)
        self.TableCarro.clear()
        self.TableCarro.setColumnCount(4)  # Numero de columnas
        self.TableCarro.setHorizontalHeaderLabels(
            ["RFC", "Nombre", "Apellidos", "Telefono"])  # Contenido de la columna
        #self.TableCarro.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Ajustar Contenido
        #self.TableCarro.resizeColumnsToContents()
        Contenido = self.db.cursor()
        Contenido.execute("select * from Cliente")
        NProductos = self.db.cursor()
        NProductos.execute("select count(*) from Cliente")  # Para saber cuantos productos existen
        self.TableCarro.setRowCount(NProductos.fetchone()[0])  # Generar las columnas para los productos
        i = 0
        for RFC,Nombre,Apellidos,Telefono in Contenido.fetchall():  # Llenar tabla
            RFC_item = QTableWidgetItem(RFC)
            Nombre_item = QTableWidgetItem(Nombre)
            Apellidos_item = QTableWidgetItem(Apellidos)
            Telefono_item = QTableWidgetItem(Telefono)
            self.TableCarro.setItem(i, 0, RFC_item)
            self.TableCarro.setItem(i, 1, Nombre_item)
            self.TableCarro.setItem(i, 2, Apellidos_item)
            self.TableCarro.setItem(i, 3, Telefono_item)
            i += 1

        self.ui.gridLayoutPago.addWidget(self.TableCarro)  # Agregar a la ventana

    def __ListasCompras(self):
        self.ui.gridLayoutPago.removeWidget(self.TableCarro)
        self.TableCarro.clear()
        self.__MostrarCompras()