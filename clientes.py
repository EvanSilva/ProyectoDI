from PyQt6 import QtWidgets, QtGui


import conexion
import eventos
import var

class Clientes:

    def checkDNI(dni):
        try:
            dni = str(dni).upper()
            var.ui.txtDnicli.setText(str(dni))
            check = eventos.Eventos.validarDNI(dni)
            if check:
                var.ui.txtDnicli.setStyleSheet("background-color: #BEEEBA;")
            else:
                var.ui.txtDnicli.setStyleSheet('background-color:#FFC0CB;')  # y si no un aspa en color rojo
                var.ui.txtDnicli.setText(None)
                var.ui.txtDnicli.setFocus()
        except Exception as e:
            print("error check cliente", e)

    def altaCliente(self):
        print("suputamadre")
        nuevocli = [var.ui.txtDnicli.text(), var.ui.txtAltacli.text(), var.ui.txtApelcli.text(), var.ui.txtNomecli.text(), var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text(), var.ui.cmbProvcli.currentText(), var.ui.cmbMunicli.currentText()]
        if conexion.Conexion.altaCliente(nuevocli):
            mbox = QtWidgets.QMessageBox()
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
            mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
            mbox.setWindowTitle('Aviso')
            print("suputamadre2")
            mbox.setText('Alta Cliente en Base de Datos')
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('Aceptar')
            mbox.exec()
        else:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            print("suputamadre3")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
            mbox.setText('Error Faltan datos o Cliente existe')
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
            mbox.exec()


    def checkEmail(mail):
        try:
            mail = str(var.ui.txtEmailcli.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailcli.setStyleSheet('background-color: rgb(255, 255, 255);')
                var.ui.txtEmailcli.setText(mail.lower())

            else:
                var.ui.txtEmailcli.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtEmailcli.setText(None)
                var.ui.txtEmailcli.setText("correo no válido")
                var.ui.txtEmailcli.setFocus()

        except Exception as error:
            print("error check cliente", error)