import time

from PyQt6 import QtWidgets, QtGui
from PyQt6 import QtCore

import conexion
import conexionserver
import eventos
import propiedades
import var


class Propiedades():

    def altaTipopropiedad(self):
        try:
            tipo = var.dlggestion.ui.txtGestipoprop.text().strip()  # Eliminar espacios
            if not tipo:  # Verificar que el tipo no esté vacío
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Por favor, ingrese un tipo de propiedad válido.')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
                return
            registro = conexion.Conexion.altaTipoprop(tipo)

            if registro is False:  # Si el registro es False, hubo un error al insertar
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error al dar de alta el tipo de propiedad, ya existe.')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
            else:  # Si se insertó correctamente, actualizar el combo box
                var.ui.cmbTipoprop.clear()
                var.ui.cmbTipoprop.addItems(registro)
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText(f'Tipo de propiedad "{tipo}", dado de alta.')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
                var.dlggestion.ui.txtGestipoprop.setText("")  # Limpiar solo si se da de alta
            print(tipo)

        except Exception as e:
            print("Error en altaTipopropiedad:", e)

    def bajaTipopropiedad(self):
        try:
            tipo = var.dlggestion.ui.txtGestipoprop.text().title()
            if (tipo):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad eliminada')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                conexion.Conexion.bajaTipoprop(tipo)
                registro = conexion.Conexion.cargarTipoprop(self)
                var.ui.cmbTipoprop.clear()
                var.ui.cmbTipoprop.addItems(registro)
                print(tipo)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Tipo de propiedad no existe')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()


        except Exception as e:
            print(e)

    def altaPropiedad(self):
        print("ALTAPROPIEDAD")
        try:
            propiedades = [var.ui.txtAltaprop.text(), var.ui.txtDirprop.text(),
                         var.ui.cmbProvprop.currentText(), var.ui.cmbMuniprop.currentText(), var.ui.cmbTipoprop.currentText(),
                         var.ui.spnHabprop.text(), var.ui.spnBanosprop.text(), var.ui.txtSuperprop.text(),
                         var.ui.txtPrecioalquilerprop.text(), var.ui.txtPrecioventaprop.text(), var.ui.txtCPprop.text(),
                         var.ui.txtObservaprop.toPlainText()
                         ]

            print("PRETIPOOPER")

            tipooper = []
            if var.ui.chkAlquiprop.isChecked():
                tipooper.append(var.ui.chkAlquiprop.text())

            if var.ui.chkVentaprop.isChecked():
                tipooper.append(var.ui.chkVentaprop.text())

            if var.ui.chkInterprop.isChecked():
                tipooper.append(var.ui.chkInterprop.text())
            propiedades.append(tipooper)
            if var.ui.rbtDisponprop.isChecked():
                propiedades.append(var.ui.rbtDisponprop.text())
            elif var.ui.rbtVentaprop.isChecked():
                propiedades.append(var.ui.rbtVentaprop.text())
            elif var.ui.rbtAlquiprop.isChecked():
                propiedades.append(var.ui.rbtAlquiprop.text())

            propiedades.append(var.ui.txtNomeprop.text())
            propiedades.append(var.ui.txtMovilprop.text())
            print("PRECOMPROBACION")

            if Propiedades.checkObligatoriosProp(self) and Propiedades.esMovilValido(propiedades[-1]):
                print("PASO DE CHECKOBLIGATORIOSY ESMOVILVALIDO")

                if conexionserver.ConexionServer.altaProp(propiedades):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText('Propiedad dada de Alta en Base de Datos')
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()
                    Propiedades.cargaTablaPropiedades(self)
                    return True
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                    mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                    mbox.setText("Error al dar de alta la propiedad")
                    mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                    mbox.exec()
                    return False

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setText("Faltan Datos Obligatorios, o los ofrecidos están mal formados")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()
                return False

            Propiedades.cargaTablaPropiedades(self)


            print(propiedades)
        except Exception as e:
            print("Error en propiedades, altaPropiedad(), " + e)

    def cargaTablaPropiedades(self):
        try:
            listado = conexionserver.ConexionServer.listadoPropiedades(self)
            index = 0
            var.ui.tablaProp.setRowCount(len(listado))
            for registro in listado:

                var.ui.tablaProp.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaProp.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tablaProp.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[6])))
                var.ui.tablaProp.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[7])))
                var.ui.tablaProp.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[8])))
                if registro[10] == "":
                    registro[10] = "-"
                if registro[11] == "":
                    registro[11] = "-"
                var.ui.tablaProp.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[10]) + " €" ))
                var.ui.tablaProp.setItem(index, 6, QtWidgets.QTableWidgetItem(str(registro[11]) + " €" ))

                string_limpio = registro[14].replace("[", "").replace("]", "").replace("'", "").strip()

                var.ui.tablaProp.setItem(index, 7, QtWidgets.QTableWidgetItem(string_limpio))
                var.ui.tablaProp.setItem(index, 8, QtWidgets.QTableWidgetItem(str(registro[15])))
                var.ui.tablaProp.setItem(index, 9, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tablaProp.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaProp.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaProp.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaProp.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaProp.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaProp.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaProp.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaProp.item(index, 7).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaProp.item(index, 8).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaProp.item(index, 9).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as e:
            print("error cargaTablaCientes", e)
            import traceback
            print(traceback.format_exc())

    def modifPropiedad(self):
        try:
            propiedades = [ var.ui.txtProp.text(),
                            var.ui.txtAltaprop.text(),
                            var.ui.txtBajaprop.text(),
                            var.ui.txtDirprop.text(),
                            var.ui.cmbProvprop.currentText(),
                            var.ui.cmbMuniprop.currentText(),
                            var.ui.cmbTipoprop.currentText(),
                            var.ui.spnHabprop.text(),
                            var.ui.spnBanosprop.text(),
                            var.ui.txtSuperprop.text(),
                            var.ui.txtPrecioalquilerprop.text(),
                            var.ui.txtPrecioventaprop.text(),
                            var.ui.txtCPprop.text(),
                            var.ui.txtObservaprop.toPlainText()
                           ]

            tipooper = []
            if var.ui.chkAlquiprop.isChecked():
                tipooper.append(var.ui.chkAlquiprop.text())

            if var.ui.chkVentaprop.isChecked():
                tipooper.append(var.ui.chkVentaprop.text())

            if var.ui.chkInterprop.isChecked():
                tipooper.append(var.ui.chkInterprop.text())
            propiedades.append(tipooper)
            if var.ui.rbtDisponprop.isChecked():
                propiedades.append(var.ui.rbtDisponprop.text())
            elif var.ui.rbtVentaprop.isChecked():
                propiedades.append(var.ui.rbtVentaprop.text())
            elif var.ui.rbtAlquiprop.isChecked():
                propiedades.append(var.ui.rbtAlquiprop.text())

            propiedades.append(var.ui.txtNomeprop.text())
            propiedades.append(var.ui.txtMovilprop.text())

            print("ESTAS SON LAS PROPIEDADES MODIFICAR: \n" )
            print(propiedades)

            if conexion.Conexion.modifPropiedad(propiedades):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Datos de la Propiedad Modificados')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Propiedades.cargaTablaPropiedades(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('ERROR AL MODIFICAR PROPIEDAD')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

        except Exception as e:
            print("Error en Modifpropiedad", e)

    def cargaOnePropiedad(self):
        try:
            fila = var.ui.tablaProp.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexionserver.ConexionServer.datosOnePropiedad(str(datos[0]))

            listado = [
                var.ui.txtProp,
                var.ui.txtAltaprop,
                var.ui.txtBajaprop,
                var.ui.txtDirprop,
                var.ui.cmbProvprop,
                var.ui.cmbMuniprop,
                var.ui.cmbTipoprop,
                var.ui.spnHabprop,
                var.ui.spnBanosprop,
                var.ui.txtSuperprop,
                var.ui.txtPrecioalquilerprop,
                var.ui.txtPrecioventaprop,
                var.ui.txtCPprop,
                var.ui.txtObservaprop,

                [var.ui.chkAlquiprop,
                var.ui.chkVentaprop,
                var.ui.chkInterprop],

                [var.ui.rbtDisponprop,
                var.ui.rbtAlquiprop,
                var.ui.rbtVentaprop],

                var.ui.txtNomeprop,
                var.ui.txtMovilprop
            ]

            print(len(registro))
            print(len(listado))

            for i, casilla in enumerate(listado):
                if isinstance(casilla, QtWidgets.QLineEdit):
                    casilla.setText(str(registro[i]))
                elif isinstance(casilla, QtWidgets.QComboBox):
                    casilla.setCurrentText(registro[i])
                elif isinstance(casilla, QtWidgets.QSpinBox):
                    casilla.setValue(int(registro[i]))
                elif isinstance(casilla, QtWidgets.QTextEdit):
                    casilla.setText(str(registro[i]))
                elif isinstance(casilla, list):
                    for subcasilla in casilla:
                        if isinstance(subcasilla, QtWidgets.QCheckBox):
                            if subcasilla.text() in registro[14]:
                                subcasilla.setChecked(True)
                            else:
                                subcasilla.setChecked(False)

                        elif isinstance(subcasilla, QtWidgets.QRadioButton):
                            if subcasilla.text() == registro[15]:
                                subcasilla.setChecked(True)
                            else:
                                subcasilla.setChecked(False)

        except Exception as e:
            print("Error en cargaOnePropiedad", e)

    def bajaPropiedad(self):
        try:
            datos = [var.ui.txtBajaprop.text(), var.ui.txtProp.text()]
            if conexion.Conexion.bajaPropiedad(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Cliente Dado de Baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                Propiedades.cargaTablaPropiedades(self)
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('ERROR AL DAR DE BAJA AL CLIENTE')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

        except Exception as e:
            print("Error en bajaCliente", e)


    def checkObligatoriosProp(self):
        try:
            textos = [var.ui.txtAltaprop.text(),
                      var.ui.txtDirprop.text(),
                      var.ui.txtSuperprop.text(),
                      var.ui.txtCPprop.text(),
                      var.ui.txtNomeprop.text(),
                      var.ui.txtMovilprop.text()]

            for texto in textos:
                if eventos.Eventos.checkTxtVacio(texto):
                    return False

            return True

        except Exception as e:
            print("error check obligatorios", e)

    def esMovilValido(movil):

        print("LLEGO AL VALIDADOR DEL MOVIL")
        if len(movil) == 13 and movil.startswith("+") and movil[3] == " " and movil[4:].isdigit():
            print("- TRUE")
            return True
        return False
        print("- FALSE")

    def filtrar(self):
        checkeado = var.ui.btnBuscaTipoProp.isChecked()
        var.ui.btnBuscaTipoProp.setChecked(not checkeado)
        Propiedades.cargaTablaPropiedades(self)


    def historicoProp(Self):
        try:
            if var.ui.chkHistoricoprop.isChecked():
                var.historico = 0

            else:
                var.historico = 1

            Propiedades.cargaTablaPropiedades(Self)
        except Exception as Error:
            print("Checkbox Historico", Error)

    def habilitarCompraVenta(self):

        txtCompraVenta = [var.ui.txtPrecioventaprop, var.ui.txtPrecioalquilerprop]

        lblCompraVenta = [var.ui.chkVentaprop, var.ui.chkAlquiprop]

        if var.ui.txtPrecioventaprop.text() == "":
            var.ui.chkVentaprop.setChecked(False)
            var.ui.chkVentaprop.setEnabled(False)
        else:
            var.ui.chkVentaprop.setChecked(True)
            var.ui.chkVentaprop.setEnabled(True)

        if var.ui.txtPrecioalquilerprop.text() == "":
            var.ui.chkAlquiprop.setChecked(False)
            var.ui.chkAlquiprop.setEnabled(False)

        else:
            var.ui.chkAlquiprop.setChecked(True)
            var.ui.chkAlquiprop.setEnabled(True)


