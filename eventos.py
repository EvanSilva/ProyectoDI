import sys
import var
from PyQt6 import QtWidgets, QtGui

import conexion
import var


class Eventos():
    def mensajeSalir(self=None):
        mbox = QtWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
        mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
        mbox.setWindowTitle('Salir')
        mbox.setText('¿Desea usted salir?')
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Sí')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')

        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            mbox.hide()



    def cargarProv(self):
        var.ui.cmbProvcli.clear()
        listado = conexion.Conexion.listarProv(self)
        var.ui.cmbProvcli.addItems(listado)