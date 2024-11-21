import conexion
import conexionserver
import eventos
from propiedades import Propiedades
from venAux import *
from venPrincipal import *
import sys
import var
import styles
import clientes
import propiedades


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        var.uicalendar = Calendar()
        var.dlgAbrir = FileDialogAbrir()
        var.dlggestion = dlgGestionprop()
        var.dlgAbout = dlgAbout()

        self.setStyleSheet(styles.load_stylesheet())
        # conexion.Conexion.db_conexion(self)
        conexionserver.ConexionServer.crear_conexion(self)

        eventos.Eventos.cargarProv(self)
        eventos.Eventos.cargarMuni(self)
        var.historico = 1
        # conexionserver.ConexionServer()

        # eventos.Eventos.cargarTipoprop(self)
        eventos.Eventos.cargarProvProp(self)
        eventos.Eventos.cargarMuniProp(self)
        propiedades.Propiedades.cargaTablaPropiedades(self)

        var.ui.chkVentaprop.setEnabled(False)
        var.ui.chkAlquiprop.setEnabled(False)

        '''
        
        EVENTOS DE TABLAS
        '''

        clientes.Clientes.cargaTablaClientes(self)
        eventos.Eventos.resizeTablaClientes(self)
        var.ui.tablaClientes.clicked.connect(clientes.Clientes.cargaOneCliente)


        var.ui.tablaProp.clicked.connect(propiedades.Propiedades.cargaOnePropiedad)
        var.ui.tablaProp.clicked.connect(propiedades.Propiedades.habilitarCompraVenta)
        eventos.Eventos.resizeTablaPropiedades(self)




        '''

        ZONA DE EVENTOS DEL MENUBAR

        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionCrearBackup.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionRestaurar.triggered.connect(eventos.Eventos.restaurarBackup)
        var.ui.actionPropiedades.triggered.connect(eventos.Eventos.abrirTipoprop)
        var.ui.actionExportar_Propiedades_CSV.triggered.connect(eventos.Eventos.exportCSVProp)
        var.ui.actionExportar_Propiedades_JSON.triggered.connect(eventos.Eventos.exportJSONProp)
        var.ui.actionAbout.triggered.connect(eventos.Eventos.abrirAbout)
        '''

        EVENTOS DE LOS BOTONES

        '''

        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.btnAltacli.clicked.connect(lambda:  eventos.Eventos.abrirCalendar(0, 0))
        var.ui.btnBajacli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0, 1))
        var.ui.btnAltaprop.clicked.connect(lambda: eventos.Eventos.abrirCalendar(1, 0))
        var.ui.btnBajaprop.clicked.connect(lambda: eventos.Eventos.abrirCalendar(1, 1))
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifCliente)
        var.ui.btnDelcli.clicked.connect(clientes.Clientes.bajaCliente)
        var.ui.btnGrabarprop.clicked.connect(propiedades.Propiedades.altaPropiedad)
        var.ui.btnModifprop.clicked.connect(propiedades.Propiedades.modifPropiedad)
        var.ui.btnDelprop.clicked.connect(propiedades.Propiedades.bajaPropiedad)
        var.ui.btnBuscaTipoProp.clicked.connect(propiedades.Propiedades.cargaTablaPropiedades)
        var.ui.btnBuscarCli.clicked.connect(clientes.Clientes.buscarOneCliente)

        '''

        EVENTOS DE CAJAS DE TEXTO

        '''

        var.ui.txtDnicli.editingFinished.connect(lambda: clientes.Clientes.checkDNI(var.ui.txtDnicli.text()))
        var.ui.txtEmailcli.editingFinished.connect(lambda: clientes.Clientes.checkEmail(var.ui.txtEmailcli.text()))
        var.ui.txtMovilcli.editingFinished.connect(lambda: clientes.Clientes.checkNumero(var.ui.txtMovilcli.text()))
        var.ui.txtPrecioalquilerprop.textChanged.connect(propiedades.Propiedades.habilitarCompraVenta)
        var.ui.txtPrecioventaprop.textChanged.connect(propiedades.Propiedades.habilitarCompraVenta)

        '''
        
        EVENTOS DE LOS COMOBOX
        
        '''
        eventos.Eventos.cargarProv(self)
        eventos.Eventos.cargarProvProp(self)
        var.ui.cmbProvcli.currentIndexChanged.connect(eventos.Eventos.cargarMuni)
        var.ui.cmbProvprop.currentIndexChanged.connect(eventos.Eventos.cargarMuniProp)

        '''

        EVENTOS TOOLBAR

        '''

        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionbarLimpiar.triggered.connect(eventos.Eventos.limpiarPanel)
        var.ui.actionFiltrado.triggered.connect(propiedades.Propiedades.filtrar)
        var.ui.actionAddTipoPropiedad.triggered.connect(eventos.Eventos.abrirTipoprop)


        '''

        EVENTOS CHECKBOX

        '''

        var.ui.chkHistoriacli.stateChanged.connect(clientes.Clientes.historicoCli)
        var.ui.chkHistoricoprop.stateChanged.connect(propiedades.Propiedades.historicoProp)








if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())