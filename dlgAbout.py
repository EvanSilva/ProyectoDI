# Form implementation generated from reading ui file '.\\templates\\dlgAbout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgAbout(object):
    def setupUi(self, dlgAbout):
        dlgAbout.setObjectName("dlgAbout")
        dlgAbout.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        dlgAbout.setEnabled(True)
        dlgAbout.resize(450, 427)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\\\templates\\../img/inmoteis.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgAbout.setWindowIcon(icon)
        dlgAbout.setModal(True)
        self.btnAbout = QtWidgets.QPushButton(parent=dlgAbout)
        self.btnAbout.setGeometry(QtCore.QRect(350, 390, 75, 23))
        self.btnAbout.setObjectName("btnAbout")
        self.lblAbout = QtWidgets.QLabel(parent=dlgAbout)
        self.lblAbout.setGeometry(QtCore.QRect(50, 20, 141, 111))
        self.lblAbout.setText("")
        self.lblAbout.setPixmap(QtGui.QPixmap(".\\\\templates\\../img/inmoteis.ico"))
        self.lblAbout.setScaledContents(True)
        self.lblAbout.setObjectName("lblAbout")
        self.line = QtWidgets.QFrame(parent=dlgAbout)
        self.line.setGeometry(QtCore.QRect(10, 140, 421, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.lblTerms1 = QtWidgets.QLabel(parent=dlgAbout)
        self.lblTerms1.setGeometry(QtCore.QRect(200, 10, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.lblTerms1.setFont(font)
        self.lblTerms1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblTerms1.setObjectName("lblTerms1")
        self.txtAbout = QtWidgets.QTextEdit(parent=dlgAbout)
        self.txtAbout.setEnabled(True)
        self.txtAbout.setGeometry(QtCore.QRect(20, 170, 401, 211))
        self.txtAbout.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.txtAbout.setAcceptDrops(False)
        self.txtAbout.setToolTip("")
        self.txtAbout.setStatusTip("")
        self.txtAbout.setWhatsThis("")
        self.txtAbout.setAccessibleName("")
        self.txtAbout.setAccessibleDescription("")
        self.txtAbout.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.txtAbout.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.txtAbout.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.txtAbout.setLineWidth(0)
        self.txtAbout.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.txtAbout.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.txtAbout.setUndoRedoEnabled(False)
        self.txtAbout.setReadOnly(True)
        self.txtAbout.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByKeyboard|QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextBrowserInteraction|QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.txtAbout.setObjectName("txtAbout")
        self.labelBua = QtWidgets.QLabel(parent=dlgAbout)
        self.labelBua.setGeometry(QtCore.QRect(20, 400, 291, 16))
        self.labelBua.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelBua.setOpenExternalLinks(True)
        self.labelBua.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByKeyboard|QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextBrowserInteraction|QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.labelBua.setObjectName("labelBua")

        self.retranslateUi(dlgAbout)
        QtCore.QMetaObject.connectSlotsByName(dlgAbout)

    def retranslateUi(self, dlgAbout):
        _translate = QtCore.QCoreApplication.translate
        dlgAbout.setWindowTitle(_translate("dlgAbout", "AboutUs"))
        self.btnAbout.setText(_translate("dlgAbout", "Aceptar"))
        self.lblTerms1.setText(_translate("dlgAbout", "INMOTEIS"))
        self.txtAbout.setHtml(_translate("dlgAbout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">[Inmoteis]</span><span style=\" font-size:8pt;\"><br />Versión 1.0.0</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Copyright © [1998-2024] Inmoteis&amp;Co. Todos los derechos reservados.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Este sitio web y su contenido están protegidos por derechos de autor y otras leyes de propiedad intelectual aplicables.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Licenciado a: Evan Silva González</span></p>\n"
"<hr />\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">El uso no autorizado de este sitio web, su contenido o materiales asociados puede dar lugar a acciones legales.</span></p></body></html>"))
        self.labelBua.setText(_translate("dlgAbout", "<p>Consulte nuestros <a href=\"http://www.youtube.com/watch?v=XfELJU1mRMg\">terminos y condiciones</a></p>"))
