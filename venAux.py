from datetime import datetime

import propiedades
from dlgCalendar import *
import var
import eventos
from dlgGestionprop import Ui_dlg_tipoprop


class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.uicalendar = Ui_dlgCalendar()
        var.uicalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year

        var.uicalendar.Calendar.setSelectedDate((QtCore.QDate(ano,mes,dia)))
        var.uicalendar.Calendar.clicked.connect(eventos.Eventos.cargaFecha)

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()

class dlgGestionprop(QtWidgets.QDialog):
    def __init__(self):
        super(dlgGestionprop, self).__init__()
        var.dlggestion = Ui_dlg_tipoprop()
        var.dlggestion.setupUi(self)
        var.dlggestion.btnAltatipoprop.clicked.connect(propiedades.Propiedades.altaTipopropiedad)