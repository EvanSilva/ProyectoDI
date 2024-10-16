import locale
import sys
import time
import re
from datetime import datetime
import os
from fileinput import filename

from PyQt6 import QtWidgets, QtGui, QtSql

import clientes
import conexion
import eventos
import var

import zipfile
import shutil

from conexion import Conexion

#Establecer configuracion regional.
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

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

    def cargarMuni(self):
        var.ui.cmbMunicli.clear()
        municipios = conexion.Conexion.listarMunicli(var.ui.cmbProvcli.currentText())
        var.ui.cmbMunicli.addItems(municipios)

    def validarDNI(dni):
        try:
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    return True
                else:
                   return False
            else:
                return False

        except Exception as error:
            print("error en validar dni ", error)

    def abrirCalendar(pan, btn):
        try:
            var.panel = pan
            var.btn = btn
            var.uicalendar.show()
        except Exception as error:
            print("error en abrir calendar ", error)

    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            if var.panel == var.ui.panPrincipal.currentIndex() and var.btn == 0:
                var.ui.txtAltacli.setText(str(data))
            elif var.panel == var.ui.panPrincipal.currentIndex() and var.btn == 1:
                var.ui.txtBajacli.setText(str(data))

            time.sleep(0.5)
            var.uicalendar.hide()
            return data
        except Exception as error:
            print("error en cargar fecha: ", error)

    def validarMail(mail):
        mail = mail.lower()
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(regex, mail):
            return True
        else:
            return False

    def resizeTablaClientes(self):
        try:
            header = var.ui.tablaClientes.horizontalHeader()
            for i in range(header.count()):
                if (i == 1 or i == 2 or i == 4 or i == 5):
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                    header_items = var.ui.tablaClientes.horizontalHeaderItem(i)
                    font = header_items.font()
                    font.setBold(True)
                    header_items.setFont(font)
        except Exception as error:
            print("error en resize tabla clientes ", error)


    def crearBackup(self):
        try:
            fecha = datetime.now()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = str(fecha)+"_backup.zip"
            directorio, fichero = var.dlgAbrir.getSaveFileName(None, "Guardar Copia Seguridad", copia, '.zip')
            if var.dlgAbrir.accept and fichero:
                fichzip = zipfile.ZipFile(fichero, 'w')
                fichzip.write('bbdd.sqlite', os.path.basename('bbdd.sqlite'), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(fichero, directorio)

                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle("Copia de Seguridad")
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setText("Copia de Seguridad Guardada")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()


        except Exception as error:
            print("error en crear backup: ", error)

    def restaurarBackup(self):
        try:
            filename = var.dlgAbrir.getOpenFileName(None, "Restaurar Copia Seguridad", '',
                                                    '*.zip;;All Files(*)')
            file = filename[0]
            if file:
                with zipfile.ZipFile(file, 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle("Copia de Seguridad")
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setText("Copia de Seguridad Restaurada")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()


        except Exception as error:
            print("error en crear backup: ", error)

    def limpiarPanel(self):
        objetosPanel = [var.ui.txtDnicli,
                    var.ui.txtAltacli,
                    var.ui.txtApelcli,
                    var.ui.txtNomecli,
                    var.ui.txtEmailcli,
                    var.ui.txtMovilcli,
                    var.ui.txtDircli,
                    var.ui.cmbProvcli,
                    var.ui.cmbMunicli]

        for i, dato in enumerate(objetosPanel):
            if i == 7 or i == 8:
                pass
            else:
                dato.setText("")

            eventos.Eventos.cargarProv(dato)


