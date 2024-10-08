from PyQt6 import QtWidgets

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
        dni = var.ui.txtDnicli.text()
        print(dni)

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